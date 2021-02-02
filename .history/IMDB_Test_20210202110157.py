'''
Author: 零到正无穷
Date: 2021-01-31 19:51:47
LastEditTime: 2021-02-02 11:01:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\IMDB_Test.py
'''
from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)
# print(train_data[1])
# print(train_data.ndim)   #todo 输出1D张量
# print(train_data.shape)  #todo 输出(25000,)
word_index = imdb.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.item()])
decoded_review = ''.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

