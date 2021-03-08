import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class DeepNet:
	def __init__(self,shape_x,shape_y,X_train,Y_train):
		self.model = keras.Sequential([keras.layers.Flatten(input_shape=(shape_x,shape_y)), keras.layers.Dense(100, activation='relu'),keras.layers.Dense(10, activation='sigmoid')])
		self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		self.model.fit(X_train, Y_train, epochs=10)

def main():
	print('DeepNet using TensorFlow')

if __name__=='__main__':
	main()