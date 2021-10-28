import filtre.flou
import filtre.gris
import filtre.dilatation

filtre.dilatation.dilater("image/image1.jpeg")
filtre.flou.floutage("image/image1.jpeg")
filtre.gris.noir_blanc("image/image1.jpeg")

