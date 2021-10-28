import cv2
import numpy

def applique_filtres(img, arg1, arg2, arg3 = "none"):
    try:
        image = cv2.imread(img)
    except cv2.error:
        print("Ce n'est pas une image")
    if arg1 == "gris":
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray image', gris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if arg1 == "flou" or arg2 == "flou":
        flou = cv2.GaussianBlur(image,(41,41),41)
        cv2.imshow('Gaussian Smoothing', flou)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if arg2 == "dilate" or arg3 == "dilate":
        dilate = cv2.dilate(image,numpy.ones((5,5)), iterations=1)
        cv2.imshow('Dilatation', dilate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image