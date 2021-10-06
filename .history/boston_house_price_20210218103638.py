'''
Author: 零到正无穷
Date: 2021-02-18 10:34:46
LastEditTime: 2021-02-18 10:36:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\boston_house_price.py
'''
from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()