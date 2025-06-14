import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt
data = iio.imread('colorful-ripe-tropical-fruits.jpg')
dudu = data[330:810, 125:670]
duahau = data[315:1100, 1635:2100]

dudu_changed = dudu[:, :, ::-1]

duahau_changed = np.clip(duahau + 50, 0, 255).astype(np.uint8)

data_result = data.copy()
data_result[330:810, 125:670] = dudu_changed
data_result[315:1100, 1635:2100] = duahau_changed

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Ảnh Gốc")
plt.imshow(data)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Ảnh Sau Khi Đổi Màu")
plt.imshow(data_result)
plt.axis("off")

plt.tight_layout()
plt.show()