import cv2

for i in range(0, 2):
    image = cv2.imread("image0.jpeg")
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gris)

    cv2.waitKey(0)
    cv2.destroyAllWindows()