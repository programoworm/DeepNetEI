#Heart Dataset 
import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn
from time import time
def heart():
	# load the dataset
	dataset=np.loadtxt('./Datasets/rand_heart.data', delimiter=',')

	# split into input (X) and output (y) variables
	X_train=dataset[:242,0:13]
	Y_train=dataset[:242,13]

	X_test=dataset[243:,0:13]
	Y_test=dataset[243:,13]

	#Model creation
	dlmod=dn.DeepNet(13, 1,'adam','binary_crossentropy',[10,6],"Heart",'sigmoid')
	#Training and Testing of the data
	dlmod.train_test(X_train,Y_train,X_test,Y_test,250,10)
	
	#Verification of a signle testdata by rounding off the neuron produced value
	t=time()
	y=np.round(dlmod.model.predict(X_test))
	t=time()-t
	print(t)
	print(y[2])
	dlmod.model.save('Models/DeepNetEI_heart')
	#EndRange=(step*epoch+1) i.e. (250*5+1)
	# summarize history for accuracy and loss
	e=np.arange(1,251,1)
	dlmod.plot(e)