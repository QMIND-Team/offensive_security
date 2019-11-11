#Takes file passlist and compares it with neural net generated list
import sys

passlist = open("testfile.txt","r")
outfile = open("SuccesfulPasswords.txt", "a+")

collisions = 0 #keep track of successful attempts

passlistlen = 0 #get total number of lines in source list
for line in open("testfile.txt","r"):
    passlistlen = passlistlen + 1

#compare source list to neural generated list
for line in open("compare.txt", "r"):
    try:
        if line in passlist:
            outfile.write(line)
            collisions = collisions+1
    except:
        print("file has improper encoding or characters that are not in utf8 form and connot be compared")
        break

print("Number of successful attempts: " + str(collisions))
print("Number of passwords not cracked: " + str(passlistlen-collisions))
print("Success rate: " +str(collisions/passlistlen*100) + "%")

x=input("Press enter to close ...")

outfile.close()
