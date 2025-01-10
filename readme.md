# Rock Paper Scissors Gesture Recognition

This project utilizes computer vision to recognize hand gestures for the popular game Rock, Paper, Scissors. Using the MediaPipe library for hand tracking and OpenCV for video capture, the application detects and classifies hand gestures based on the position of the hand landmarks.

## Features

- Real-time hand gesture recognition.
- Detects three common hand gestures for Rock, Paper, Scissors.
- Draws hand landmarks on the video frame for visual feedback.
- Displays the recognized gesture on the screen.
- Uses MediaPipe’s hand tracking solution for accurate hand landmark detection.
  
## Requirements

- Python 3.x (i use 3.9)
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

To install the required dependencies, you can use the following pip commands:

```bash
pip install opencv-python
pip install mediapipe
pip install numpy
```

## Code Breakdown

1. **Setup MediaPipe Hands:**
   - Initializes the MediaPipe Hands solution with detection and tracking confidence thresholds set to 0.7.

2. **Classify Hand Gestures:**
   - The function `classify_hand_gesture()` analyzes the landmarks of the hand to determine if the hand gesture corresponds to:
     - **Rock**: All fingers curled.
     - **Paper**: All fingers extended.
     - **Scissors**: Index and middle fingers extended, others curled.

3. **Video Capture:**
   - The OpenCV `cv2.VideoCapture()` function is used to start video capture from the webcam.
   - Frames are read, flipped horizontally, and processed using MediaPipe to detect hand landmarks.

4. **Gesture Recognition:**
   - The hand landmarks are used to classify the hand gesture (Rock, Paper, or Scissors).
   - A text overlay is displayed on the frame showing the recognized gesture.

5. **Displaying Results:**
   - The hand landmarks are drawn on the video frame, and the classified gesture is displayed at the top-left corner of the screen.
   - The video feed is continuously shown until the user presses 'q' to quit.

## Usage

1. Run the script.
2. Allow the program to access the webcam.
3. Make one of the following hand gestures:
   - **Rock**: Curl all fingers inward.
   - **Paper**: Extend all fingers outward.
   - **Scissors**: Extend the index and middle fingers, curl the others inward.
4. The recognized gesture will be displayed on the screen.

To exit the program, press the `q` key.

## Notes

- The accuracy of gesture recognition depends on the quality of the webcam and lighting conditions.
- The gesture classification works by analyzing the relative vertical positions of finger landmarks, and it might need adjustments for varying hand positions or sizes.
  
## License

This project is open-source and available under the MIT License.