# Diabetes Dataset
'''
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
# load the dataset
dataset = loadtxt('d_test.data', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=250, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
# save the model
model.save("model.h5")
print("Saved model to disk")

'''
import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn

#Training data modelling
data=np.loadtxt("Datasets/diabetes.data",delimiter=",",comments='#')
X = data[:,0:8]
y = data[:,8]

#Model creation
dlmod=dn.DeepNet(8, 1,'adam','binary_crossentropy',[12,8],"Diabetes")

# compile the keras model
dlmod.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
dlmod.model.fit(X, y, epochs=250, batch_size=10)
# evaluate the keras model
_, accuracy = dlmod.model.evaluate(X, y)
# save the model
dlmod.model.save("diabetes.h5")
print("Saved model to disk")
