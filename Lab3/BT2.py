import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt
data = iio.imread('colorful-ripe-tropical-fruits.jpg')
dudu = data[330:810, 125:670]
duahau = data[315:1100, 1635:2100]

dudu_changed = dudu[:, :, ::-1]
duahau_changed = duahau[:, :, ::-1]

plt.subplot(1, 2, 1)
plt.imshow(dudu_changed)

plt.subplot(1, 2, 2)
plt.imshow(duahau_changed)

plt.show()