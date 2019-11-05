import hashlib
import sys


f = open(sys.argv[1], "r", errors='ignore')
z = open("output.txt","a+")

for x in f:
    y = x.rstrip("\n\r")
    hashthing = hashlib.md5(y.encode())

    try:
        z.write(y+":"+str(hashthing.hexdigest()) + "\n")
    except:
        print("idk something fucked up")

f.close()
