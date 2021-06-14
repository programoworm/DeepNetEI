import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn
from time import time
def corona():
  dataset = np.genfromtxt('./Datasets/corona_tested_individuals_updated.csv', delimiter=',')
  X = dataset[1:1000,:-1]
  Y = dataset[1:1000,-1]
	# split into input (X) and output (y) variables
  X_train,X_test=np.split(X,[int(len(X)*0.8)])
  Y_train,Y_test=np.split(Y,[int(len(Y)*0.8)])

#  print(X_test[len(X_test)-11])
#  print(X_test[len(X_test)-11].reshape(8,1))
  #Model creation
  dlmod=dn.DeepNet(X_train.shape[1], 1,'adam', 'binary_crossentropy',[5],"Corona",'sigmoid')
  #Training and Testing of the data
  
  dlmod.train_test(X_train,Y_train,X_test,Y_test,25,8)
	#Verification of a single testdata by rounding off the neuron produced value
  s=time()
  print(len(X_test))
  print(X_train[1])#X_test[len(X_test)-26])
  print(X_train[0])#X_test[len(X_test)-26])
  y1=np.round(dlmod.model.predict(X_train[1].reshape(1,8)))#X_test[len(X_test)-26].reshape(1,8)))
  y2=np.round(dlmod.model.predict(X_train[0].reshape(1,8)))#X_test[len(X_test)-26].reshape(1,8)))
  t=time()-s
  print(t)
  print(y1)
  print(y2)
  #EndRange=(step*epoch+1) i.e. (250*5+1)
  e=np.arange(1,11,1)
  dlmod.model.save("covid.h5")