'''
Author: Daylight
Date: 2021-02-03 17:02:23
LastEditTime: 2021-02-03 17:11:02
LastEditors: Please set LastEditors
Description: Python method verification
FilePath: \TensorFlow\Python_ method_ verification.py
'''
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

(train_image, train_labels), (test_image, test_labels) = mnist.load_data()

print(len(train_image))   #todo 60000
print(train_image.shape)  #todo (60000, 28, 28)
print(len(train_labels))  #todo 60000
print(train_labels)      
print(train_image.ndim) 

print(len(test_image))    #todo 10000
print(test_image.shape)   #todo (10000, 28, 28)
print(len(test_labels))   #todo 10000
print(test_labels)
print(test_image.ndim)