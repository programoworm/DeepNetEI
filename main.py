import numpy as np
import matplotlib.pyplot as plt
import DeepNet as dn

def main():
	#print('DeepNet using TensorFlow ',tf.__version__)
	print('\nTraining the model\n=================\n')
	
	#Training data modelling
	data=np.loadtxt("./Datasets/d_train.data",delimiter=",")
	X_train=data[:,0:8]
	Y_train=data[:,8]

	#Testing data modelling
	data=np.loadtxt("./Datasets/d_test.data",delimiter=",")
	X_test=data[:,0:8]
	Y_test=data[:,8]
	
	#Model creation and training by constructor
	dlmod=dn.DeepNet(8, 1, [5,12])
		
	#print("\nTest Results\n============\n")
	
	#Testing data using test() method of the model
	dlmod.train_test(X_train,Y_train,X_test,Y_test,'adam','binary_crossentropy',250,10)
	
	#Verification of a signle testdata by rounding off
	#the neuron produced value
	y=np.round(dlmod.model.predict(X_test))
	print(y[2])
	#EndRange=(step*epoch+1) i.e. (250*5+1)
	e=np.arange(1,1251,5)
	plt.plot(e,dlmod.h.history['accuracy'],'g',label='Training Accuracy')
	plt.plot(e,dlmod.h.history['val_accuracy'],'b',label='Testing Accuracy')
	plt.title('Accuracy plotting')
	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.legend(['Test','Train'],loc='upper left')
	plt.show()

if __name__=='__main__':
	main()