'''
Author: 零到正无穷
Date: 2021-02-14 21:32:16
LastEditTime: 2021-02-18 08:55:01
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\TF_1.py
'''
# TensorFlow and tf.keras
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()