from time import sleep
from config import configs

from numpy import zeros
from cv2 import (
  VideoCapture,
  imshow,
  destroyAllWindows,
  waitKey,
  flip,
  putText,
)

from analyser import (
  draw_lips_landmarks,
  classify_mouth_state,
)

cap = VideoCapture(configs["camera_index"])
sleep(1)

prev_frame = zeros(cap.read()[1].shape)

while cap.isOpened():
  ret, frame = cap.read()
  if not ret:
    break

  frame = flip(frame, 1)
  frame = draw_lips_landmarks(frame)
  frame = putText(
    frame,
    classify_mouth_state(frame),
    (50, 250), 0, 10, (0, 0, 0), 2
  )

  imshow("Webcam Feed", frame)
  prev_frame = frame

  if waitKey(1) & 0xFF == 27:
    break

cap.release()
destroyAllWindows()

