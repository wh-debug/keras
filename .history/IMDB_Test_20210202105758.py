'''
Author: 零到正无穷
Date: 2021-01-31 19:51:47
LastEditTime: 2021-02-02 10:57:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\IMDB_Test.py
'''
from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)
print(train_data[1])
print(train_data.ndim)   #todo 输出1
print(train_data.shape)  #todo 输出(25000,)