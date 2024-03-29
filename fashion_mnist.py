# -*- coding: utf-8 -*-
"""fashion mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jvaXT8G8wOXgGgOqeYe_XdXdONTVd82p
"""

from keras.models import Sequential
from keras.layers import Dense, Flatten, BatchNormalization, Dropout, Convolution2D, MaxPooling2D
from keras.datasets import fashion_mnist
from matplotlib import pyplot
from keras.utils import np_utils
import numpy as np

# load data
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

for i in range(25):
  pyplot.subplot(10/2, 10/2, i+1)
  pyplot.imshow(x_train[i])

num_class = len(np.unique(y_train))
print(num_class)

y_train = np_utils.to_categorical(y_train, num_classes=num_class)
y_test = np_utils.to_categorical(y_test, num_classes=num_class)

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

for i in range(25):
  pyplot.subplot(10/2, 10/2, i+1)
  pyplot.imshow(x_test[i])

input_shape = x_test.shape
print(input_shape)

x_train = x_train.reshape((60000, 28, 28, 1))
x_test = x_test.reshape((10000, 28, 28, 1))

x_train.shape

def model1():
  model = Sequential()
  model.add(Convolution2D(filters=32, kernel_size = 3, padding='same', input_shape = (28, 28, 1), activation = 'elu'))
  model.add(Droupout(0.2))
  model.add(MaxPooling2D(pool_size=2))
  model.add(BatchNormalization())
  model.add(Convolution2D(filters=64, kernel_size = 3, padding='same', activation = 'elu'))
  model.add(Droupout(0.2))
  model.add(MaxPooling2D(pool_size=2))
  model.add(BatchNormalization())
  model.add(Convolution2D(filters=128, kernel_size = 3, padding='same', activation = 'elu'))
  model.add(Droupout(0.2))
  model.add(MaxPooling2D(pool_size=2))
  model.add(BatchNormalization())
  model.add(Convolution2D(filters=256, kernel_size = 3, padding='same', activation = 'elu'))
  model.add(Droupout(0.2))
  model.add(MaxPooling2D(pool_size=2))
  model.add(BatchNormalization())
  model.add(Flatten())
  model.add(Dense(10, activation = 'softmax'))
  return model

model = model1()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x_train, y_train, validation_split=0.2, batch_size=32, epochs=20, shuffle=True, verbose=1)

print(history.history.keys())

pyplot.plot(history.history['loss'], color = 'red')
pyplot.plot(history.history['val_loss'])
pyplot.title('model loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'test'], loc='upper left')
pyplot.show()

pyplot.plot(history.history['acc'], color = 'red')
pyplot.plot(history.history['val_acc'])
pyplot.title('model accuracy')
pyplot.ylabel('accuracy')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'test'], loc='upper left')
pyplot.show()

