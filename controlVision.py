import cv2 #capturer et afficher les images du webcam
import mediapipe as mp #pour la détection des mains
import pyautogui#déplacer lza souris et faire des clics

pyautogui.FAILSAFE = False #Désactive la sécurité automatique de PyAutoGUI (évite qu'il bloque si la souris va dans un coin).
screen_w, screen_h = pyautogui.size() #Récupère les dimensions de l'écran (largeur et hauteur).
mp_hands = mp.solutions.hands#Charge le module de détection des mains.
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)#Configure pour détecter une seule main avec une confiance minimale de 70 %.
mp_draw = mp.solutions.drawing_utils #Prépare un outil pour dessiner les repères sur l'image(les lignes d'articulation etc).

try:
    cam = cv2.VideoCapture(0)#Ouvre la caméra.
    if not cam.isOpened():
        raise RuntimeError("Cannot open camera")
except Exception as e:
    print(f"Camera initialization failed: {e}")
    exit()

try:
    while True:
        ret, frame = cam.read()#ret est booléen frame est un tableau
        if not ret or frame is None or frame.size == 0:
            print("Empty or invalid frame")
            continue
        frame = cv2.flip(frame, 1) #pivoter l'image effet miroir pour rendre l'interaction plus naturelle
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)#result va contenir les information de l'image rgb traitée
        frame_h, frame_w, _ = frame.shape #frame.shape  ➔ (480, 640, 3) la troisième valeur est le nb de canaux couleur (que j'ai pas besoin)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark #On extrait la liste des landmarks de cette main,Chaque landmark est une position (x, y, z) normalisée (valeurs entre 0 et 1).
                index_tip = landmarks[8]#On récupère le landmark numéro 8, qui correspond à l’extrémité (bqout) de l’index.
                screen_x = screen_w * index_tip.x
                screen_y = screen_h * index_tip.y
                pyautogui.moveTo(screen_x, screen_y)#Déplace le curseur de la souris à la position (screen_x, screen_y) sur ton écran,où ton doigt bouge, la souris suit !
                fingers_up = []
                fingers_up.append(1 if landmarks[8].y < landmarks[6].y else 0)  # Index
                fingers_up.append(1 if landmarks[12].y < landmarks[10].y else 0)  # Majeur
                fingers_up.append(1 if landmarks[16].y < landmarks[14].y else 0)  # Annulaire
                fingers_up.append(1 if landmarks[20].y < landmarks[18].y else 0)  # Auriculaire

                if fingers_up == [1, 1, 0, 0]:
                    pyautogui.click()
                    pyautogui.sleep(1)  #Petite pause 1 ms après le clic pour éviter les clics répétés trop rapides.
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)#Dessine les lignes et les points des articulations de la main sur l’image.
        cv2.imshow("Finger Controlled Mouse", frame)#Affiche la vidéo en temps réel avec les annotations.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cam.release()#Libère la caméra.
    cv2.destroyAllWindows()
