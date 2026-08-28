# Hướng dẫn cài đặt và sử dụng công cụ

Hướng dẫn chi tiết các bước cài đặt **FFmpeg** và chạy script Python để sử dụng công cụ một cách thuận tiện nhất.

---

## 1. Tải và cài đặt FFmpeg

FFmpeg là thư viện xử lý đa phương tiện bắt buộc cần có trên hệ thống để script có thể hoạt động chính xác.

Mở **PowerShell** hoặc **Command Prompt** với quyền **Administrator (Quản trị viên)** và chạy lệnh tương ứng với hệ điều hành của bạn:

### 🪟 Windows
```powershell
winget install --id=Gyan.FFmpeg -e
```
*(Nếu máy chưa có winget, bạn có thể tải thủ công từ trang chủ FFmpeg hoặc cài đặt qua Chocolatey: `choco install ffmpeg`)*

### 🍎 macOS
Sử dụng trình quản lý gói [Homebrew](https://brew.sh/):
```bash
brew install ffmpeg
```

### 🐧 Linux (Ubuntu / Debian)
```bash
sudo apt update && sudo apt install ffmpeg
```

---

## 2. Chạy file Python

Sau khi đã tải và giải nén thư mục chứa mã nguồn của công cụ:

1. Mở thư mục chứa file **`download.py`** trong File Explorer.
2. Click chuột vào thanh hiển thị đường dẫn thư mục (Address Bar) ở phía trên cùng.
3. Gõ chữ **`cmd`** rồi nhấn **Enter** để mở nhanh cửa sổ Command Prompt tại đúng thư mục đó.
4. Chạy lệnh sau để khởi động chương trình:
   ```bash
   python download.py
   ```

---
*Chúc bạn sử dụng công cụ thành công! Nếu gặp lỗi, hãy kiểm tra lại xem Python và FFmpeg đã được thêm vào biến môi trường (Environment Variables) hay chưa.*
