import cv2
import numpy

def floutage(img):

    """
    floutage sert à  flouter les images.
    :param img: str - chemin d'accès à l'image.
    :return: l'image floutée.
    """
    try:
        image = cv2.imread(img)
        dst = cv2.GaussianBlur(image,(41,41),41)
        cv2.imshow('Gaussian Smoothing', numpy.hstack((image, dst)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return dst
    except cv2.error:
        print("Ce n'est pas une image")