import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from tensorflow.keras import utils
import numpy as np
from PIL import Image

dataset1 = np.array([np.array(Image.open("/content/COVID-19_Radiography_Dataset/COVID_data/COVID-{}.png".format(fname)).convert('L')) for fname in range(1,1001)])

dataset2 = np.array([np.array(Image.open("/content/COVID-19_Radiography_Dataset/Normal_data/Normal-{}.png".format(fname)).convert('L')) for fname in range(1,1001)])

dataset3 = np.array([np.array(Image.open("/content/COVID-19_Radiography_Dataset/Pneumonia_data/Viral Pneumonia-{}.png".format(fname)).convert('L')) for fname in range(1,1001)])
dataset3.shape

dataset = np.concatenate((dataset1,dataset2,dataset3))

label1 = np.full(dataset1.shape[0],1)
label2 = np.full(dataset2.shape[0],0)
label3 = np.full(dataset3.shape[0],2)

label = np.concatenate((label1,label2,label3))

index = np.array([i for i in range(0,dataset.shape[0])])

np.random.shuffle(index)

data=[]
labels=[]
for i in index:
  data.append(dataset[i])
  labels.append(label[i])

X_train,X_test = np.split(data,[int(len(data)*0.8)])
Y_train,Y_test = np.split(labels,[int(len(labels)*0.8)])

X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],X_train.shape[2],1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],X_test.shape[2],1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255

classes = 3
print("Shape before one-hot encoding: ", Y_train.shape)
Y_train = utils.to_categorical(Y_train, classes)
Y_test = utils.to_categorical(Y_test, classes)
print("Shape after one-hot encoding: ", Y_train.shape)

# building a linear stack of layers with the sequential model
model = Sequential()
# convolutional layer
model.add(Conv2D(25, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu', input_shape=(X_train.shape[1],X_train.shape[2],1)))
model.add(MaxPool2D(pool_size=(1,1)))
# flatten output of conv
model.add(Flatten())
# hidden layer
model.add(Dense(100, activation='relu'))
# output layer
model.add(Dense(3, activation='softmax'))

model.summary()

# compiling the sequential model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
# training the model for 10 epochs
model.fit(X_train, Y_train, batch_size=128, epochs=10, validation_data=(X_test, Y_test))