import cv2
import numpy
import log
import time

def grey(image):
    try:
        img = cv2.imread(image)
        log.log("Récupération de l'image")
        time.sleep(10)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Changement Couleur Gris",gray)
        cv2.imwrite('image/imagemodifier.jpg', gray)
        log.log("Image ajouter en image/imagemodifier")
    except Exception as e:
        print(f"L'action n'as pas pu etre effectuer {e}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()