# ControlVision
This our Computer Vision' Project / Amir Sghaier & Anis Kchaou

# Étude de Projet — *ControlVision*

# 1. Titre et objectif du projet
**ControlVision** — Contrôle du curseur de la souris par reconnaissance gestuelle de la main à l'aide de la vision par ordinateur.

L'objectif est de développer une application utilisant une webcam pour permettre le contrôle du curseur de la souris via les mouvements de la main, en suivant l’index pour le déplacement et en utilisant la fermeture de la main pour effectuer un clic.

---

# 2. Motivation
- Rendre l'interaction homme-machine plus naturelle et sans contact.
- Proposer une solution d'accessibilité pour les personnes ayant des difficultés motrices à utiliser une souris traditionnelle.
- Expérimenter des technologies de vision par ordinateur et d'interaction gestuelle.

---

# 3. Technologies utilisées
- Python : Langage de programmation principal
- OpenCV : Capture et traitement de la vidéo
- Mediapipe : Détection des mains et des points clés (landmarks)
- PyAutoGUI : Contrôle du curseur et clic de la souris

---

# 4. Fonctionnalités
- Suivi de la main en temps réel.
- Détection de l’index (point 8 dans Mediapipe).
- Déplacement du curseur basé sur la position de l’index.
- Détection de la fermeture de la main pour effectuer un clic.

---

# 5. Méthodologie
1. **Capture vidéo** avec OpenCV.
2. **Détection de la main** avec Mediapipe.
3. **Repérage des landmarks** pour obtenir la position de l’index.
4. **Conversion des coordonnées** caméra vers coordonnées écran.
5. **Suivi du curseur** avec PyAutoGUI.
6. **Détection d’un clic** par la distance entre les doigts (compression de la main).

---

# 6. Résultats attendus
- Une interface intuitive qui permet de contrôler la souris sans contact.
- Réactivité fluide et temps réel.
- Précision suffisante pour une utilisation basique.

---

### 🚀 8. **Améliorations futures**
- Ajout de gestes supplémentaires (clic droit, scroll, drag & drop).
- Interface utilisateur avec options de calibrage.
- Entraînement personnalisé pour reconnaître les gestes d’un utilisateur spécifique.


