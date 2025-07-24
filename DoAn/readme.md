# Giải thích code 

# Công nghệ sử dụng
- `Python`
- `Tkinter`: giao diện đồ họa.
- `OpenCV (cv2)`: xử lý ảnh.
- `PIL (Pillow)`: hiển thị ảnh trong Tkinter.

# Tính Năng Chính

| Nút chức năng        | Mô tả                                                                 |
|----------------------|-----------------------------------------------------------------------|
|  **Nhập ảnh**        | Chọn ảnh từ máy tính và hiển thị ảnh lên giao diện.                  |
|  **Làm rõ ảnh**       | Áp dụng bộ lọc sharpen để làm sắc nét ảnh.                          |
|  **Xử lý nhiễu**     | Khử nhiễu màu sử dụng `cv2.fastNlMeansDenoisingColored`.             |
|  **Quay lại ảnh gốc** | Phục hồi ảnh về trạng thái ban đầu.                                 |
|  **Xóa ảnh**         | Xóa ảnh khỏi giao diện hiển thị và bộ nhớ.                          |

---

# Giải thích code
### Tạo lớp chính

```python
class ImageProcessorApp:
    def __init__(self, root):
```
- Đây là constructor khởi tạo giao diện và các biến ảnh cần thiết.
- 
### Tạo cửa sổ ứng dụng
```python
        self.root = root
        self.root.title("Xử lý ảnh đơn giản")
        self.root.geometry("800x600")
```
- Đặt tiêu đề và kích thước cửa sổ chính.
  
### Khởi tạo các biến lưu ảnh
```python
        self.original_image = None   # ảnh gốc
        self.processed_image = None  # ảnh sau khi xử lý
        self.display_image = None    # ảnh hiển thị trên canvas
```

### Tạo vùng hiển thị ảnh
```python
        # Khung hiển thị ảnh
        self.canvas = tk.Canvas(root, width=600, height=400, bg='gray')
        self.canvas.pack(pady=10)
```
- Vùng Canvas để vẽ/hiển thị ảnh lên giao diện.

### Tạo các nút điều khiển
```python
        # Các nút chức năng
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="nhập ảnh", command=self.load_image).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Làm rõ ảnh", command=self.sharpen_image).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Xử lý nhiễu", command=self.denoise_image).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Quay lại ảnh gốc", command=self.restore_image).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Xóa ảnh", command=self.clear_image).grid(row=0, column=4, padx=5)
```
- Tạo khung chứa các nút bấm.
- Mỗi nút gán với một hàm xử lý tương ứng.
  
### Hàm `load_image()` – nhập ảnh
```python
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            image = cv2.imread(file_path)
            self.original_image = image.copy()
            self.processed_image = image.copy()
            self.display_image_on_canvas(image)
```
- Mở hộp thoại chọn ảnh.
- Dùng cv2.imread() để đọc ảnh gốc.
- Lưu bản sao ảnh vào biến original_image và processed_image.
- Gọi hàm display_image_on_canvas() để hiển thị ảnh.

### Hàm `display_image_on_canvas()` – hiển thị ảnh
```python
    def display_image_on_canvas(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image.thumbnail((600, 400))  # Resize nhỏ gọn
        self.display_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(300, 200, image=self.display_image)
```
|Bước                 |	Mô tả
|---------------------|----------------------------------------------------------|
|`cv2.cvtColor`	      | Chuyển ảnh BGR (OpenCV) sang RGB (Tkinter).              |
|`Image.fromarray`	  | Chuyển NumPy array thành ảnh PIL.                        |
|`thumbnail()`	      | Resize ảnh để vừa vùng canvas.                           | 
|`ImageTk.PhotoImage`	| Chuyển ảnh thành đối tượng có thể hiển thị trong Tkinter.|
|`create_image`       |	Vẽ ảnh lên vùng canvas (tọa độ giữa là 300, 200).        |

### Hàm `sharpen_image()` – làm rõ ảnh
```python
    def sharpen_image(self):
        if self.processed_image is not None:
            kernel = np.array([[0, -1, 0],
                               [-1, 5,-1],
                               [0, -1, 0]])
            sharpened = cv2.filter2D(self.processed_image, -1, kernel)
            self.processed_image = sharpened
            self.display_image_on_canvas(sharpened)
```
- Áp dụng kernel lọc sắc nét (sharpen).
- Dùng `cv2.filter2D()` để làm rõ.
- Cập nhật `processed_image` và hiển thị lại.

### Hàm `denoise_image()` – khử nhiễu
```python
    def denoise_image(self):
        if self.processed_image is not None:
            denoised = cv2.fastNlMeansDenoisingColored(self.processed_image, None, 10, 10, 7, 21)
            self.processed_image = denoised
            self.display_image_on_canvas(denoised)
```
- Dùng thuật toán khử nhiễu nâng cao của OpenCV cho ảnh màu.
  
### Hàm `restore_image()` – khôi phục ảnh gốc
```python
    def restore_image(self):
        if self.original_image is not None:
            self.processed_image = self.original_image.copy()
            self.display_image_on_canvas(self.original_image)
```
- Khôi phục lại ảnh gốc ban đầu.

### Hàm `clear_image()` – xóa ảnh
```python
    def clear_image(self):
        self.original_image = None
        self.processed_image = None
        self.canvas.delete("all")
```
- Xóa ảnh khỏi canvas và đặt các biến ảnh về `None`.

### Khởi chạy ứng dụng
```python
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
```
- Tạo cửa sổ chính `Tkinter`.
- Gọi lớp `ImageProcessorApp` để khởi tạo giao diện.
- Gọi `mainloop()` để chạy giao diện liên tục cho đến khi đóng.
