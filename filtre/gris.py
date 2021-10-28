import cv2
import numpy
import log
import time

def noir_blanc(img):

    """
    noir_blanc transforme une image en couleur en image en noir et blanc.
    :param img: str - chemin d'accès vers l'image.
    :return: l'image en noir et blanc.
    """

    try:
        image = cv2.imread(img)
        log.log("Récupération de l'image")
        time.sleep(10)
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Changement Couleur Gris', gris)
        for j in range(3):
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', gris)
        log.log("Image ajouter en filtre_image/imagemodifier")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return gris
    except Exception as e:
        print(f"L'action n'as pas pu etre effectuer {e}")
