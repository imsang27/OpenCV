import cv2 as cv
import sys

img = cv.imread("soccer.jpg")
t, bin_img = cv.threshold(img[:,:,2], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

cv.imshow('R Channel', img[:, :, 2])
cv.imshow('R Channel bainerization', bin_img)

cv.waitKey()
cv.destroyAllWindows()