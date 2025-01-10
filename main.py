import cv2
import numpy as np
import mediapipe as mp

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# classifying landmarks
def classify_hand_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    
    # Check for 'Paper' - all fingers extended
    if (thumb_tip[1] < landmarks[3][1] and 
        index_tip[1] < landmarks[7][1] and
        middle_tip[1] < landmarks[11][1] and
        ring_tip[1] < landmarks[15][1] and
        pinky_tip[1] < landmarks[19][1]):
        return 'paper'

    # Check for 'Rock' - all fingers curled in
    if (thumb_tip[1] > landmarks[3][1] and
        index_tip[1] > landmarks[7][1] and
        middle_tip[1] > landmarks[11][1] and
        ring_tip[1] > landmarks[15][1] and
        pinky_tip[1] > landmarks[19][1]):
        return 'rock'
    
    # Check for 'Scissors' - index and middle finger extended, others curled
    if (index_tip[1] < landmarks[7][1] and
        middle_tip[1] < landmarks[11][1] and
        thumb_tip[1] > landmarks[3][1] and
        ring_tip[1] > landmarks[15][1] and
        pinky_tip[1] > landmarks[19][1]):
        return 'scissors'

    # Default case
    return 'unknown'

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB and get landmarks
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # If found classify the gesture
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            hand_landmarks = [(landmark.x, landmark.y) for landmark in landmarks.landmark]
            
            # Classify the gesture
            gesture = classify_hand_gesture(hand_landmarks)
            
            # Draw landmarks
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Display the gesture
            cv2.putText(frame, f'Gesture: {gesture}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Rock Paper Scissors Gesture Recognition', frame)
    
    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()