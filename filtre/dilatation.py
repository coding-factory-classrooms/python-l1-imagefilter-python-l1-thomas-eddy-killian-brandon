import cv2
import numpy

def dilater(img):
    try:
        image = cv2.imread(img, 1)
        dst = cv2.dilate(image,numpy.ones((5,5)), iterations=1)
        cv2.imshow('Dilatation', numpy.hstack((image, dst)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error:
        print("Ce n'est pas une image")