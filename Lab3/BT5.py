import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pyplot as plt
import os

img_folder = "exercise"
image_files = ["colorful-ripe-tropical-fruits.jpg", "pagoda.jpg", "quang_ninh.jpg"]

print("Chọn thao tác:")
print("T - Tịnh tiến")
print("X - Xoay")
print("P - Phóng to")
print("H - Thu nhỏ")
print("C - Coordinate Map")

choice = input("Nhập lựa chọn (T/X/P/H/C): ").upper()

if choice not in ['T', 'X', 'P', 'H', 'C']:
    print("Lựa chọn không hợp lệ.")
    exit()

print("Chọn ảnh (1, 2 hoặc 3):")
img_index = int(input("Nhập số: ")) - 1
if img_index not in [0, 1, 2]:
    print("Số ảnh không hợp lệ.")
    exit()

img_path = os.path.join(img_folder, image_files[img_index])
img = iio.imread(img_path)

if choice == 'T':
    result = nd.shift(img, (0, 30, 0)) 
elif choice == 'X':
    result = nd.rotate(img, 45, reshape=True)
elif choice == 'P':
    result = nd.zoom(img, (5, 5, 1)) 
elif choice == 'H':
    result = nd.zoom(img, (1/5, 1/5, 1)) 
elif choice == 'C':
    H, W, C = img.shape
    M = np.indices((H, W))

    d = 5
    q = 2 * d * np.random.rand(*M.shape) - d 
    mp = (M + q).astype(int)

    mp[0] = np.clip(mp[0], 0, H - 1)
    mp[1] = np.clip(mp[1], 0, W - 1)
    result = np.zeros_like(img)
    for i in range(C):  
        result[:, :, i] = img[mp[0], mp[1], i]

plt.subplot(1, 2, 1)
plt.title("Ảnh Gốc")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title("Ảnh Sau Biến Đổi")
plt.imshow(result)

plt.show()
