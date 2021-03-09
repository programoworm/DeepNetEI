import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow import keras
import numpy as np

class DeepNet:
	
	def __init__(self, shape_x, shape_y, X_train, Y_train):
		self.model = keras.Sequential([keras.layers.Flatten(input_shape=(shape_x,shape_y)), keras.layers.Dense(8, activation='relu'),keras.layers.Dense(1, activation='sigmoid')])
		self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
		self.model.fit(X_train, Y_train, epochs=100)
<<<<<<< HEAD
=======
	
>>>>>>> master
	def test(self,X_test,Y_test):
		self.model.evaluate(X_test,Y_test)

def main():
	print('DeepNet using TensorFlow ',tf.__version__)
<<<<<<< HEAD
	file=open("train.data",'r')
=======
	print('\nTraining the model\n=================\n')
	file=open("./Datasets/d_train.data",'r')
>>>>>>> master
	X_train,Y_train=[],[]
	for line in file:
		txy=line.strip().split(",")
		tx=[]
		for i in range(8):
			tx.append(float(txy[i]))
		X_train.append(tx)
		Y_train.append(float(txy[8]))
<<<<<<< HEAD
	print(np.array(X_train))
	print(np.array(Y_train))
	print(np.array(X_train).shape)
	file=open("test.data",'r')
	dlmod=DeepNet(8, 1, np.array(X_train), np.array(Y_train))
=======
	dlmod=DeepNet(8, 1, np.array(X_train), np.array(Y_train))
	file=open("./Datasets/d_test.data",'r')
>>>>>>> master
	X_test=[]
	Y_test=[]
	for line in file:
		txy=line.strip().split(",")
		tx=[]
		for i in range(8):
			tx.append(float(txy[i]))
		X_test.append(tx)
		Y_test.append(float(txy[8]))
	print("\nTest Results\n============\n")
	dlmod.test(np.array(X_test),np.array(Y_test))
<<<<<<< HEAD
=======

>>>>>>> master
if __name__=='__main__':
	main()