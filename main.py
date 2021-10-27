from Filtre.flou import flou
from Filtre.gray import grey
import sys

args = sys.argv

for i in range(0,len(args)):
    arg = args[i]
    if arg == '--filter':
        if args[i+1] == '-grey':
            grey('image/image1.jpeg')
        elif args[i+1] == '-flou':
            flou('image/image1.jpeg')

