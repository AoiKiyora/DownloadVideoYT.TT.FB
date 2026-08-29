import sys
import subprocess
import os

if os.path.exists('requirements.txt'):
    try:
        import yt_dlp
    except ImportError:
        print("Đang tự động cài đặt các thư viện cần thiết...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        import yt_dlp
        print("✅ Cài đặt hoàn tất!\n")

print("\033[1mCHÀO MỪNG BẠN DOWNLOAD VIDEO CODE THUỘC BẢN QUYỂN CỦA AOI KIYORA\033[0m\n")

def ydl_download(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'outtmpl': '~/Downloads/%(title)s.%(ext)s',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        },
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("✅ Đã tải xong! Video được lưu trong thư mục Downloads.\n")

# Bắt đầu vòng lặp ở đây, đưa toàn bộ menu vào trong để có thể lặp lại
while True:
    print("\033[1mMỜI BẠN CHỌN NỀN TẢNG DOWNLOAD: \033[0m")
    print("1. Download video YouTube")
    print("2. Download video Facebook")
    print("3. Download video TikTok")
    print("4. Download video X")
    print("5. Thoát chương trình")
    
    a = input("Nhập lựa chọn của bạn: ")

    try:
        if a == "1":
            url = input("Nhập link YouTube (Để trống để quay lại): ")
            if url == "":
                print("🔄 Đang quay lại menu...\n")
                continue
            if "youtube.com" not in url and "youtu.be" not in url:
                print("⚠️ Link không hợp lệ. Vui lòng nhập link YouTube hợp lệ.\n")
                continue
            ydl_download(url)
            
        elif a == "2":
            url = input("Nhập link Facebook (Để trống để quay lại): ")
            if url == "":
                print("🔄 Đang quay lại menu...\n")
                continue
            if "facebook.com" not in url:
                print("⚠️ Link không hợp lệ. Vui lòng nhập link Facebook hợp lệ.\n")
                continue
            ydl_download(url)
            
        elif a == "3":
            url = input("Nhập link TikTok (Để trống để quay lại): ")
            if url == "":
                print("🔄 Đang quay lại menu...\n")
                continue
            if "tiktok.com" not in url:
                print("⚠️ Link không hợp lệ. Vui lòng nhập link TikTok hợp lệ.\n")
                continue
            ydl_download(url)

        elif a == "4":
            url = input("Nhập link X (Để trống để quay lại): ")
            if url == "":
                print("🔄 Đang quay lại menu...\n")
                continue
            if "x.com" not in url:
                print("⚠️ Link không hợp lệ. Vui lòng nhập link X hợp lệ.\n")
                continue
            ydl_download(url)

        elif a == "5":
            print("👋 Cảm ơn bạn đã sử dụng tool của Aoi Kiyora. Tạm biệt!")
            break
            
        else:
            print("⚠️ Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.\n")
            
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi: {e}. Vui lòng thử lại.\n")
