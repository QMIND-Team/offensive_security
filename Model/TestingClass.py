# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:10:37 2020

@author: lewis
"""
from Model import Model
from Testing import Testing

epochLimit = 30
epochLimit2 = 50
addedFile = open('5k.txt','r').readlines()

model1 = Model("TestModel", "5k2.txt") # Initialize model object with a name and a training set

model1.prepTrainingSet() # Perform preprocessing to data

model1.buildModel(epochLimit) # Build the model, Include limit 

model1.model.save(model1.name+'.h5') # Save the model so that new data can be added

model1.prepTrainingSet(addedFile) # Reprocess data with added file

model1.continueTraining(epochLimit2) # Continue training with new epoch limit

testObj = Testing()


