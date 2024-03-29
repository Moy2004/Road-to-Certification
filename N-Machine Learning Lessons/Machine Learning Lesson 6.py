"""
2023 4/17
1444 رَمَضَان 26

Handwritten Digit Recognition with Tensorflow
"""
import cv2 as cv  # it's an open cv library
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# loading data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Adding layer
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

# Adding dense layer
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))

# output dense layer
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

# Compiling
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)  # how many times this should repeat

loss, accuracy = model.evaluate(x_test, y_test)
print(loss)
print(accuracy)

model.save('digits.model')

# scanning input by user to determine
for x in range(1, 6):
    img = cv.imread(f'{x}.png')[:, :, 0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print(f'The given image is most likely to be: {np.argmax(prediction)}')
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()

"""
Quick 日記
Before doing this lesson, there was lesson about
nural networks and how it works. So I do have basic Idea of how this work
"""
