'''
Author: 零到正无穷
Date: 2021-01-31 19:51:47
LastEditTime: 2021-02-02 11:28:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\IMDB_Test.py
'''
from keras.datasets import imdb
from keras import models
from keras import layers
import numpy as np

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)
# print(train_data[1])
# print(train_data.ndim)   #todo 输出1D张量
# print(train_data.shape)  #todo 输出(25000,)
word_index = imdb.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.item()])
decoded_review = ''.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

def vectorize_sequences(sequences, dimension = 10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

x_train = vectorize_sequences(train_data)
x_train = vectorize_sequences((test_data))

y_train = np.asarray(train_labels).astype('float32')
y_test  = np.asarray(test_labels).astype('float32')

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

x_val =x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(partial_x_train,)   

