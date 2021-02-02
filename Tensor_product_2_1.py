import numpy as np

def native_matrix_vector_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z

num1 = np.array([[1,2,3,4],
                [3,4,5,6],
                [5,6,7,8]])

num2 = np.array([1,2,3,4])

print(native_matrix_vector_dot(num1, num2))
