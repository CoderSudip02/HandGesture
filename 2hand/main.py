import cv2
import mediapipe as mp
from tensorflow.keras.models import load_model
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils





# Load the gesture recognizer model
qmodel = load_model("mp_hand_gesture")

# Load class names
f = open('gesture.names', 'r')
lables = f.read().split('\n')
f.close()
print(lables)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)

    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                landmarks.append([lmx, lmy])

    # Drawing landmarks on frames
    mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

# For webcam input:
cap = cv2.VideoCapture(0)
with mpHands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
      _, frame = cap.read()
      x, y, z = frame.shape

      # Flip the frame vertically
      frame = cv2.flip(frame, 1)
      framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      # Get hand landmark prediction
      result = hands.process(framergb)

      # print(result)

      className = ''

      # post process the result
      if result.multi_hand_landmarks:
          landmarks = []
          for handslms in result.multi_hand_landmarks:
              for lm in handslms.landmark:
                  # print(id, lm)
                  lmx = int(lm.x * x)
                  lmy = int(lm.y * y)
                  landmarks.append([lmx, lmy])

              # Drawing landmarks on frames
              mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

              # Predict gesture
              prediction = model.predict([landmarks])
              # print(prediction)
              classID = np.argmax(prediction)
              className = lables[classID].capitalize()

      # show the prediction on the frame
      cv2.putText(frame, className, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

      # Show the final output
      cv2.imshow("Output", frame)
      if cv2.waitKey(1) == ord('q'):
       break
cap.release()