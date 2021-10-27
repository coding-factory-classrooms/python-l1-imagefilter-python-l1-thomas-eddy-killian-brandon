import cv2
import numpy

image = cv2.imread("image/image0.jpeg")
dst = cv2.GaussianBlur(image,(51,51),51)
cv2.imshow('Original image', image)
cv2.imshow('Gray image', numpy.hstack((image, dst)))

cv2.waitKey(0)
cv2.destroyAllWindows()