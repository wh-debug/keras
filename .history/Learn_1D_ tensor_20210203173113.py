'''
Author: Daylight
Date: 2021-02-03 17:22:44
LastEditTime: 2021-02-03 17:31:13
LastEditors: Please set LastEditors
Description: Learn 1D tensor
FilePath: \TensorFlow\Learn_1D_ tensor.py
'''
'''
数字组成的数组叫做向量或一维张量。一维张量只有一个轴。如下面的例子所示。
'''
import numpy as np 

num = np.array([1,2,3,4,5,6,7])
num1 = np.array([1,2,3,4])
num2 = np.array([1,2,3,4],
                [4,5,6,7],
                [7,8,9,0])

print(f"num.ndim={num.ndim},num1.ndim={num1.ndim},num2.ndim={num2.ndim}")