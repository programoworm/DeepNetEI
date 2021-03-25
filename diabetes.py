#Diabetes Dataset
import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn

def diabetes():
	#Training data modelling
	data=np.loadtxt("./Datasets/diabetes.data",delimiter=",",comments='#')
	X_train=data[:559,0:8]
	Y_train=data[:559,8]

	#Testing data modelling
	X_test=data[560:,0:8]
	Y_test=data[560:,8]
	
	#Model creation
	dlmod=dn.DeepNet(8, 1,'adam','binary_crossentropy',[5,3],"Diabetes")

	#Training and Testing of the data
	dlmod.train_test(X_train,Y_train,X_test,Y_test,250,10)
	
	#Verification of a signle testdata by rounding off the neuron produced value
	y=np.round(dlmod.model.predict(X_test))
	print(y[2])
	#EndRange=(step*epoch+1) i.e. (250*5+1)
	
	e=np.arange(1,251,1)
	plt.plot(e,dlmod.h.history['accuracy'])
	plt.plot(e,dlmod.h.history['val_accuracy'])
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()
	# summarize history for loss
	plt.plot(e,dlmod.h.history['loss'])
	plt.plot(e,dlmod.h.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()