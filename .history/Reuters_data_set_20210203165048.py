'''
Author: 零到正无穷
Date: 2021-02-03 16:31:40
LastEditTime: 2021-02-03 16:50:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\Reuters_data_set.py
'''
from keras.datasets import reuters

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words = 10000)

print(train_data.shape)
print(train_data.ndim)
print(len(train_data))   #todo 8982
print(len(train_labels)) #todo 8982
print(len(test_data))    #todo 2246
print(len(test_labels))  #todo 2246
print(test_data)
print("\n")
print(test_data[0])