import cv2
import mediapipe as mp


# --------------------------------------------------
# MEDIAPIPE SETUP
# --------------------------------------------------

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


# --------------------------------------------------
# VARIABLES
# --------------------------------------------------

prev_x = None
prev_y = None

canvas = None


# --------------------------------------------------
# HAND CONNECTIONS
# --------------------------------------------------

HAND_CONNECTIONS = [
    # Thumb
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),

    # Index finger
    (0, 5),
    (5, 6),
    (6, 7),
    (7, 8),

    # Middle finger
    (5, 9),
    (9, 10),
    (10, 11),
    (11, 12),

    # Ring finger
    (9, 13),
    (13, 14),
    (14, 15),
    (15, 16),

    # Pinky
    (13, 17),
    (17, 18),
    (18, 19),
    (19, 20),

    # Palm
    (0, 17)
]


# --------------------------------------------------
# MEDIAPIPE OPTIONS
# --------------------------------------------------

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=r"D:\PythonPractice\Practice_Python\etc\hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO
)


# --------------------------------------------------
# CAMERA
# --------------------------------------------------

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


# --------------------------------------------------
# HAND LANDMARKER
# --------------------------------------------------

with HandLandmarker.create_from_options(options) as landmarker:

    frame_number = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Camera not opened!")
            break


        # Mirror camera
        frame = cv2.flip(frame, 1)


        # Create canvas
        if canvas is None:
            canvas = frame.copy()
            canvas[:] = 0


        # --------------------------------------------------
        # MEDIAPIPE IMAGE
        # --------------------------------------------------

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )


        # Timestamp
        timestamp_ms = frame_number * 33
        frame_number += 1


        # Detect hand
        result = landmarker.detect_for_video(
            mp_image,
            timestamp_ms
        )


        # --------------------------------------------------
        # HAND DETECTED
        # --------------------------------------------------

        if result.hand_landmarks:

            hand = result.hand_landmarks[0]


            # --------------------------------------------------
            # DRAW 21 HAND LANDMARKS
            # --------------------------------------------------

            points = []

            for landmark in hand:

                x = int(
                    landmark.x * frame.shape[1]
                )

                y = int(
                    landmark.y * frame.shape[0]
                )

                points.append((x, y))


            # --------------------------------------------------
            # DRAW CONNECTION LINES
            # --------------------------------------------------

            for start, end in HAND_CONNECTIONS:

                cv2.line(
                    frame,
                    points[start],
                    points[end],
                    (255, 255, 255),
                    2
                )


            # --------------------------------------------------
            # DRAW RED LANDMARK POINTS
            # --------------------------------------------------

            for x, y in points:

                cv2.circle(
                    frame,
                    (x, y),
                    4,
                    (0, 0, 255),
                    -1
                )


            # --------------------------------------------------
            # INDEX FINGER
            # --------------------------------------------------

            index_tip = hand[8]
            index_middle = hand[7]


            # Check index finger open
            if index_tip.y < index_middle.y:

                x = int(
                    index_tip.x * frame.shape[1]
                )

                y = int(
                    index_tip.y * frame.shape[0]
                )


                # Green dot on index finger
                cv2.circle(
                    frame,
                    (x, y),
                    7,
                    (0, 255, 0),
                    -1
                )


                # --------------------------------------------------
                # AIR DRAWING
                # --------------------------------------------------

                if prev_x is not None and prev_y is not None:

                    distance = max(
                        abs(x - prev_x),
                        abs(y - prev_y)
                    )

                    # Extra points for fast movement
                    steps = max(
                        1,
                        distance // 3
                    )


                    for i in range(
                        1,
                        steps + 1
                    ):

                        new_x = int(
                            prev_x +
                            (x - prev_x) * i / steps
                        )

                        new_y = int(
                            prev_y +
                            (y - prev_y) * i / steps
                        )


                        cv2.circle(
                            canvas,
                            (new_x, new_y),
                            3,
                            (255, 0, 0),
                            -1
                        )


                prev_x = x
                prev_y = y


            else:

                # Index finger closed
                prev_x = None
                prev_y = None


        else:

            # Hand not detected
            prev_x = None
            prev_y = None


        # --------------------------------------------------
        # COMBINE CAMERA + DRAWING
        # --------------------------------------------------

        output = cv2.addWeighted(
            frame,
            1,
            canvas,
            1,
            0
        )


        # --------------------------------------------------
        # SHOW
        # --------------------------------------------------

        cv2.imshow(
            "Hand Tracking + Air Drawing",
            output
        )


        # --------------------------------------------------
        # KEYBOARD
        # --------------------------------------------------

        key = cv2.waitKey(1) & 0xFF


        # C = CLEAR
        if key == ord('c'):

            canvas[:] = 0

            prev_x = None
            prev_y = None


        # S = SAVE
        if key == ord('s'):

            cv2.imwrite(
                "my_drawing.png",
                canvas
            )

            print("Drawing saved successfully!")


        # ESC = EXIT
        if key == 27:
            break


# --------------------------------------------------
# RELEASE
# --------------------------------------------------

cap.release()
cv2.destroyAllWindows()     