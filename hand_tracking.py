import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        import cv2
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        return result

    def get_landmarks(self, frame, result):
        landmarks_list = []
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
                h, w, _ = frame.shape
                for lm in hand_landmarks.landmark:
                    landmarks_list.append((int(lm.x * w), int(lm.y * h)))
        return landmarks_list

    def fingers_up(self, landmarks):
        if not landmarks:
            return []

        tips = [8, 12, 16, 20]
        fingers = []

        for tip in tips:
            if landmarks[tip][1] < landmarks[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
