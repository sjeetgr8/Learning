# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:55:20 2022

@author: Satya
"""

from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


"""

MNIST is a database. 
   The acronym stands for “Modified National Institute of Standards and Technology.” 
   The MNIST database contains handwritten digits (0 through 9), and can provide a baseline for testing image processing systems. 
   MNIST is the “hello world” of machine learning.
   
"""
train_images.shape
len(train_labels)
train_labels


## And here’s the test data:

test_images.shape
len(test_labels)
test_labels   

from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)

digit = train_images[4]
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


my_slice = train_images[10:100]
print(my_slice.shape)























