#Diabetes Dataset
import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn
from time import time
def diabetes():
	#Training data modelling
	data=np.loadtxt("./Datasets/diabetes.data",delimiter=",",comments='#')
	X_train=data[:615,0:8]
	Y_train=data[:615,8]

	#Testing data modelling
	X_test=data[616:,0:8]
	Y_test=data[616:,8]
	
	#Model creation
	dlmod=dn.DeepNet(8, 1,'adam','binary_crossentropy',[12,8],"Diabetes")

	#Training and Testing of the data
	dlmod.train_test(X_train,Y_train,X_test,Y_test,250,10)
	
	#Verification of a single testdata by rounding off the neuron produced value
	t=time()
	y=np.round(dlmod.model.predict(X_test))
	t=time()-t
	print(t)
	print(y[2])
	#EndRange=(step*epoch+1) i.e. (250*5+1)
	dlmod.model.save('Models/DeepNetEI_diab')
	e=np.arange(1,251,1)
	dlmod.plot(e)