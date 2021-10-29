from Filtre.flou import flou
from Filtre.gray import grey
import sys
import os
import cv2
import numpy
from Filtre.dilatation import dilater

args = sys.argv
dir = os.listdir("image")
strB =args[2].split("|")
tab_arg=[]

for i in range(0,len(strB)):
    strD = strB[i].split(":")
    tab_arg.append(strD)


for i in range(0,len(args)):
    arg = args[i]

    if arg == '--filter':
        if len(tab_arg) == 1:
            for pi in range(0, len(tab_arg)):
                valeur_tab = tab_arg[pi]
                did = valeur_tab[0]
                if did == 'flou':
                    for ti in range(0, len(dir)):
                        x = valeur_tab[1]
                        dst =flou(f'image/{dir[ti]}', x)
                        cv2.imwrite(f'image1/{dir[ti]}', dst)
                elif did == 'grey':
                    for ti in range(0, len(dir)):
                        dst =grey(f'image/{dir[ti]}')
                        cv2.imwrite(f'image1/{dir[ti]}', dst)
                elif did == 'dilater':
                    for ti in range(0, len(dir)):
                        x = valeur_tab[1]
                        dst = dilater(f'image/{dir[ti]}', x)
                        cv2.imwrite(f'image1/{dir[ti]}', dst)

        if len(tab_arg) == 2:

            valeur_tab = tab_arg[0]
            valeur_tab2 = tab_arg[1]
            did = valeur_tab[0]
            valeur_tab2.append(did)

            if 'grey' not in valeur_tab2:
                for ti in range(0, len(dir)):
                    x = valeur_tab[1]
                    dst = flou(f'image/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
                for ti in range(0, len(dir)):
                    x = valeur_tab2[1]
                    dst = dilater(f'image1/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
            if 'flou' not in valeur_tab2:
                for ti in range(0, len(dir)):
                    dst = grey(f'image/{dir[ti]}')
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
                for ti in range(0, len(dir)):
                    x = valeur_tab[1]
                    dst = dilater(f'image1/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
            if 'dilater' not in valeur_tab2:
                for ti in range(0, len(dir)):
                    dst = grey(f'image/{dir[ti]}')
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
                for ti in range(0, len(dir)):
                    x = valeur_tab[1]
                    dst = flou(f'image1/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)





















