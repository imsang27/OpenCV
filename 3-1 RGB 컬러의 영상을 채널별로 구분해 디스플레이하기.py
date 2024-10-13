import cv2 as cv
import sys

img = cv.imread("ch02_soccer.jpg")

if img is None:
  sys.exit("파일을 찾을 수 없습니다.")

cv.imshow("Original RGB", img)
cv.imshow("Upper left half", img[0:img.shape[0] // 2, 0:img.shape[1] // 2, :])
cv.imshow("Center half", img[img.shape[0] // 4:3*img.shape[0] // 4, img.shape[1] // 4:3^img.shape[1] // 4, :])

cv.imshow('R Channel', img[:,:,2])
cv.imshow('G Channel', img[:,:,1])
cv.imshow('B Channel', img[:,:,0])

cv.waitkey()
cv.destroyAllWindows()