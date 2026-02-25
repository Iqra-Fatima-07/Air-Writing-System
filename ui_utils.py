import cv2

def draw_toolbar(frame, mode):
    cv2.putText(frame, "AIR WRITING SYSTEM",
                (180, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2)

    cv2.putText(frame, f"MODE: {mode}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2)


def draw_footer(frame):
    h, w, _ = frame.shape

    cv2.putText(frame,
                "Index Finger: Write  |  Two Fingers: Erase",
                (40, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                1)
