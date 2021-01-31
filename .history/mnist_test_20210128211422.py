from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

(train_image, train_labels), (test_image, teat_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

train_image = train_image.reshape((60000, 28*28))
train_image = train_image.astype('float32') / 255

test_image = test_image.reshape((10000, 28*28))
test_image = test_image.astype('float32') / 255

train_labels = to_categorical((train_labels))
teat_labels = to_categorical(teat_labels)

network.fit(train_image, train_labels, epochs=5, batch_size=128)