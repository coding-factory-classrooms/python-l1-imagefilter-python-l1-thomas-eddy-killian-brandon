import filtre.filtres
import filtre.gris, filtre.flou, filtre.dilatation

images = ["image/image0.jpeg", "image/image1.jpeg", "image/image2.jpeg"]

def f(arg):
    for i in images:
        if arg == "gris":
            filtre.gris.noir_blanc(i)
        elif arg == "flou":
            filtre.flou.floutage(i)
        elif arg == "dilate":
            filtre.dilatation.dilater(i)
        elif arg == "gris|flou":
            filtre.filtres.applique_filtres(i, "gris", "flou")
        elif arg == "flou|dilate":
            filtre.filtres.applique_filtres(i, "flou", "dilate")
        elif arg == "gris|dilate":
            filtre.filtres.applique_filtres(i, "gris", "dilate")
        elif arg == "gris|flou|dilate":
            filtre.filtres.applique_filtres(i, "gris", "flou", "dilate")

