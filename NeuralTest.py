# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:33:37 2019

@author: lewis
"""

import numpy as np

passes = open("test.txt", 'r').readlines()  # Used as temporary storage for the file so that line endings can be removed

full_list = [0]*len(passes) #creating a new list for stripped passwords
p = 0

for i in passes:
    full_list[p] = i.rstrip("\n\r") + " " # Remove line endings and add a space to indicate end of line
    p=p+1

char_to_index = dict((chr(i+31),i) for i in range(1,96))  # Creating an array of all characters that can be used with corresponding index value

index_to_char =  dict((i, chr(i+31)) for i in range(1,96)) # Reverse of the previous

#### The next section is used for one hot encoding so that the neural net can make prediction
max_char = len(max(full_list, key=len))
m = len(full_list)
char_dim = len(char_to_index)

X = np.zeros((m,max_char, char_dim)) # 3D array for storing one hot encoded characters
Y = np.zeros((m,max_char, char_dim))

for i in range(m):          # One hot encoding
    password = list(full_list[i])
    for j in range(len(password)):
        X[i,j, char_to_index[password[j]]] = 1
        if j < len(password)-1:
            Y[i,j, char_to_index[password[j+1]]] = 1

#### Neural Model ####  
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import LambdaCallback

model = Sequential()
model.add(LSTM(128, input_shape=(max_char, char_dim), return_sequences=True))
model.add(Dense(char_dim, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

def make_name(model): # Create the name
    name = []
    x = np.zeros((1, max_char, char_dim))
    end = False
    i = 0
    
    while end==False:
        probs = list(model.predict(x)[0,i])
        probs = probs / np.sum(probs)
        index = np.random.choice(range(char_dim), p=probs)
        if i == max_char-2:
            character = '.'
            end = True
        else:
            character = index_to_char[index]
        name.append(character)
        x[0, i+1, index] = 1
        i += 1
        if character == ' ':
            end = True
    
    print(''.join(name))
    
# Generate 3 passwords every 5 epochs
def generate_name_loop(epoch, _):
    if epoch % 5 == 0:
        
        print('Names generated after epoch %d:' % epoch)

        for i in range(3):
            make_name(model)
        
        print()

name_generator = LambdaCallback(on_epoch_end = generate_name_loop)

model.fit(X, Y, batch_size=64, epochs=300, callbacks=[name_generator], verbose=0)
