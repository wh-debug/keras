'''
Author: Daylight
Date: 2021-02-03 20:31:42
LastEditTime: 2021-02-03 20:37:01
LastEditors: Please set LastEditors
Description: Learn 3D tensors
FilePath: \TensorFlow\Learn_3D_ tensors.py
'''
import numpy as np 
import tensorflow as tf

#todo 输出(3, 2, 5)
num = np.array([[[ 0, 1, 2, 3, 4],
                 [ 5, 6, 7, 8, 9]],
                [[10, 11, 12, 13, 14],
                 [15, 16, 17, 18, 19]],
                [[20, 21, 22, 23, 24],
                 [25, 26, 27, 28, 29]]])

print(num.shape)