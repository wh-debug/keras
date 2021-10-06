import tensorflow as tf
input = [[1, 2, 3], [2, 3, 4]]
input_tf = tf.constant(input, dtype = tf.float32, shape = [3, 2])
print("input_tf shape :", input_tf.get_shape().as_list())
print("input_tf dtype :", input_tf.dtype)

with tf.Session() as sess:
    print("input_tf value :\n", sess.run(input_tf))