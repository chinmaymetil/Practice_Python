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

signature = None


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


        # --------------------------------------------------
        # CREATE SIGNATURE PAD
        # --------------------------------------------------

        if signature is None:

            signature = 255 * \
                __import__("numpy").ones(
                    (480, 640, 3),
                    dtype="uint8"
                )


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


            # Index finger
            index_tip = hand[8]
            index_middle = hand[6]


            # --------------------------------------------------
            # CHECK INDEX FINGER OPEN
            # --------------------------------------------------

            if index_tip.y < index_middle.y:

                # Camera coordinates
                x = int(
                    index_tip.x *
                    frame.shape[1]
                )

                y = int(
                    index_tip.y *
                    frame.shape[0]
                )


                # --------------------------------------------------
                # GREEN DOT
                # --------------------------------------------------

                cv2.circle(
                    frame,
                    (x, y),
                    7,
                    (0, 255, 0),
                    -1
                )


                # --------------------------------------------------
                # DRAW SIGNATURE
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
                            (x - prev_x)
                            * i / steps
                        )

                        new_y = int(
                            prev_y +
                            (y - prev_y)
                            * i / steps
                        )


                        cv2.line(
                            signature,
                            (prev_x, prev_y),
                            (new_x, new_y),
                            (0, 0, 0),
                            4,
                            cv2.LINE_AA
                        )


                        prev_x = new_x
                        prev_y = new_y


                else:

                    prev_x = x
                    prev_y = y


            else:

                # --------------------------------------------------
                # FIST / INDEX CLOSED
                # --------------------------------------------------

                prev_x = None
                prev_y = None


        else:

            # Hand not detected
            prev_x = None
            prev_y = None


        # --------------------------------------------------
        # DISPLAY CAMERA
        # --------------------------------------------------

        cv2.putText(
            frame,
            "INDEX FINGER = SIGN",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


        cv2.putText(
            frame,
            "FIST = STOP",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )


        # --------------------------------------------------
        # DISPLAY SIGNATURE PAD
        # --------------------------------------------------

        cv2.putText(
            signature,
            "DIGITAL SIGNATURE",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (120, 120, 120),
            2
        )


        cv2.putText(
            signature,
            "C = CLEAR     S = SAVE     ESC = EXIT",
            (20, 460),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (120, 120, 120),
            2
        )


        # --------------------------------------------------
        # SHOW WINDOWS
        # --------------------------------------------------

        cv2.imshow(
            "Camera",
            frame
        )

        cv2.imshow(
            "Digital Signature Pad",
            signature
        )


        # --------------------------------------------------
        # KEYBOARD CONTROLS
        # --------------------------------------------------

        key = cv2.waitKey(1) & 0xFF


        # CLEAR
        if key == ord("c"):

            signature[:] = 255

            prev_x = None
            prev_y = None

            print("Signature cleared!")


        # SAVE
        if key == ord("s"):

            cv2.imwrite(
                "digital_signature.png",
                signature
            )

            print(
                "Signature saved as digital_signature.png"
            )


        # EXIT
        if key == 27:
            break


# --------------------------------------------------
# RELEASE
# --------------------------------------------------

cap.release()
cv2.destroyAllWindows()