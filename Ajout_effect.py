import log
from Filtre.flou import flou
from Filtre.gray import grey
from Filtre.dilatation import dilater
import sys
import os
import cv2
import numpy
import glob


args = sys.argv
dir = os.listdir("image")

files = glob.glob('image/*.jpeg')

def system_architecture():
    print("Bienvenue, Nous allons prendre vos photos et appliquez vos filtres")

    for i in range(0,len(args)):
        arg = args[i]

        if arg == '--filter':
            strB = args[2].split("|")
            tab_arg = []

            for i in range(0, len(strB)):
                strD = strB[i].split(":")
                tab_arg.append(strD)
            if len(tab_arg) == 1:
                for pi in range(0, len(tab_arg)):
                    valeur_tab = tab_arg[pi]
                    did = valeur_tab[0]
                    if did == 'flou':
                        for ti in range(0, len(files)):
                            x = valeur_tab[1]
                            dst =flou(f'{files[ti]}', x)
                            cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    elif did == 'grey':
                        for ti in range(0, len(files)):

                            dst =grey(f'{files[ti]}')
                            cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    elif did == 'dilater':
                        for ti in range(0, len(files)):
                            x = valeur_tab[1]
                            dst = dilater(f'{files[ti]}', x)
                            cv2.imwrite(f'image1/image{ti}.jpeg', dst)

            if len(tab_arg) == 2:

                valeur_tab = tab_arg[0]
                valeur_tab2 = tab_arg[1]
                did = valeur_tab[0]
                valeur_tab2.append(did)

                if 'grey' not in valeur_tab2:
                    for ti in range(0, len(files)):
                        x = valeur_tab[1]
                        dst = flou(f'{files[ti]}', x)
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    for ti in range(0, len(files)):
                        x = valeur_tab2[1]
                        dst = dilater(f'image1/image{ti}.jpeg', x)
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                if 'flou' not in valeur_tab2:
                    for ti in range(0, len(files)):
                        dst = grey(f'{files[ti]}')
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    for ti in range(0, len(files)):
                        x = valeur_tab[1]
                        dst = dilater(f'image1/image{ti}.jpeg', x)
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                if 'dilater' not in valeur_tab2:
                    for ti in range(0, len(files)):
                        dst = grey(f'{files[ti]}')
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    for ti in range(0, len(files)):
                        x = valeur_tab[1]
                        dst = flou(f'image1/image{ti}.jpeg', x)
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)

            if len(tab_arg) == 3:
                valeur_tab = tab_arg[0]
                valeur_tab2 = tab_arg[1]
                valeur_tab3 = tab_arg[2]
                did = valeur_tab[0]
                didi = valeur_tab2[0]
                valeur_tab3.append(did)
                valeur_tab3.append(didi)


                if 'dilater' in valeur_tab3 and 'flou' in valeur_tab3 and 'grey' in valeur_tab3:
                    for ti in range(0, len(files)):

                        dst = grey(f'{files[ti]}')
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    for ti in range(0, len(files)):
                        x = valeur_tab[1]
                        dst = flou(f'image1/image{ti}.jpeg', x)
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)
                    for ti in range(0, len(files)):
                        x = valeur_tab[1]
                        dst = dilater(f'image1/image{ti}.jpeg', x)
                        cv2.imwrite(f'image1/image{ti}.jpeg', dst)







def loging_system():

    for y in range(0, len(args)):
        arg = args[y]

        if arg == '--clear':
            log.clear_log()
        if arg == '--suppfile':
            try:
                files = glob.glob('image1/*.jpeg')
                for f in files:
                    os.remove(f)
                    print("Suppression des anciennes images.")
            except Exception as e:
                print(f"Impossible de supprimer le fichier car il n'existe pas {e}")
        if arg == '--ini':
            os.system('python main.py --filter "-flou:19|dilater:19|grey"')


system_architecture()
loging_system()