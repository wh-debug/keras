'''
Author: Daylight
Date: 2021-02-03 17:12:31
LastEditTime: 2021-02-03 17:19:52
LastEditors: Please set LastEditors
Description: Learn 0D tensor
FilePath: \TensorFlow\Learn_0D_tensor.py
'''
'''
仅包含一个数字的张量叫做标量（也叫做标量张量，零维张量，0D张量）。可以用方法(.ndim)
查看张量的维数，下面的例子是一个numpy的标量
'''

import numpy as np 
num = np.array(12)
print(f"ouput = {num.ndim}")  

'''
在vscode中输出：
-------------------
0
----------------------
'''