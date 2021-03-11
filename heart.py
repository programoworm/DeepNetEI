# Heart Dataset 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

np.random.seed(0)

# load the dataset
dataset=np.loadtxt('./Datasets/rand_heart.data', delimiter=',')

# split into input (X) and output (y) variables
X_train=dataset[:250,0:13]
y_train=dataset[:250,13]

X_test=dataset[251:,0:13]
y_test=dataset[251:,13]
# define the keras model
'''model=keras.Sequential()
model.add(Dense(13, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
'''
model=keras.Sequential([keras.layers.Flatten(input_shape=(13,1)), 
			keras.layers.Dense(5, activation='relu'),
			keras.layers.Dense(12, activation='relu'),
			keras.layers.Dense(1, activation='sigmoid')])
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
history = model.fit(X_train, y_train, validation_split=0.33, epochs=250, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X_test, y_test)
print('Accuracy: %.2f' % (accuracy*100))
# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()