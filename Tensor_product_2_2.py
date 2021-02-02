import numpy as np

num1 = np.array([[1,2,3,4],
                 [3,4,5,6],
                 [5,6,7,8]])

num2 = np.array([[2,3,4,5],
                 [3,4,5,6],
                 [4,5,6,7],
                 [5,6,7,8]])
#todo 两个一维向量相乘，
def native_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] == y.shape[0]

    z = 0.    #todo 有"."输出40.0，没有"."输出40
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z
#todo 两个二维向量相乘
def native_matrix_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]

    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = native_vector_dot(row_x, column_y)
    return z

print(num1.shape[1])
print(num2.shape[0])
print(native_matrix_dot(num1, num2))
print(num1[0, :])