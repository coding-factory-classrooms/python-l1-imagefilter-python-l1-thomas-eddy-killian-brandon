import cv2
import log
import numpy

def grey(image):
    try:
        img = cv2.imread(image)



        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(f"Couleur appliquer")
        return gray
    except Exception as e:
        print(f"L'action n'as pas pu etre effectuer {e}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


