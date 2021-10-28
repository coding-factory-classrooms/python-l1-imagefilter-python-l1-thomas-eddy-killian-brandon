from Filtre.flou import flou
from Filtre.gray import grey
import sys
import os

args = sys.argv
dir = os.listdir("image")

print(args)

strA = "".join(args[2])
strB = strA.split(":")




for i in range(0,len(args)):
    arg = args[i]
    if arg == '--filter':
        if strB[0] == '-grey':
            for i in range(0,len(dir)):
                grey(f'image/{dir[i]}')
        elif strB[0] == '-flou':
            for i in range(0, len(dir)):
                x = strB[1]
                flou(f'image/{dir[i]}',x)













