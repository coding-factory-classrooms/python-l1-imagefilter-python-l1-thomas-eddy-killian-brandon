import cv2
import numpy

def floutage(img):
    try:
        image = cv2.imread(img)
        dst = cv2.GaussianBlur(image,(101,101),101)
        cv2.imshow('Gaussian Smoothing', numpy.hstack((image, dst)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error:
        print("Ce n'est pas une image")