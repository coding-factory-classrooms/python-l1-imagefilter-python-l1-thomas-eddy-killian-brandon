import cv2
import numpy


def floutage(image):
    try:
        img = cv2.imread(image)
        dst = cv2.GaussianBlur(img,(51,51),51)
        cv2.imshow("Image Flouter",numpy.hstack((img, dst)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return dst
    except Exception as e:
        print(f"L'image n'as pas pu etre effectuer{e}")