#!/usr/bin/python3

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = tf.Keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.laayers.Dense(10, activation=tf.nn.softmax)])
