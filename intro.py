import sys
import numpy as np
import matplotlib as mp

X=[[1,2,3,2.5],
   [2.0,5.0,-1.0,2.0],
   [-1.5,2.7,3.3,-0.8]]

class DNet:
	def __init__(self,nip,neurons):
		self.w=0.1*np.random.randn(nip,neurons)
		self.b=np.zeros((1,nip))
	def forward(self,i):
		self.op=np.dot(i,self.w)

#Softmax Activation
class SMA:
	def __init__(self,i):
		self.vals=np.exp(i-np.max(i, axis=1, keepdims=True))
		self.probs=self.vals/np.sum(self.vals, axis=1, keepdims=True)

def main():
	print(str(sys.version)+"\n"+str(mp.__version__)+"\n"+str(np.__version__)+"\n")
	L1=DNet(4,5)
	Final=DNet(5,2)
	L1.forward(X)
	Final.forward(L1.op)
	F=SMA(Final.op)
	print(F.probs)

if __name__ == '__main__':
	main()