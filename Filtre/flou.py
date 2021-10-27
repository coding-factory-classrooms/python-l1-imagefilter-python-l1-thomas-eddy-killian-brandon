import cv2
import numpy

def grey(image):
    try:
        img = cv2.imread(image)

        gre= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gaussian Smoothing",numpy.hstack((gre, gray)))
    except Exception as e:
        print(f"L'action n'as pas pu etre effectuer {e}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


