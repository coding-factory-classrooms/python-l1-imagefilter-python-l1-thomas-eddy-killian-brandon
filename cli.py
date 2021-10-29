import filtre.gris
import filtre.flou
import filtre.dilatation
import cv2

images = ["image/image0.jpg", "image/image1.jpg", "image/image2.jpg"]
filtre_image = []


def multi_filtre(arg):

    """
    multi_filtre prend en paramètre les filtres choisis.
    :param arg: filtres à utiliser.
    """
    j = 0
    for i in images:
        if arg == "gris":
            dst = filtre.gris.noir_blanc(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "flou":
            dst = filtre.flou.floutage(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "dilate":
            dst = filtre.dilatation.dilater(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "gris|flou":
            dst = filtre.gris.noir_blanc(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "flou|dilate":
            dst = filtre.flou.floutage(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "gris|dilate":
            dst = filtre.gris.noir_blanc(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "gris|flou|dilate":
            dst = filtre.gris.noir_blanc(i)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
    for k in filtre_image:
        if arg == "gris|flou":
            dst = filtre.gris.noir_blanc(k)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "flou|dilate":
            dst = filtre.flou.floutage(k)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "gris|dilate":
            dst = filtre.gris.noir_blanc(k)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
        elif arg == "gris|flou|dilate":
            dst = filtre.gris.noir_blanc(k)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
    for l in filtre_image:
        if arg == "gris|flou|dilate":
            dst = filtre.gris.noir_blanc(l)
            cv2.imwrite('filtre_image/imagemodifier' + str(j) + '.jpg', dst)
            filtre_image.append('filtre_image/imagemodifier' + str(j) + '.jpg')
    j += 1
