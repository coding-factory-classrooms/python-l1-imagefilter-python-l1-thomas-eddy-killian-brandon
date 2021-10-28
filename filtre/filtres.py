import cv2
import numpy

def applique_filtres(img):
    try:
        image = cv2.imread(img)
    except cv2.error:
        print("Ce n'est pas une image")

    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image = gris

    flou = cv2.GaussianBlur(image,(41,41),41)
    cv2.imshow('Gaussian Smoothing', numpy.hstack((image, flou)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image = flou

    dst = cv2.dilate(image,numpy.ones((5,5)), iterations=1)
    cv2.imshow('Dilatation', numpy.hstack((image, dst)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image = dst

    return image