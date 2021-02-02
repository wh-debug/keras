from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt


(train_image, train_labels), (test_image, teat_labels) = mnist.load_data()
digit = train_image[4]
plt.imshow(digit, cmap = plt.cm.binary)
plt.show()

