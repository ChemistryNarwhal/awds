pip install tensorflow tensorflow-gpu opencv matplotlib

import tensorflow as tf
import os #nagation though file struters on all operating sistems 

#stop from using all your memory
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    ft.config.experimental.set_memory_growth(gpu, True)

import cv2
import imghdr #checks extenchens 

data_dir = 'data'
