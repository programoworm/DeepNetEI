# Diabetes Dataset
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