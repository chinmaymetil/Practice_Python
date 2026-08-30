import cv2
import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


# Previous finger position
prev_x = None
prev_y = None

# Drawing canvas
canvas = None


# MediaPipe options
options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=r"D:\PythonPractice\Practice_Python\etc\hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO
)


# Open camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


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


        # Convert to MediaPipe image
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


        # Check hand detected
        if result.hand_landmarks:

            hand = result.hand_landmarks[0]


            # Index finger tip = 8
            index_tip = hand[8]

            # Index finger middle joint = 6
            index_middle = hand[7]


            # Check index finger is OPEN
            if index_tip.y < index_middle.y:

                # Convert to screen coordinates
                x = int(index_tip.x * frame.shape[1])
                y = int(index_tip.y * frame.shape[0])


                # Green dot
                cv2.circle(
                    frame,
                    (x, y),
                    7,
                    (0, 255, 0),
                    -1
                )


                # Draw line
                if prev_x is not None and prev_y is not None:

                    distance = max(
                        abs(x - prev_x),
                        abs(y - prev_y)
                    )

                    # Extra points for fast movement
                    steps = max(1, distance // 3)


                    for i in range(1, steps + 1):

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


                # Update position
                prev_x = x
                prev_y = y


            else:

                # ✊ Fist / Index closed
                # Stop drawing
                prev_x = None
                prev_y = None


        else:

            # No hand detected
            prev_x = None
            prev_y = None


        # Combine camera + drawing
        output = cv2.addWeighted(
            frame,
            1,
            canvas,
            1,
            0
        )


        # Show
        cv2.imshow(
            "Air Drawing",
            output
        )


        # Keyboard
        key = cv2.waitKey(1) & 0xFF


        # C = Clear
        if key == ord('c'):

            canvas[:] = 0

            prev_x = None
            prev_y = None


        # S = Save
        if key == ord('s'):

            cv2.imwrite(
                "my_drawing.png",
                canvas
            )

            print("Drawing saved successfully!")


        # ESC = Exit
        if key == 27:
            break


# Release
cap.release()
cv2.destroyAllWindows()