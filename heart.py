# Heart Dataset 
import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn
def heart():
	# load the dataset
	dataset=np.loadtxt('./Datasets/rand_heart.data', delimiter=',')

	# split into input (X) and output (y) variables
	X_train=dataset[:250,0:13]
	Y_train=dataset[:250,13]

	X_test=dataset[251:,0:13]
	Y_test=dataset[251:,13]

	#Model creation
	dlmod=dn.DeepNet(13, 1,'adam','binary_crossentropy',[10,6],"Heart")
	#Training and Testing of the data
	dlmod.train_test(X_train,Y_train,X_test,Y_test,250,10)
	
	#Verification of a signle testdata by rounding off the neuron produced value
	y=np.round(dlmod.model.predict(X_test))
	print(y[2])
	#EndRange=(step*epoch+1) i.e. (250*5+1)
	# summarize history for accuracy
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
