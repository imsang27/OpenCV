import cv2 as cv
import numpy as np

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        # 지정된 영역 잘라내기
        roi = img[iy:y, ix:x]
        # 보간 적용 (원하는 보간 방법 선택)
        resized_roi = cv.resize(roi, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
        # 원본 이미지에 보간된 영역 붙여넣기
        img[iy:y, ix:x] = resized_roi
        cv.imshow('Image', img)

img = cv.imread('rose.png')

drawing = False
ix, iy = -1, -1

cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_rectangle)

while True:
    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()