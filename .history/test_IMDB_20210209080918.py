'''
Author: Daylight
Date: 2021-02-08 22:00:32
LastEditTime: 2021-02-08 22:50:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\test_IMDB.py
'''
# -*- coding: utf-8 -*-

from keras.datasets import imdb
from keras import models
from keras import layers
import numpy as np
import matplotlib.pyplot as plt

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)
# print(train_data[1])
# print(train_data.ndim)   #todo 输出1D张量
# print(train_data.shape)  #todo 输出(25000,)
word_index = imdb.get_word_index()
# print(word_index)
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# print(reverse_word_index)
decoded_review = ''.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])
print(decoded_review)



