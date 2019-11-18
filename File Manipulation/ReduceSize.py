# This script removes passwords that are longer than 20 characters or shorter than 4 characters

import sys

f = open(sys.argv[1], "r", errors='ignore')

h = open("Minimized.txt","a+")

for x in f:
    if (len(x)<59 and len(x)>37):
        h.write(x)

f.close()
