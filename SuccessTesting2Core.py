#Takes file passlist and compares it with neural net generated list

#NOTE THAT THIS CODE IS FOR 2 CORES

from multiprocessing import Process, Value

# Description of the process that will be multithreaded
def pass_comparison(subset, collisions):
    outfile = open("Successful.txt","a+")
    for line in open("Neural.txt", "r"):
        try:
            if line in subset:
                outfile.write(line)
                collisions.value = collisions.value+1
        except:
            print("file has improper encoding or characters that are not in utf8 form and connot be compared")

if __name__ == "__main__":
    

    collisions = Value('i',0) #Shared value for multiprocess
    
    passlist = open("TestSet.txt","r").readlines()
    passlistlen = 0
    for line in open("TestSet.txt","r"):
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

    x=input("Press enter to close ...")
