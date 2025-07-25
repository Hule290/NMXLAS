# Ứng dụng xử lý ảnh

# Công nghệ sử dụng
- `Python`: Ngôn ngữ lập trình
- `Tkinter`: giao diện đồ họa.
- `OpenCV (cv2)`: xử lý ảnh.
- `PIL (Pillow)`: hiển thị ảnh trong Tkinter.
- `Numpy`: hỗ trợ tạo kernel xử lý ảnh

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

### Khởi tạo lớp giao diện

```python
class ImageProcessorApp:
    def __init__(self, root):
```
- Tạo lớp giao diện chính `ImageProcessorApp` nhận vào cửa sổ Tkinter (`root`).

### Khởi tạo giao diện
```python
        self.root = root
        self.root.title("Xử lý ảnh đơn giản")
        self.root.geometry("1200x600")
```
- Đặt tiêu đề và kích thước cửa sổ chính.
  
### Khởi tạo các biến lưu ảnh
```python
        self.original_image = None   # ảnh gốc
        self.processed_image = None  # ảnh sau khi xử lý
        self.display_image_original = None    # ảnh gốc hiển thị trên canvas
        self.display_image_processed = None   # ảnh sau khi xử lý hiển thị trên canvas

```

### Tạo vùng hiển thị ảnh
```python
        self.image_frame = tk.Frame(root)
        self.image_frame.pack(pady=10)
```
- Tạo một khung (`Frame`) chứa hai vùng hiển thị ảnh.

### Nhãn và canvas cho ảnh gốc
```python
        self.label_original = tk.Label(self.image_frame, text="Ảnh gốc", font=("Arial", 14))
        self.label_original.pack(side=tk.LEFT, padx=10)

        self.canvas_original = tk.Canvas(self.image_frame, width=500, height=400, bg='gray')
        self.canvas_original.pack(side=tk.LEFT, padx=10)
```
- Tạo nhãn và khung vẽ (`Canvas`) để hiển thị ảnh gốc.

### Khai báo canvas cho ảnh xử lý
```python
        self.canvas_processed = None
        self.label_processed = None
```

- Được tạo khi có ảnh xử lý, tránh chiếm không gian khi chưa dùng.


### Tạo các nút điều khiển
```python
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Nhập ảnh", command=self.load_image).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Làm rõ ảnh", command=self.sharpen_image).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Khử mờ", command=self.deblur_image).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Quay lại ảnh gốc", command=self.restore_image).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Xóa ảnh", command=self.clear_image).grid(row=0, column=4, padx=5)
```
- Tạo các nút điều khiển: nhập ảnh, làm rõ ảnh, khử mờ, Quay lại ảnh gốc, xóa ảnh.
- Mỗi nút gán với một hàm xử lý tương ứng.
  
### Hàm `load_image()` – nhập ảnh
```python
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            image = cv2.imread(file_path)
            if image is None:
                messagebox.showerror("Lỗi", "Không thể đọc được tệp ảnh. Vui lòng chọn tệp hợp lệ.")
                return
            self.original_image = image.copy()
            self.processed_image = image.copy()
            self.display_image_on_canvas()
```
- Mở hộp thoại chọn ảnh.
- Dùng `cv2.imread()` để đọc ảnh gốc.
- Lưu bản sao ảnh vào biến `original_image` và `processed_image`.
- Gọi hàm `display_image_on_canvas()` để hiển thị ảnh.

### Hàm `display_image_on_canvas()` – hiển thị ảnh
```python
    def display_image_on_canvas(self):
        # Hiển thị ảnh gốc
        if self.original_image is not None:
            if len(self.original_image.shape) == 3 and self.original_image.shape[2] == 3:
                image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            else:
                image = self.original_image
            image = Image.fromarray(image)
            image.thumbnail((500, 400))
            self.display_image_original = ImageTk.PhotoImage(image)
            self.canvas_original.create_image(250, 200, image=self.display_image_original)

        # Hiển thị ảnh xử lý nếu khung xử lý tồn tại
        if self.canvas_processed and self.processed_image is not None:
            if len(self.processed_image.shape) == 3 and self.processed_image.shape[2] == 3:
                image = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2RGB)
            else:
                image = self.processed_image
            image = Image.fromarray(image)
            image.thumbnail((500, 400))
            self.display_image_processed = ImageTk.PhotoImage(image)
            self.canvas_processed.create_image(250, 200, image=self.display_image_processed)
```
|Bước                 |	Mô tả
|---------------------|----------------------------------------------------------|
|`cv2.cvtColor`	      | Chuyển ảnh BGR (OpenCV) sang RGB (Tkinter).              |
|`Image.fromarray`	  | Chuyển NumPy array thành ảnh PIL.                        |
|`thumbnail()`	      | Resize ảnh để vừa vùng canvas.                           | 
|`ImageTk.PhotoImage` | Chuyển ảnh thành đối tượng có thể hiển thị trong Tkinter.|
|`create_image`       |	Vẽ ảnh lên vùng canvas (tọa độ giữa là 250, 200).        |

### Hàm `create_processed_canvas()` – tạo khung xử lý ảnh
```python
    def create_processed_canvas(self):
        if not self.canvas_processed:
            # Thêm nhãn "Ảnh đã xử lý" phía trên canvas
            self.label_processed = tk.Label(self.image_frame, text="Ảnh đã xử lý", font=("Arial", 14))
            self.label_processed.pack(side=tk.LEFT, padx=10)
            
            self.canvas_processed = tk.Canvas(self.image_frame, width=500, height=400, bg='gray')
            self.canvas_processed.pack(side=tk.LEFT, padx=10)
```
- Tạo canvas và nhãn cho ảnh đã xử lý nếu chưa tồn tại.
  
### Hàm `sharpen_image()` – làm rõ ảnh
```python
    def sharpen_image(self):
        if self.processed_image is not None:
            if len(self.processed_image.shape) != 3 or self.processed_image.shape[2] != 3:
                messagebox.showerror("Lỗi", "Ảnh phải là ảnh màu (RGB).")
                return
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            sharpened = cv2.filter2D(self.processed_image, -1, kernel)
            self.processed_image = sharpened
            self.create_processed_canvas()
            self.display_image_on_canvas()
        else:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý.")
```
- Áp dụng kernel lọc sắc nét (sharpen).
- Dùng `cv2.filter2D()` để làm rõ.
- Cập nhật `processed_image` và hiển thị lại.

### Hàm `deblur_image()` – khử mờ
```python
    def deblur_image(self):
        if self.processed_image is not None:
            if len(self.processed_image.shape) != 3 or self.processed_image.shape[2] != 3:
                messagebox.showerror("Lỗi", "Ảnh phải là ảnh màu (RGB).")
                return
            kernel = np.array([[-1, -1, -1],
                               [-1,  9, -1],
                               [-1, -1, -1]])
            deblurred = cv2.filter2D(self.processed_image, -1, kernel)
            self.processed_image = deblurred
            self.create_processed_canvas()
            self.display_image_on_canvas()
        else:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh để xử lý.")
```
- Kernel này tương tự sharpen nhưng mạnh hơn, dùng để giảm độ mờ trong ảnh.
  
### Hàm `restore_image()` – khôi phục ảnh gốc
```python
    def restore_image(self):
        if self.original_image is not None:
            self.processed_image = self.original_image.copy()
            if self.canvas_processed:
                self.canvas_processed.destroy()
                self.canvas_processed = None
                if self.label_processed:
                    self.label_processed.destroy()
                    self.label_processed = None
            self.display_image_on_canvas()
        else:
            messagebox.showwarning("Cảnh báo", "Không có ảnh gốc để khôi phục.")
```
- Khôi phục lại ảnh gốc ban đầu.
- Hủy canvas và nhãn của ảnh đã xử lý nếu tồn tại.

### Hàm `clear_image()` – xóa ảnh
```python
    def clear_image(self):
        if self.original_image is not None or self.processed_image is not None:
            self.original_image = None
            self.processed_image = None
            self.canvas_original.delete("all")
            if self.canvas_processed:
                self.canvas_processed.destroy()
                self.canvas_processed = None
                if self.label_processed:
                    self.label_processed.destroy()
                    self.label_processed = None
        else:
            messagebox.showwarning("Cảnh báo", "Không có ảnh để xóa.")

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
