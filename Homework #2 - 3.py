import cv2 as cv
import numpy as np

img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize = (0, 0), fx = 0.4, fy = 0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray, 'soccer', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv.imshow('Original', gray)

# 가우시안 스무딩
smooth = np.hstack((cv.GaussianBlur(gray, (5, 5), 0.0),
                    cv.GaussianBlur(gray, (9, 9), 0.0),
                    cv. GaussianBlur(gray, (15, 15), 0.0)))
cv.imshow('Smooth', smooth)

femboss = np.array([[-1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0]])

# 메디안 스무딩
median = np.hstack((cv.medianBlur(gray, 5),
                     cv.medianBlur(gray, 9),
                     cv.medianBlur(gray, 15)))

gray16 = np.int16(gray)
emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss)+ 128, 0, 255))
emboss_bad = np.uint8(cv.filter2D(gray16, -1, femboss)+ 128)
emboss_worse = cv.filter2D(gray, -1, femboss)

cv.imshow('Emboss', emboss)
cv.imshow('Emboss_bad', emboss_bad)
cv.imshow('Emboss_worse', emboss_worse)
cv.imshow('Median', median)

cv.waitKey()
cv.destroyAllWindows()