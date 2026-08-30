import cv2
import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

prev_x = None
prev_y = None
canvas = None


# Callback function
def print_result(result, output_image, timestamp_ms):

    global prev_x, prev_y, canvas

    if not result.hand_landmarks:
        prev_x = None
        prev_y = None
        return

    # First hand
    hand = result.hand_landmarks[0]

    # Index finger tip = 8
    x = int(hand[8].x * output_image.width)
    y = int(hand[8].y * output_image.height)

    # Draw line
    if prev_x is not None and prev_y is not None:

        cv2.line(
            canvas,
            (prev_x, prev_y),
            (x, y),
            (255, 0, 0),
            5,
            cv2.LINE_AA
        )

    # Update position
    prev_x = x
    prev_y = y


# MediaPipe options
options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=r"D:\PythonPractice\Practice_Python\etc\hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result
)


# Camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


with HandLandmarker.create_from_options(options) as landmarker:

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

        # Convert image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )

        # Timestamp
        timestamp = int(cap.get(cv2.CAP_PROP_POS_MSEC))

        # Detect hand
        landmarker.detect_async(
            mp_image,
            timestamp
        )

        # Show camera + drawing
        output = cv2.addWeighted(
            frame,
            1,
            canvas,
            1,
            0
        )

        cv2.imshow("Finger Drawing", output)

        key = cv2.waitKey(1) & 0xFF

        # Clear drawing
        if key == ord('c'):
            canvas[:] = 0
            prev_x = None
            prev_y = None

        # Exit
        if key == 27:
            break


cap.release()
cv2.destroyAllWindows()