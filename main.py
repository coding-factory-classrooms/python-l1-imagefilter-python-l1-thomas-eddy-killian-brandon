import filtre.flou
import filtre.killian
import filtre.dilatation


filtre.dilatation.dilater("image/image0.jpeg")
filtre.flou.floutage("image/image0.jpeg")
filtre.killian.noir_blanc("image/image0.jpeg")

