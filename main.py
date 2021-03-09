import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class DeepNet:
	def __init__(self, shape_x, shape_y, X_train, Y_train):
		self.model = keras.Sequential([keras.layers.Flatten(input_shape=(shape_x,shape_y)), keras.layers.Dense(8, activation='relu'),keras.layers.Dense(1, activation='sigmoid')])
		self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		self.model.fit(X_train, Y_train, epochs=10)

def main():
	print('DeepNet using TensorFlow ',tf.__version__)
	#iname=input("Enter the name of the input file: ")
	file=open("train.data",'r')
	#Y_train=file.readline().split(",")
	count=0
	X_train,Y_train=[],[]
	for line in file:
		if count==5:
			break
		txy=line.strip().split(",")
		tx=[]
		for i in range(8):
			tx.append(float(txy[i]))
		X_train.append(tx)
		Y_train.append(float(txy[8]))
		count+=1
	#print(int(Y_train[8]))
	print(X_train)
	print(Y_train)
	dlmod=DeepNet(8, 1, X_train, Y_train)
if __name__=='__main__':
	main()