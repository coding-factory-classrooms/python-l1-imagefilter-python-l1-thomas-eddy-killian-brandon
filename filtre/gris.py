import cv2

def noir_blanc(img):

    """
    noir_blanc transforme une image en couleur en image en noir et blanc.
    :param img: str - chemin d'accès vers l'image.
    :return: l'image en noir et blanc.
    """

    try:
        image = cv2.imread(img)
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray image', gris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return gris
    except cv2.error:
        print("Ce n'est pas une image")