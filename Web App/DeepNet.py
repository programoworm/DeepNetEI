import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from datetime import datetime
class DeepNet:
	
	def __init__(self, shape_x, shape_y, opt, l, neurons, mname, a):
		self.model=keras.Sequential([keras.layers.Flatten(input_shape=(shape_x,shape_y))]) 
		for n in neurons:
			self.model.add(keras.layers.Dense(n, activation='relu'))
		self.model.add(keras.layers.Dense(shape_y, activation=a))
		self.model.compile(optimizer=opt, loss=l, metrics=['accuracy'])
		self.mname=mname
	
	def train_test(self,X_train,Y_train,X_test,Y_test,e,bs):
		print('\nTraining the model\n=================\n')
		self.h=self.model.fit(X_train, Y_train, epochs=e, batch_size=bs, validation_data=(X_test,Y_test))
		print("\nTest Results for ",self.mname,"\n=========================\n")
		s=datetime.now()
		self.model.evaluate(X_test,Y_test)
		self.t=datetime.now()-s

	def plot(self,e):
		plt.plot(e,self.h.history['accuracy'])
		plt.plot(e,self.h.history['val_accuracy'])
		plt.title('model accuracy')
		plt.ylabel('accuracy')
		plt.xlabel('epoch')
		plt.legend(['train', 'test'], loc='upper left')
		plt.show()
		# summarize history for loss
		plt.plot(e,self.h.history['loss'])
		plt.plot(e,self.h.history['val_loss'])
		plt.title('model loss')
		plt.ylabel('loss')
		plt.xlabel('epoch')
		plt.legend(['train', 'test'], loc='upper left')
		plt.show()