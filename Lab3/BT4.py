import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt

data = iio.imread('exercise/pagoda.jpg')
chua = data[125:320, 0:570]

chua_zoom = nd.zoom(chua, 5)

plt.imsave('chua_zoom.jpg', chua_zoom)

plt.subplot(1,2,1)
plt.imshow(chua)

plt.subplot(1,2,2)
plt.imshow(chua_zoom)

plt.show()