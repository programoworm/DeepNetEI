import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow import keras
import numpy as np

class DeepNet:
	def __init__(self, shape_x, shape_y, X_train, Y_train):
		self.model = keras.Sequential([keras.layers.Flatten(input_shape=(shape_x,shape_y)), 
			keras.layers.Dense(5, activation='relu'),
			keras.layers.Dense(12, activation='relu'),
			keras.layers.Dense(1, activation='sigmoid')])
		self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
		self.model.fit(X_train, Y_train, epochs=150, batch_size=10)
	
	def test(self,X_test,Y_test):
		self.model.evaluate(X_test,Y_test)

def main():
	print('DeepNet using TensorFlow ',tf.__version__)
	print('\nTraining the model\n=================\n')
	
	#Training data modelling
	data=np.loadtxt("./Datasets/d_train.data",delimiter=",")
	X_train=data[:,0:8]
	Y_train=data[:,8]

	#Model creation and training by constructor
	dlmod=DeepNet(8, 1, np.array(X_train), np.array(Y_train))
	
	#Testing data modelling
	data=np.loadtxt("./Datasets/d_test.data",delimiter=",")
	X_test=data[:,0:8]
	Y_test=data[:,8]
	print("\nTest Results\n============\n")
	
	#Testing data using test() method of the model
	dlmod.test(np.array(X_test),np.array(Y_test))
	
	#Verification of a signle testdata by rounding off
	#the neuron produced value
	y=np.round(dlmod.model.predict(X_test))
	print(y[2])

if __name__=='__main__':
	main()