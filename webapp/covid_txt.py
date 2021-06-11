import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn
from time import time
def corona():
  dataset = np.genfromtxt('./Datasets/corona_tested_individuals_updated.csv', delimiter=',')
  X = dataset[1:56000,:-1]
  Y = dataset[1:56000,-1]
	# split into input (X) and output (y) variables
  X_train,X_test=np.split(X,[int(len(X)*0.8)])
  Y_train,Y_test=np.split(Y,[int(len(Y)*0.8)])

  #Model creation
  dlmod=dn.DeepNet(X_train.shape[1], 1,'adam', 'binary_crossentropy',[10,6],"Corona",'sigmoid')
  #Training and Testing of the data
  
  dlmod.train_test(X_train,Y_train,X_test,Y_test,1,32)
	#Verification of a single testdata by rounding off the neuron produced value
  s=time()
  y=np.round(dlmod.model.predict(X_test))
  t=time()-s
  print(t)
  print("predicted",y[2])
  #EndRange=(step*epoch+1) i.e. (250*5+1)
  e=np.arange(1,11,1)
  dlmod.model.save("covid.h5")
  
if __name__ == '__main__':
  corona()