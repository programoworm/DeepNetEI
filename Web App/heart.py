# Heart Dataset 
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