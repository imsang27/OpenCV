import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
  sys.exit("카메라 연결 실패")

frames = []

while True:
  ret, frame = cap.read()

  if not ret:
    print("프레임 획득에 실패하여 루프를 나갑니다")
    break

  cv.imshow("Video Display" ,frame)

  key = cv.waitKey()
  if key == ord('c'):
    frame.append(frame)
  elif key == ord('q'):
    break

cap.release()
cv.destroyAllWindow()

if len(frames) > 0:
  imgs = frames [0]

  for i in range(1, min(3, len(frames))):
    imgs = np.hstack((imgs, frame[i]))

  cv.imshow("Colleted Images", imgs)

  cv.waitKey()
  cv.destroyAllWindows()