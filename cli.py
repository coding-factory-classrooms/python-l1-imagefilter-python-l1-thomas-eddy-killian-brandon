import filtre.filtres
import filtre.gris
import filtre.flou
import filtre.dilatation

images = ["image/image0.jpeg", "image/image1.jpeg", "image/image2.jpeg"]


def multi_filtre(arg):

    """
    multi_filtre prend en paramètre les filtres choisis.
    :param arg: filtres à utiliser.
    """

    for i in images:
        if arg == "gris":
            filtre.gris.noir_blanc(i)
        elif arg == "flou":
            filtre.flou.floutage(i)
        elif arg == "dilate":
            filtre.dilatation.dilater(i)
        elif arg == "gris|flou":
            filtre.filtres.applique_filtres(i, arg)
        elif arg == "flou|dilate":
            filtre.filtres.applique_filtres(i, arg)
        elif arg == "gris|dilate":
            filtre.filtres.applique_filtres(i, arg)
        elif arg == "gris|flou|dilate":
            filtre.filtres.applique_filtres(i, arg)
