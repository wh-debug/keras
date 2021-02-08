'''
Author: 零到正无穷
Date: 2021-02-03 16:31:40
LastEditTime: 2021-02-03 16:34:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\Reuters_data_set.py
'''
from keras.datasets import reuters

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words = 10000)
