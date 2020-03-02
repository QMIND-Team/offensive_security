# Model Documentation
## Initialization
Import the file:

    from model import model
 Initialize an object
    
    modelObject = Model(modelName, fileName)
   

 - modelName - Choose a name for the model as a string
 - fileName - Give the name of the initial training set, include file type (.txt)
 
 ## Preprocessing
 

    modelObject.prepTrainingSet(addedFile)
   

 - Adding a file is *optional* and should only be when adding a new file, it does not need to be called for the initial training data
 - When adding a file ensure that it is opened as follows:
	 - `addedFile = open("filename.txt", 'r').readlines()`

 - This function fully preps the data for the model

## Model Functionality

    modelObject.buildModel(epochLimit)
   

 - Once preprocessing is complete, call this function with an epoch limit
	 - The reason there is an epoch limit is because the program **cannot** continue to run while the model is training.



  `modelObject.continueTraining(epochLimit)`

 - After adding a new data to the training set, this function will resume training with a new epoch limit

`modelObject.generateTextFile(outputLength)`

 - Create a file with 'outputLength' number of passwords
 
## Visualizing Probability
 - Run `model.make_name(display)`
 - Pass in display as 1 and it will generate each character while printing a new graph


## How to add new data
Prepare the new data: `addedFile = open('fileName.txt','r').readlines()`

Save the Model: `modelObject.model.save(modelObject.name+'.h5')`

Reprocess the data: `modelObject.prepTrainingSet(addedFile)`

Resume Training: `modelObject.continueTraining(epochLimit)`

## How to load a model
First, include the library from keras: `from keras.models import load_model`

Create a new model object `modelObject = Model('ModelName', 'textFile')`
 - Important Note: the text file used, MUST be the same as the one that trained the model

Compile the model `model1.buildModel`
 - No parameters need to be passed in, but if it is causing issues use buildModel(0,1) instead
 
Load the model `modelObject.model = load_model("modelName.h5")`

## Known Issues

 - Some text files causes issues if they have characters outside the range of ascii 33-126 (! to ~)
	 - I'm trying to fix this with a script, but it doesn't seem strip the character properly
 - If the new file added has a single password that is longer than the longest password in the initial list, the model cannot continue.
	 - This is because the shape input shape of the model is determined by the longest password in the first list. Removing the layer and re-adding it would remove parameter values, which would just be equivalent to retraining
	 - I cannot think of any fix for this other than completely retraining the model, or reworking the structure
	 - Temporary fix: Run text file through Md5Encrypt.py, then through ReduceSize.py and then through SplitPassHash.py, and use the outputed password file.

    

   
   

