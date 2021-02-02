import numpy as np


#todo 实现两个矩阵相加
def native_add(x, y):
    assert len(x.shape) == 2    #todo 判断x是否为2D张量
    assert x.shape == y.shape   #todo 判断两个矩阵是否相等 

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x

num1 = np.array([[1,2,3,4],
                 [3,4,5,6],
                 [5,6,7,8]])

num2 = np.array([[2,3,4,5],
                 [3,4,5,6],
                 [4,5,6,7]])

num3 = np.array([[2,3,4,5],
                 [3,4,5,6]])

#todo 与函数中的结果相同
z = num1 + num2
z = np.maximum(z, 0)
print(z)
#print(native_add((num1, num3))) #todo 根据矩阵相加的法则，那么当两个矩阵大小不同时，那么会出现错误
print(native_add(num1, num2))