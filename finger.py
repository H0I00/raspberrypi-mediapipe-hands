import cv2
import mediapipe as mp
from picamera2 import Picamera2

# 初始化摄像头
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

# MediaPipe 初始化
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:
        frame = picam2.capture_array()

        # 有时 Picamera2 输出 4 通道（XBGR8888），裁掉 alpha 通道
        if frame.ndim == 3 and frame.shape[2] == 4:
            frame = frame[:, :, :3].copy()

        # BGR -> RGB 给 MediaPipe 处理
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        # 绘制关键点到原始 BGR 帧
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

        cv2.imshow("MediaPipe Hands", frame)

        # 按 ESC 退出
        if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.destroyAllWindows()
