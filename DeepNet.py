import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow import keras

class DeepNet:
	
	def __init__(self, shape_x, shape_y, opt, l, neurons, mname):
		self.model=keras.Sequential([keras.layers.Flatten(input_shape=(shape_x,shape_y))]) 
		for n in neurons:
			self.model.add(keras.layers.Dense(n, activation='relu'))
		self.model.add(keras.layers.Dense(shape_y, activation='sigmoid'))
		self.model.compile(optimizer=opt, loss=l, metrics=['accuracy'])
		self.mname=mname
	
	def train_test(self,X_train,Y_train,X_test,Y_test,e,bs):
		print('\nTraining the model\n=================\n')
		self.h=self.model.fit(X_train, Y_train, epochs=e, batch_size=bs, validation_data=(X_test,Y_test))
		print("\nTest Results for ",self.mname,"\n=========================\n")
		self.model.evaluate(X_test,Y_test)