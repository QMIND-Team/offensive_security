#Takes file passlist and compares it with neural net generated list
import sys

passlist = open("TestSet.txt","r").readlines()
outfile = open("SuccesfulPasswords.txt", "a+")

collisions = 0 #keep track of successful attempts
progress = 0
progressPercent = 0

passlistlen = 0 #get total number of lines in source list
neurallistlen = 0

for line in open("TestSet.txt","r"):
    passlistlen = passlistlen + 1
for line in open("Neural.txt","r"):
    neurallistlen = neurallistlen + 1

#compare source list to neural generated list
for line in open("Neural.txt", "r"):
    try:
        progress = progress + 1
        if (progress/neurallistlen > progressPercent+0.1):
            progressPercent = progress/neurallistlen
            print(str(round(progressPercent*100)+"%"))
        if line in passlist:
            outfile.write(line)
            collisions = collisions+1
    except:
        print("file has improper encoding or characters that are not in utf8 form and connot be compared")

print("Number of successful attempts: " + str(collisions))
print("Number of passwords not cracked: " + str(passlistlen-collisions))
print("Success rate: " +str(collisions/passlistlen*100) + "%")

x=input("Press enter to close ...")

outfile.close()
