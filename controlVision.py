import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False
screen_w, screen_h = pyautogui.size()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Tentative d’ouverture de la caméra
try:
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        raise RuntimeError("Cannot open camera")
except Exception as e:
    print(f"Camera initialization failed: {e}")
    exit()

try:
    while True:
        ret, frame = cam.read()
        if not ret or frame is None or frame.size == 0:
            print("Empty or invalid frame")
            continue
        frame = cv2.flip(frame, 1)   # Inverser horizontalement l'image (effet miroir)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)  # Traitement pour détecter les mains
        frame_h, frame_w, _ = frame.shape

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                index_tip = landmarks[8]
                index_x = int(index_tip.x * frame_w)
                index_y = int(index_tip.y * frame_h)
                
                # Dessiner un cercle vert sur le bout de l'index
                cv2.circle(frame, (index_x, index_y), 8, (0, 255, 0), -1)

                # Calculer la position de la souris à l'échelle de l'écran
                screen_x = screen_w * index_tip.x
                screen_y = screen_h * index_tip.y

                # Déplacer la souris à la position calculée
                pyautogui.moveTo(screen_x, screen_y)

                # Détecter quels doigts sont levés
                fingers_up = []
                fingers_up.append(1 if landmarks[8].y < landmarks[6].y else 0)
                fingers_up.append(1 if landmarks[12].y < landmarks[10].y else 0)
                fingers_up.append(1 if landmarks[16].y < landmarks[14].y else 0)
                fingers_up.append(1 if landmarks[20].y < landmarks[18].y else 0)
                if fingers_up == [1, 0, 0, 0]:
                    pyautogui.click()
                    pyautogui.sleep(1)  # Pause d’une seconde pour éviter des clics multiples
            
                # Dessiner les connexions des points de la main sur la frame    
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow("Finger Controlled Mouse", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cam.release()
    cv2.destroyAllWindows()
