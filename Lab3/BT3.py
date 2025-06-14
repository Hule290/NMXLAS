import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt
data = iio.imread('quang_ninh.jpg')
nui = data[25:330, 445:655]
thuyen = data[455:545, 490:655]

nui_xoay = nd.rotate(nui, 45, reshape = True)
thuyen_xoay = nd.rotate(thuyen, 45, reshape = True)

plt.imsave('nui_xoay.jpg',nui_xoay)
plt.imsave('thuyen.jpg',thuyen_xoay)

plt.subplot(1, 2, 1)
plt.imshow(nui_xoay)

plt.subplot(1, 2, 2)
plt.imshow(thuyen_xoay)

plt.show()