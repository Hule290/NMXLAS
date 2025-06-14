import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt
data = iio.imread('colorful-ripe-tropical-fruits.jpg')
kiwiImg = data[920:1100, 390:570]

shifted = nd.shift(kiwiImg, (0, 30, 0))
shifted = np.clip(shifted, 0, 255).astype(np.uint8)

output = data.copy()
output[920:1100, 420:600] = shifted  

plt.figure(figsize=(12, 6))
plt.imshow(output)
plt.show()