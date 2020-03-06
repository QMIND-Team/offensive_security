# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:10:37 2020

@author: lewis
"""
from Model import Model
from keras.models import load_model

epochLimit = 300

ProbabilityDemo = 0

##DEMO
model1 = Model("loadModel2", "pass.txt")
model1.prepTrainingSet() # Perform preprocessing to data

model1.buildModel(epochLimit,0) # Build the model, Include limit 
#model1.buildModel(0,1)
model1.model.save(model1.name+'.h5')
#model1.model = load_model("loadModel.h5")

if (ProbabilityDemo):
    model1.make_name(1)

else:
    model1.generateTextFile(100000)



