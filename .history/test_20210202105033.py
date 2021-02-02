'''
Author: your name
Date: 2021-01-28 20:37:29
LastEditTime: 2021-02-01 09:18:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\test.py
'''
import tensorflow as tf
print(tf.__version__)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))