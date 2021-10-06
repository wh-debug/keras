'''
Author: your name
Date: 2021-01-28 20:37:29
LastEditTime: 2021-02-25 20:59:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\test.py
'''
import tensorflow as tf
print(tf.__version__)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

num = [[1,2,3],[1,2,5]] #todo 列表里面保存列表
print(num)

def add(x, y) -> int:
    return x + y

