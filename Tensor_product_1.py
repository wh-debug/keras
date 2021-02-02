import numpy as np

num1 = np.array([1,2,3,4])

num2 = np.array([2,3,4,5])

z = np.dot(num1, num2)
print(z)

#todo 下列函数与上面的结果相同
def native_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] == y.shape[0]

    z = 0.    #todo 有"."输出40.0，没有"."输出40
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z

print(native_vector_dot(num1, num2))