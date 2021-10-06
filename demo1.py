"""测试consant的功能，以及函数各个形参的作用"""

import tensorflow as tf
input = [[1, 2, 3], [2, 3, 4]]
intput_tf = tf.constant(input)
print(intput_tf.get_shape().as_list())
print(intput_tf.dtype)

#todo  函数constant中的变量有constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
#todo  value 可以是数，也可以是列表，
#todo  dtype可以是常用的数据类型
#todo  shape可以是一个数，一个数组，矩阵等形状的表达，如shape=[], shape=[n],shape=[n,m]
#todo  name是字符串 
#todo  verify_shape是bool类型