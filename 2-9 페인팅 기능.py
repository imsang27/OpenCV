import cv2 as cv
import sys

img = cv.imread('ch02_soccor.jpg')

if img is None:
  sys.exit('파일을 찾을 수 없습니다.')

BrushSize = 5
LColor, RColor = (255, 0, 0), (0, 0, 255)

def paintimg(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONUP:
    cv.circle(img, (x, y), BrushSize, LColor, RColor, -1)
  elif event == cv.EVENT_RBUTTONUP:
    cv.circle(img, (x, y), BrushSize, LColor, RColor, -1)
  elif event == cv.EVENT_MOUSEMOVE and cv.EVENT_FLAG_LBUTTON:
    cv.circle(img, (x, y), BrushSize, LColor, RColor, -1)
  elif event == cv.EVENT_MOUSEMOVE and cv.EVENT_FLAG_RBUTTON:
    cv.circle(img, (x, y), BrushSize, LColor, RColor, -1)

  cv.imshow('Paintong', img)

cv.namedWindow('Paintong')
cv.imshow('Paintong', img)

cv.setMouseCallback('Paintong', paintimg)

while True:
  if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    break