import numpy as np

#todo [1, 2]是2阶矩阵的第一行而非第一列
num1 = [[1,2],[3,4]]
num2 = [[5,6],[8,9]]

out = np.dot(num1, num2)
print(out)