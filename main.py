import cv2
import numpy as np
from hand_tracking import HandTracker
from ui_utils import draw_toolbar, draw_footer

cap = cv2.VideoCapture(0)
tracker = HandTracker()

canvas = None
prev_x, prev_y = 0, 0
mode = "IDLE"

# Writing parameters
movement_threshold = 6
alpha = 0.3
pen_thickness = 2

# Stroke control
is_writing = False
stable_counter = 0
stable_threshold = 3   # frames needed before writing starts

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    result = tracker.detect_hands(frame)
    landmarks = tracker.get_landmarks(frame, result)
    fingers = tracker.fingers_up(landmarks)

    if landmarks and len(landmarks) > 8 and fingers:

        x, y = landmarks[8]

        # ✍ WRITE MODE (Only index finger)
        if fingers == [1, 0, 0, 0]:
            mode = "WRITE"

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            dx = abs(x - prev_x)
            dy = abs(y - prev_y)

            # Check if movement is controlled
            if dx > movement_threshold or dy > movement_threshold:
                stable_counter += 1
            else:
                stable_counter = 0

            # Activate writing only after stable movement
            if stable_counter >= stable_threshold:
                is_writing = True

            if is_writing:
                smooth_x = int(alpha * x + (1 - alpha) * prev_x)
                smooth_y = int(alpha * y + (1 - alpha) * prev_y)

                cv2.line(canvas,
                         (prev_x, prev_y),
                         (smooth_x, smooth_y),
                         (0, 0, 255),
                         pen_thickness)

                prev_x, prev_y = smooth_x, smooth_y

        # 🧽 ERASE MODE
        elif fingers[0] == 1 and fingers[1] == 1:
            mode = "ERASE"
            cv2.circle(canvas, (x, y), 25, (0, 0, 0), -1)
            is_writing = False
            stable_counter = 0
            prev_x, prev_y = 0, 0

        # ✋ Pen Up (Stop Writing)
        else:
            mode = "IDLE"
            is_writing = False
            stable_counter = 0
            prev_x, prev_y = 0, 0

    # Merge canvas
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    draw_toolbar(frame, mode)
    draw_footer(frame)

    cv2.imshow("Air Writing System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
