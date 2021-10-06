'''
Author: 零到正无穷
Date: 2021-02-18 10:34:46
LastEditTime: 2021-02-23 22:09:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\boston_house_price.py
'''
from keras.datasets import boston_housing
from keras import models
from keras import layers

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

print(train_data[0])

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model