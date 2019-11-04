#This is a Script Written by Alastair Lewis to show how a simple brute force password crack works.
#It only takes in strings of length 4 because the time taken to crack passwords much longer quickly
#becomes impractical, emphasising the need for a better approach such as a wordlist/dictionary attack
import sys
import time
import hashlib
import os

def main():
    #Creating the hashing object
    m = hashlib.md5()

    #Start Hashing with Enter
    password_to_crack = input("Press Enter a four character password to crack: ")
    m.update(password_to_crack.encode('utf-8'))
    print("Attempting to Crack: " + str(m.digest()))
    time.sleep(3)

    #Four Loops to iterate through all combinations
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                for d in range(97, 123):
                    attempt = str(chr(a) + chr(b) + chr(c) + chr(d))  #Creating the string to attempt
                    #print("Attempting: " + attempt)
                    n = hashlib.md5() #Hashing the String
                    n.update(attempt.encode('utf-8'))
                    if m.digest() == n.digest(): #Checking if strings match
                        print("Password was: " + attempt)
                        return
    print("Password couldn't be Cracked") #Sad message

main()
