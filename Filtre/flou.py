import cv2
import log
import numpy



def flou(image,x):
    f = int(x)
    print(f"Flou appliquer")
    try:
        img = cv2.imread(image)
        dst = cv2.GaussianBlur(img,(f,f),f)

        return dst
    except Exception as e:
        print(f"L'image n'as pas pu etre effectuer{e}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

