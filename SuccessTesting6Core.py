#Takes file passlist and compares it with neural net generated list

#NOTE THAT THIS CODE IS FOR 6 CORES

import sys
from multiprocessing import Process, Value

try:
    open(sys.argv[1], "r").readlines()
    open(sys.argv[2], "r").readlines()
except: 
    sys.exit("(ERROR) Execute with file parameters \"SuccessTesting6Core.py (TestSet).txt (NeuralSet.txt)")
    

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
    
    neuralLen = 0
    for line in open(sys.argv[2], "r"):
    neuralLen = neuralLen + 1
    
    passlist = open(sys.argv[1],"r").readlines()
    passlistlen = 0
    for line in open(sys.argv[1],"r"):
        passlistlen = passlistlen + 1

    #splitting text file for each core
    pList1 = passlist[:int(passlistlen/6)]
    pList2 = passlist[int(passlistlen/6)+1:int(passlistlen/6)*2]
    pList3 = passlist[int(passlistlen/6)*2+1:int(passlistlen/6)*3]
    pList4 = passlist[int(passlistlen/6)*3+1:int(passlistlen/6)*4]
    pList5 = passlist[int(passlistlen/6)*4+1:int(passlistlen/6)*5]
    pList6 = passlist[int(passlistlen/6)*5+1:]

    p1 = Process(target=pass_comparison, args = (pList1, collisions))
    p2 = Process(target=pass_comparison, args = (pList2, collisions))
    p3 = Process(target=pass_comparison, args = (pList3, collisions))
    p4 = Process(target=pass_comparison, args = (pList4, collisions))
    p5 = Process(target=pass_comparison, args = (pList5, collisions))
    p6 = Process(target=pass_comparison, args = (pList6, collisions))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    
    print("Number of successful attempts: " + str(collisions.value))
    print("Number of passwords not cracked: " + str(passlistlen - collisions.value))
    print("Success rate (Percentage of passwords cracked): " + str(collisions.value/passlistlen*100) + "%")
    print("Neural set efficiency (Number of working passwords vs set length): " + str(collisions.value/neuralLen*100)+"%")

    x=input("Press enter to close ...")
