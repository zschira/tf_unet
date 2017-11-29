from __future__ import print_function, division, absolute_import, unicode_literals
from tf_unet import image_gen
from tf_unet import unet
from tf_unet import util

nx = 80
ny = 80

mx = 320
my = 320

training_iters = 1000
epochs = 100
dropout = 0.75 # Dropout, probability to keep units
display_step = 2
restore = False

