'''
Author: Daylight
Date: 2021-02-03 17:22:44
LastEditTime: 2021-02-03 20:20:06
LastEditors: Please set LastEditors
Description: Learn 1D tensor
FilePath: \TensorFlow\Learn_1D_ tensor.py
'''
'''
数字组成的数组叫做向量或一维张量。一维张量只有一个轴。如下面的例子所示。
'''
import numpy as np 

num = np.array([1,2,3,4,5,6,7])  #todo 1D张量
num1 = np.array([1,2,3,4])       #todo 1D张量
num2 = np.array([[1,2,3,4],
                [4,5,6,7],
                [7,8,9,0]])

print(num.shape)
print(num1.shape)
print(num2.shape)
print(f"num.ndim={num.ndim},num1.ndim={num1.ndim},num2.ndim={num2.ndim}")

'''
num2 = np.array([1,2,3,4],
                [4,5,6,7],
                [7,8,9,0])
这样使用num2.ndim输出时会报错证明1D张量，在括号里只能有一个中括号
'''
'''
num2 = np.array([[1,2,3,4],
                [4,5,6,7],
                [7,8,9,0]])

这样num2.ndim输出等于2。可见此时他为2D张量
'''