# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:59:42 2020

@author: Lewis Hillard

"""

import numpy as np

class Model:
    char_to_index = dict((chr(i+31),i) for i in range(0,97))  # Creating an array of all characters that can be used with corresponding index value
    index_to_char =  dict((i, chr(i+31)) for i in range(0,97)) # Reverse of the previous
    
    
    def __init__(self, modelName, fileName):
        self.name = modelName
        self.passes = open(fileName, 'r').readlines()  # Used as temporary storage for the file so that line endings can be removed
        
    def prepTrainingSet(self, addedText = []):
        for i in addedText:
            self.passes.append(i)
        
        print(len(self.passes))
        
        self.full_list = [0]*len(self.passes) #creating a new list for stripped passwords
        
        p = 0
        for i in self.passes:
            self.full_list[p] = i.rstrip("\n\r") + " " # Remove line endings and add a space to indicate end of line
            p=p+1
        
        
        self.max_char = len(max(self.full_list, key=len))
        m = len(self.full_list)
        self.char_dim = len(Model.char_to_index)
        
        self.X = np.zeros((m,self.max_char, self.char_dim)) # 3D array for storing one hot encoded characters
        self.Y = np.zeros((m,self.max_char, self.char_dim))
        
        for i in range(m):          # One hot encoding
            password = list(self.full_list[i])
            for j in range(len(password)):
                self.X[i,j, Model.char_to_index[password[j]]] = 1
                if j < len(password)-1:
                    self.Y[i,j, Model.char_to_index[password[j+1]]] = 1
        
    def buildModel(self, epochLimit):
        from keras.models import Sequential
        from keras.layers import LSTM, Dense
        from keras.callbacks import LambdaCallback
        
        
        self.model = Sequential()
        self.model.add(LSTM(256, input_shape=(self.max_char, self.char_dim), return_sequences=True))
        self.model.add(Dense(self.char_dim, activation='softmax'))
        
        self.model.compile(loss='categorical_crossentropy', optimizer='adam')
        
        self.name_generator = LambdaCallback(on_epoch_end = self.generate_name_loop)
        
        self.model.fit(self.X, self.Y, batch_size=512, epochs=epochLimit, callbacks=[self.name_generator], verbose=0)
            
            
    def continueTraining(self, epochLimit):
        from keras.models import load_model
        self.model = load_model(self.name+'.h5')
        self.model.fit(self.X, self.Y, batch_size=512, epochs=epochLimit, callbacks=[self.name_generator], verbose=0)


    def make_name(self): # Create the name
        name = []
        x = np.zeros((1, self.max_char, self.char_dim))
        end = False
        i = 0
        
        while end==False:
            probs = list(self.model.predict(x)[0,i])
            probs = probs / np.sum(probs)
            
            index = np.random.choice(range(self.char_dim), p=probs) # Picks a random character based off of its probability
            while i<5 and index == 1:
                index = np.random.choice(range(self.char_dim), p=probs)
                
            if i == self.max_char-2:
                character = ' '
                end = True
            else:
                character = Model.index_to_char[index]
            name.append(character)
            x[0, i+1, index] = 1
            i += 1
            if character == ' ':
                end = True
        
        return(''.join(name))
    

    def generate_name_loop(self, epoch, _):
        
        print("Epoch Completed: ", epoch)
        if epoch % 10 == 0:
            
            print('Names generated after epoch %d:' % epoch)
    
            for i in range(3):
                p = str(self.make_name())
                print(p)
            
            
        


    def generateTextFile(self, outputLength):
        temp = open("GenOutput.txt", "a+")
        for i in range(outputLength):
            x = str(self.make_name())
            temp.write(x + "\n")
            #print(x)
        temp.close();