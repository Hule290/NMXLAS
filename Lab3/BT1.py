import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt

data = iio.imread('exercise/colorful-ripe-tropical-fruits.jpg')
kiwi = data[920:1100, 390:570]

kiwi_shifted = nd.shift(kiwi, (0, 30, 0))

output = data.copy()
output[920:1100, 390:570] = kiwi_shifted  

plt.imshow(output)
plt.show()