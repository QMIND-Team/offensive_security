from Model import Model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


epochLimit = 10
trainingSet = open('./5k2.txt','r').readlines() #Initial Training Set
passwords = open("./5k.txt", 'r').readlines() #We will try and generate as many of these as possible
crackedList = []

m = Model("DemoModel", "./5k2.txt")
m.prepTrainingSet()

#Initial Train
print("Initial Training to 50 Epochs starting...")
m.buildModel(50)


#Continuously retrain model and attack until no more passwords remain
while len(passwords) > 0:
    print("Passwords Uncracked = " + str(len(passwords)))
    print("Passwords Cracked = " + str(len(crackedList)))

    #Prepare trainingset
    m.prepTrainingSet()
    
    #Empty the attackSet
    attackSet = []

    #Build and save the model
    m.model.save(m.name + '.h5')
    print("Model Saved")

    #Generate 10000 passwords to use for attacking
    for i in range(0, 10000):
        attackSet.append(str(m.make_name()))
    print("Attack Set created")

    #Perform attack
    for p in passwords:
        if p in attackSet:
            print("Cracked password: " + p)
            passwords.remove(p) #Remove cracked Password from the password list
            crackedList.append(p)   #Add password to the list of cracks
            #Add cracked password to the training set for retraining
            with open('./5k2.txt', 'a') as f:  
                f.write("\n")
                f.write(p)
    
    m.continueTraining(epochLimit)
    
        



