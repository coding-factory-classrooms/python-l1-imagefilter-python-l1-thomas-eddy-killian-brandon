import os

dir = os.listdir(os.getcwd())
dir.sort()

for file in dir:
   print (file)