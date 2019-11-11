import hashlib
import sys


f = open(sys.argv[1], "r", errors='ignore') #Dragged file gets taken as input
z = open("output.txt","a+")

for x in f:
    y = x.rstrip("\n\r") #remove new line and return characters so they don't get hashed as well
    hashthing = hashlib.md5(y.encode())

    try:
        z.write(y+":"+str(hashthing.hexdigest()) + "\n") #print original password and hash. Add back on new line character
    except:
        print("Issue with line encoding, skip to next line")

f.close()
