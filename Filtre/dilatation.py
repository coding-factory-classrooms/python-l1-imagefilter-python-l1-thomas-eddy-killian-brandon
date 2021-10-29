import cv2
import numpy

def dilater(img,x):
    f = int(x)
    print("ffvd")

    """
    dilater transforme l'image en la dilatant.
    :param img: str - chemin d'accès vers l'image.
    :return: l'image dilatée.
    """

    try:
        image = cv2.imread(img, 1)
        dst = cv2.dilate(image,numpy.ones((f,f)))

        return dst
    except cv2.error:
        print("Ce n'est pas une image")
    cv2.waitKey(0)
    cv2.destroyAllWindows()