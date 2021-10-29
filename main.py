<<<<<<< HEAD
from Filtre.gray import grey
from Filtre.flou import flou
import sys

args = sys.argv

for i in range(0,len(args)):
    arg = args[i]
    if arg == '--filter':
        if args[i+1] == '-grey':
            grey('/Users/eddymuz/python-l1-imagefilter-python-l1-thomas-eddy-killian-brandon/image/image1.jpeg')
        elif args[i+1] == '-flou':
            flou('/Users/eddymuz/python-l1-imagefilter-python-l1-thomas-eddy-killian-brandon/image/image1.jpeg')
=======
from Filtre.flou import flou
from Filtre.gray import grey
import sys
import os
import cv2
import glob
import numpy
from Filtre.dilatation import dilater

args = sys.argv
dir = os.listdir("image")
strB =args[2].split("|")
tab_arg=[]

'''
On crée une boucle pour séparer chaque filtre de sa valeur avec la fonction split()
puis on ajoute le tableau obtenu dans le tableau tab_arg.
'''

for i in range(0,len(strB)):
    strD = strB[i].split(":")
    tab_arg.append(strD)

''' 
On crée une boucle les arguments pour vérifier si la commande est organisée 
comme --filter "filtre:valeur|filtre"
'''

for i in range(0,len(args)):
    arg = args[i]

    if arg == '--filter':

       # On regarde si il n'y a qu'un seul filtre ajouté.

        if len(tab_arg) == 1:
            for pi in range(0, len(tab_arg)):
                valeur_tab = tab_arg[pi]
                did = valeur_tab[0]

                ''' On regarde si le filtre est : flou, grey ou dilater. '''

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

        ''' On regarde si deux filtres sont ajoutés. '''

        if len(tab_arg) == 2:

            valeur_tab = tab_arg[0]
            valeur_tab2 = tab_arg[1]
            did = valeur_tab[0]
            valeur_tab2.append(did)

            ''' On regarde quel est le filtre qui n'est pas ajouté. '''

            if 'grey' not in valeur_tab2:                       # Filtre flou + dilater
                for ti in range(0, len(dir)):
                    x = valeur_tab[1]
                    dst = flou(f'image/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
                for ti in range(0, len(dir)):
                    x = valeur_tab2[1]
                    dst = dilater(f'image1/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
            if 'flou' not in valeur_tab2:                       # Filtre grey + dilater
                for ti in range(0, len(dir)):
                    dst = grey(f'image/{dir[ti]}')
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
                for ti in range(0, len(dir)):
                    x = valeur_tab[1]
                    dst = dilater(f'image1/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
            if 'dilater' not in valeur_tab2:                    # Filtre grey + flou
                for ti in range(0, len(dir)):
                    dst = grey(f'image/{dir[ti]}')
                    cv2.imwrite(f'image1/{dir[ti]}', dst)
                for ti in range(0, len(dir)):
                    x = valeur_tab[1]
                    dst = flou(f'image1/{dir[ti]}', x)
                    cv2.imwrite(f'image1/{dir[ti]}', dst)

        ''' On regarde si tous les filtres sont ajoutés. '''

        if len(tab_arg) == 3:
            valeur_tab = tab_arg[0]
            valeur_tab2 = tab_arg[1]
            valeur_tab3 = tab_arg[2]
            did = valeur_tab[0]
            didi = valeur_tab2[0]
            valeur_tab3.append(did)
            valeur_tab3.append(didi)
            print(valeur_tab3)

        ''' On regarde si les filtres sont bien : flou, grey et dilater. '''

        if 'dilater' in valeur_tab3 and 'flou' in valeur_tab3 and 'grey' in valeur_tab3:
            for ti in range(0, len(dir)):
                if dir[1] == ".DS_Store":
                    file= glob.glob('image/.DS_Store')
                    for s in file:
                        os.remove(s)

                print(dir)
                dst = grey(f'image/{dir[ti]}')
                cv2.imwrite(f'image1/{dir[ti]}', dst)
            for ti in range(0, len(dir)):
                x = valeur_tab[1]
                dst = flou(f'image1/{dir[ti]}', x)
                cv2.imwrite(f'image1/{dir[ti]}', dst)
            for ti in range(0, len(dir)):
                x = valeur_tab[1]
                dst = dilater(f'image1/{dir[ti]}', x)
                cv2.imwrite(f'image1/{dir[ti]}', dst)




















>>>>>>> 759561c1766eeadb693ac731edaee78fff7f7324

