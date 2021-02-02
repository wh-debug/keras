import numpy as np

x = [1,2]
y = [3,4]

num1 = [[1,2],[3,4]]
num2 = [[5,6],[8,9]]

z = x + y
z = np.maximum(z, 0.)

t = num1 + num2
t = np.maximum(t, 0.)

print(z)
print(t)