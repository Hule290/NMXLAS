# Giải thích LAB3

# Công nghệ sử dụng
- Python:
  Ngôn ngữ lập trình chính 
- NumPy: Thư viện xử lý mảng số học, giúp truy cập và thao tác dữ liệu ảnh dạng ma trận (pixel).
- SciPy: Cung cấp các hàm xử lý ảnh như xoay, phóng to, tịnh tiến, làm mờ, v.v.
- Matplotlib: Dùng để hiển thị ảnh và trực quan hóa kết quả bằng biểu đồ hoặc subplot.
- ImageIO: Dùng để đọc và ghi file ảnh dưới nhiều định dạng khác nhau.
- Os: Làm việc với hệ thống file, ví dụ: duyệt thư mục, kiểm tra ảnh có tồn tại không.

# BT1:
```python
import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt
```
Các thư viện được sử dụng trong bài này

```python
data = iio.imread('exercise/colorful-ripe-tropical-fruits.jpg')
kiwiImg = data[920:1100, 390:570]
```
lấy ảnh từ thư mục và cắt ảnh theo yêu cầu của bài

```python
kiwi_shifted = nd.shift(kiwi, (0, 30, 0))
```
Dịch chuyển hình sang phải 30 pixel

```python
output = data.copy()
output[920:1100, 390:570] = kiwi_shifted  
```
Tạo bản sao của ảnh góc
Dán hình đã dịch chuyển vào đúng vị trí ban đầu
  
```python
plt.imshow(output)
plt.show()
```
Hiển thị ảnh kết quả

# BT2:
```python
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt
```
Các thư viện được sử dụng trong bài này

```python
data = iio.imread('exercise/colorful-ripe-tropical-fruits.jpg')
dudu = data[330:810, 125:670]
duahau = data[315:1100, 1635:2100]
```
lấy ảnh từ thư mục và cắt 2 ảnh theo yêu cầu của bài

```python
dudu_changed = dudu[:, :, ::-1]
duahau_changed = duahau[:, :, ::-1]
```
Đảo kênh màu RGB thành BGR (đổi màu ảnh)

```python
plt.subplot(1, 2, 1)
plt.imshow(dudu_changed)

plt.subplot(1, 2, 2)
plt.imshow(duahau_changed)

plt.show()
```

Hiển thị 2 ảnh kết quả cạnh nhau bằng ```subplot```

# BT3:
```python
import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt
```
Các thư viện được sử dụng trong bài này

```python
data = iio.imread('exercise/quang_ninh.jpg')
nui = data[25:330, 445:655]
thuyen = data[455:545, 490:655]
```
lấy ảnh từ thư mục và cắt 2 ảnh theo yêu cầu của bài

```python
nui_xoay = nd.rotate(nui, 45, reshape = True)
thuyen_xoay = nd.rotate(thuyen, 45, reshape = True)
```
xoay ảnh bằng ```rotate```  góc 45 độ
```reshape=True``` giúp ảnh xoay không bị cắt góc, nhưng sẽ làm kích thước thay đổi.

```python
plt.imsave('nui_xoay.jpg',nui_xoay)
plt.imsave('thuyen.jpg',thuyen_xoay)
```

Lưu ảnh đã thay đổi vào máy

```python
plt.subplot(1, 2, 1)
plt.imshow(nui_xoay)

plt.subplot(1, 2, 2)
plt.imshow(thuyen_xoay)

plt.show()
```

Hiển thị 2 ảnh kết quả cạnh nhau bằng ```subplot```

# BT4:
```python
import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pylab as plt
```
Các thư viện được sử dụng trong bài này

```python
data = iio.imread('exercise/pagoda.jpg')
chua = data[125:320, 0:570]
```
lấy ảnh từ thư mục và cắt ảnh theo yêu cầu của bài

```python
chua_zoom = nd.zoom(chua, (5,5,1))
```
phóng to hình lên 5 lần

```python
plt.imsave('chua_zoom.jpg', chua_zoom)
```

Lưu ảnh đã thay đổi vào máy

```python
plt.subplot(1,2,1)
plt.imshow(chua)

plt.subplot(1,2,2)
plt.imshow(chua_zoom)

plt.show()
```

Hiển thị 2 ảnh kết quả trước và sau cạnh nhau bằng ```subplot```

# BT5:
```python
import numpy as np
import scipy.ndimage as nd
import imageio.v2 as iio
import matplotlib.pyplot as plt
import os
```
Các thư viện được sử dụng trong bài này

```python
img_folder = "exercise"
image_files = ["colorful-ripe-tropical-fruits.jpg", "pagoda.jpg", "quang_ninh.jpg"]
```
tạo biến của thư mục ```exercise``` và ép 3 ảnh trong thư mục vào mảng

```python
print("Chọn thao tác:")
print("T - Tịnh tiến")
print("X - Xoay")
print("P - Phóng to")
print("H - Thu nhỏ")
print("C - Coordinate Map")
```
in ra màn hình các lực chọn trong menu

```python
choice = input("Nhập lựa chọn (T/X/P/H/C): ").upper()
```

lấy kết quả nhập từ bàn phím bằng ```input``` sao đó ép kiểu in hoa bằng ```upper```


```python
if choice not in ['T', 'X', 'P', 'H', 'C']:
    print("Lựa chọn không hợp lệ.")
    exit()
```

Nếu kết quả nhập từ bàn phím không phải 1 trong các ký tự ```['T', 'X', 'P', 'H', 'C']``` thì hiện thông báo ra màn hình và kết thúc

```python
print("Chọn ảnh (1, 2 hoặc 3):")
img_index = int(input("Nhập số: ")) - 1
```
in thông báo chọn ảnh ra màn hình
```img_index = int(input("Nhập số: ")) - 1```  nhập 1 số từ bàn phím và ```img_index``` sẽ nhận kết quả nhận kết quả trừ 1 ```VD: nhập: 4 -> kết quả: 3 ``

```python
if img_index not in [0, 1, 2]:
    print("Số ảnh không hợp lệ.")
    exit()
```

Nếu Kết quả nhập từ bàn phím không nằm trong mảng```[0, 1, 2]``` thì in thông báo ra màn hình và kết thúc

```python
img_path = os.path.join(img_folder, image_files[img_index])
img = iio.imread(img_path)
```

```os.path.join(...)``` hàm lấy đường dận của thư viện os trong python 
```img_folder``` biến chứa thư mục được chọn
```image_files``` mảng chứa hình 
```[img_index]``` hình được người dùng chọn

sau đó đọc và lấy ảnh từ đường dẫn trên bằng ```iio.imread(img_path)```

```python
if choice == 'T':
    result = nd.shift(img, (0, 30, 0)) 
elif choice == 'X':
    result = nd.rotate(img, 45, reshape=True)
elif choice == 'P':
    result = nd.zoom(img, (5, 5, 1)) 
elif choice == 'H':
    result = nd.zoom(img, (1/5, 1/5, 1)) 
```

Nếu ký tự được nhập từ bàn phím giống với ký tự của công việc nào thì sẽ thực hiện công việc đó đối với ảnh được chọn:
- ```T```: Tịnh tiến ảnh sang ngang 30 pixel
- ```X```: xoay ảnh 45 độ
- ```P```: phóng to ảnh 5 lần
- ```H```: thu nhỏ ảnh 5 lần

```python
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
```

Nếu ký tự nhập từ bàn phím là ```C``` thì thực hiện việc này
- ```H, W, C = img.shape```: gán shape của ảnh ```img``` vào các biến
- ```M = np.indices((H, W))```: Tạo một mảng ```M``` chứa toàn bộ tọa độ gốc của ảnh.
```python
  d = 5
  q = 2 * d * np.random.rand(*M.shape) - d
```
- Tạo nhiễu ngẫu nhiên ```q``` có giá trị nằm trong khoảng ```[-5, 5]```

```python
   mp = (M + q).astype(int)
```
- ```mp``` là bản đồ tọa độ mới sau khi cộng thêm nhiễu.
- Sau đó ép kiểu về int vì chỉ số ảnh phải là số nguyên. 

```python
mp[0] = np.clip(mp[0], 0, H - 1)
mp[1] = np.clip(mp[1], 0, W - 1)
```
- Đảm bảo các tọa độ mới không bị ra ngoài ảnh bằng cách giới hạn lại

```python
result = np.zeros_like(img)
for i in range(C): 
    result[:, :, i] = data[mp[0], mp[1], i]
```
- Lấy pixel từ ```img``` theo tọa độ mới trong ```mp``` rồi gán sang ảnh mới.
- Làm lần lượt cho từng kênh màu (R, G, B).

```python
plt.subplot(1, 2, 1)
plt.title("Ảnh Gốc")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title("Ảnh Sau Biến Đổi")
plt.imshow(result)

plt.show()
```

Hiển thị 2 ảnh kết quả trước và sau cạnh nhau bằng ```subplot```
