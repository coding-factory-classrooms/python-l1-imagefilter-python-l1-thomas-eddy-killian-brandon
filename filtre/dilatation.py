import cv2
import numpy

def dilater(img):

    """
    dilater transforme l'image en la dilatant.
    :param img: str - chemin d'accès vers l'image.
    :return: l'image dilatée.
    """

    try:
        image = cv2.imread(img, 1)
        dst = cv2.dilate(image,numpy.ones((5,5)), iterations=1)
        cv2.imshow('Dilatation', dst)
        for j in range(3):
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return dst
    except cv2.error:
        print("Ce n'est pas une image")
