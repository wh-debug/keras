'''
Author: Daylight
Date: 2021-02-03 17:02:23
LastEditTime: 2021-02-03 17:05:16
LastEditors: Please set LastEditors
Description: Python method verification
FilePath: \TensorFlow\Python_ method_ verification.py
'''
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

(train_image, train_labels), (test_image, test_labels) = mnist.load_data()

print(test_image.shape)