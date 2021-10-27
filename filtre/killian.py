import cv2

def noir_blanc(img):
    image = cv2.imread(img)
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Gray image', gris)

    cv2.waitKey(0)
    cv2.destroyAllWindows()