from Filtre.flou import flou
from Filtre.grey import grey
import cv2
import sys
import log

args = sys.argv

for i in range(0,len(args)):
    arg = args[i]
    if arg == '--filter':
        if args[i+1] == '-grey':
            grey('image/image1.jpg')

        elif args[i+1] == '-flou':
            flou('image/image1.jpg')
    elif arg == '--clear':
        log.clear_log()

