#Takes file passlist and compares it with neural net generated list

#NOTE THAT THIS CODE IS FOR 2 CORES

import sys
from multiprocessing import Process, Value

try:
    open(sys.argv[1], "r").readlines()
    open(sys.argv[2], "r").readlines()
except: 
    sys.exit("(ERROR) Execute with file parameters \"SuccessTesting2Core.py (TestSet).txt (NeuralSet.txt)")
# Description of the process that will be multithreaded
def pass_comparison(subset, collisions):
    outfile = open("Successful.txt","a+")
    for line in open(sys.argv[2], "r"):
        try:
            if line in subset:
                outfile.write(line)
                collisions.value = collisions.value+1
        except:
            print("file has improper encoding or characters that are not in utf8 form and connot be compared")

if __name__ == "__main__":
    

    collisions = Value('i',0) #Shared value for multiprocess

    neurallen = 0
    for line in open(sys.argv[2],"r"):
        neurallen = neurallen+1
    
    passlist = open(sys.argv[1],"r").readlines()
    passlistlen = 0
    for line in open(sys.argv[1],"r"):
        passlistlen = passlistlen + 1

    #splitting text file for each core
    pList1 = passlist[:int(passlistlen/2)]
    pList2 = passlist[int(passlistlen/2)+1:]

    p1 = Process(target=pass_comparison, args = (pList1, collisions))
    p2 = Process(target=pass_comparison, args = (pList2, collisions))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    print("Number of successful attempts: " + str(collisions.value))
    print("Number of passwords not cracked: " + str(passlistlen - collisions.value))
    print("Success rate: " + str(collisions.value/passlistlen*100) + "%")
    print("Neural Net Efficiency (Percentage of passwords cracked vs the length of the generated list): " + str((collisions.value/neurallen)*100)+"%")


    x=input("Press enter to close ...")
