from Filtre.flou import flou
from Filtre.gray import grey
import sys
import os

args = sys.argv
dir = os.listdir("image")




strB =args[2].split("|")
tab_arg = []

for i in range(0, len(strB)):
    strD = strB[i].split(":")
    tab_arg.append(strD)

for i in range(0, len(args)):
    arg = args[i]

    if arg == '--filter':

        for pi in range(0, len(tab_arg)):
            valeur_tab = tab_arg[pi]
            did = valeur_tab[0]
            if did == '-flou':
                for ti in range(0, len(dir)):
                    print('tt')
                    x = valeur_tab[1]
                    flou(f'image/{dir[ti]}', x)
            elif did == 'grey':
                for ti in range(0, len(dir)):
                    grey(f'image/{dir[ti]}')

