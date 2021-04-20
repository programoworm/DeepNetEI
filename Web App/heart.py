# Heart Dataset 
'''
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
# load the dataset
dataset = loadtxt('rand_heart.data', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:13]
y = dataset[:,13]
# define the keras model
model = Sequential()
model.add(Dense(13, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, validation_split=0.33, epochs=250, batch_size=10, verbose=0)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
# save the model
model.save("model1.h5")
print("Saved model to disk")

'''
import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn

#Training data modelling
data=np.loadtxt("./Datasets/rand_heart.data",delimiter=",",comments='#')
X = data[:,0:13]
y = data[:,13]

#Model creation
dlmod=dn.DeepNet(13, 1,'adam','binary_crossentropy',[13,6],"Diabetes")

# compile the keras model
dlmod.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
dlmod.model.fit(X, y, epochs=250, batch_size=10)
# evaluate the keras model
_, accuracy = dlmod.model.evaluate(X, y)
# save the model
dlmod.model.save("model1.h5")
print("Saved model to disk")

