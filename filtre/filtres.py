import cv2
import numpy

def applique_filtres(img, arg):

    """
    applique_filtres transforme l'image choisie en fonction des filtres choisis.
    :param img: str - image à transformer.
    :param arg: str - arguments pour filtrer l'image.
    :return: une image filtrée.
    """

    try:
        image = cv2.imread(img)
    except cv2.error:
        print("Ce n'est pas une image")
    if arg == "gris|flou":
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray image', gris)
        flou = cv2.GaussianBlur("".join(gris), (41, 41), 41)
        cv2.imshow('Gaussian Smoothing', flou)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if arg == "flou|dilate":
        flou = cv2.GaussianBlur(image,(41,41),41)
        cv2.imshow('Gaussian Smoothing', flou)
        dilate = cv2.dilate("".join(flou), numpy.ones((5, 5)), iterations=1)
        cv2.imshow('Dilatation', dilate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if arg == "gris|dilate":
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray image', gris)
        dilate = cv2.dilate("".join(gris),numpy.ones((5,5)), iterations=1)
        cv2.imshow('Dilatation', dilate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if arg == "gris|flou|dilate":
        gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray image', gris)
        flou = cv2.GaussianBlur("".join(gris), (41, 41), 41)
        cv2.imshow('Gaussian Smoothing', flou)
        dilate = cv2.dilate("".join(flou), numpy.ones((5, 5)), iterations=1)
        cv2.imshow('Dilatation', dilate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image