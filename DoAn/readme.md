# Giải thích code 

# Công nghệ sử dụng
- Python 3.x
- Tkinter: giao diện đồ họa.
- OpenCV (cv2): xử lý ảnh.
- PIL (Pillow): hiển thị ảnh trong Tkinter.

# Tính Năng Chính

| Nút chức năng        | Mô tả                                                                 |
|----------------------|-----------------------------------------------------------------------|
|  **Nhập ảnh**        | Chọn ảnh từ máy tính và hiển thị ảnh lên giao diện.                  |
|  **Làm rõ ảnh**       | Áp dụng bộ lọc sharpen để làm sắc nét ảnh.                          |
|  **Xử lý nhiễu**     | Khử nhiễu màu sử dụng `cv2.fastNlMeansDenoisingColored`.             |
|  **Quay lại ảnh gốc** | Phục hồi ảnh về trạng thái ban đầu.                                 |
|  **Xóa ảnh**         | Xóa ảnh khỏi giao diện hiển thị và bộ nhớ.                          |

---

