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

