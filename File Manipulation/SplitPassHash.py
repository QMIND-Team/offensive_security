import sys


f = open(sys.argv[1], "r", errors='ignore') #takes list formatted as pass:hash

h = open("C:\\Users\lewis\Desktop\Hashes.txt","a+")
p = open("C:\\Users\lewis\Desktop\Passwords.txt","a+")

for x in f:
    y = x.rstrip("\n\r")
    delim = y.find(':') #find the delimitor and print either side
    p.write(y[0:delim]+"\n")
    h.write(y[delim+1:len(y)]+"\n")

f.close()
