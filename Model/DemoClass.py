from Model import Model
from keras.models import load_model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


epochLimit = 10
trainingSet = open('./5k2.txt','r').readlines() #Initial Training Set
passwords = open("./5k.txt", 'r').readlines() #We will try and generate as many of these as possible
crackedList = []

m = Model("DemoModel", "./5k2.txt")
m.prepTrainingSet()

#Initial Train
print("Loading Prepared Model...")
m.buildModel(0, 0)
m.model = load_model("../TestModel.h5")
print("Model Successfully Loaded")


#Continuously retrain model and attack until no more passwords remain
while len(passwords) > 0:
    print("Passwords Uncracked = " + str(len(passwords)))
    print("Passwords Cracked = " + str(len(crackedList)))

    #Prepare trainingset
    m.prepTrainingSet()
    print("## Training Set Prepared ##")

    #Continue Training Model
    print("## Training Model ##")
    m.continueTraining(epochLimit)

    #Empty the attackSet
    attackSet = []

    #Generate 1000 passwords to use for attacking
    for i in range(0, 1000):
        attackSet.append(str(m.make_name(0)))
    print("## Attack Set created ##")

    #Perform attack
    print("## Attacking Passwords ##")
    m.attackList(passwords, crackedList)
