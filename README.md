<h1 align="center">✨🎥 DoLive - Tool Livestream Đa Nền Tảng 🎥✨</h1>

<p align="center">
  Tự động livestream video từ link hoặc file video lên các nền tảng như Facebook, YouTube, TikTok hoặc bất kỳ server RTMP nào!  
</p>

---

## 🌟 Giới thiệu

**DoLive** là một tool livestream đơn giản nhưng mạnh mẽ, cho phép bạn:
- Phát video từ **file** hoặc **link YouTube/Facebook**
- Hỗ trợ đa nền tảng: **Facebook**, **YouTube**, **TikTok**, hoặc **RTMP tùy chỉnh**
- Bật tắt tính năng **lặp lại video**
- Giao diện web dễ sử dụng, hỗ trợ login bằng **key một lần/ngày**

> **Note:** Tool đang trong giai đoạn phát triển nên có thể còn lỗi nhỏ. Mong được mọi người thông cảm và góp ý thêm nhé!

---

## ⚙️ Yêu cầu hệ thống

### Python Packages:
- Flask
- requests
- moviepy
- pytube
- ffmpeg-python
- werkzeug

### System Packages:
- `ffmpeg`: Dùng để xử lý video và livestream
- `yt-dlp`: Dùng để tải video từ YouTube hoặc Facebook

---

## 🚀 Cài đặt

### 1. Clone project

```bash
git clone https://github.com/tiendung102k3/DoLive.git
cd DoLive


---

🐧 Cài đặt trên Termux (Android)

pkg update -y && pkg upgrade -y
pkg install python -y
pkg install ffmpeg -y
pkg install yt-dlp -y
pip install -r requirements.txt

✅ Cài nhanh:

chmod +x install.sh
./install.sh


---

🪟 Cài đặt trên Windows

Cài đặt thủ công:

1. Cài Python: https://www.python.org/downloads/


2. Tải và cài đặt ffmpeg: https://ffmpeg.org/download.html
(Giải nén và thêm thư mục bin/ vào biến môi trường PATH)


3. Cài thư viện Python:



pip install -r requirements.txt
pip install yt-dlp

✅ Cài nhanh:

Chạy file:

install.bat


---

▶️ Cách sử dụng

1. Chạy tool:

python app.py

2. Mở trình duyệt:

Truy cập: http://127.0.0.1:5000

3. Đăng nhập:

Nhập key trong ngày

Nếu chưa có, click vào link lấy key ngay trên trang login



---

🎛️ Chức năng chính


---

❗ Lưu ý

Tool không lưu key vĩnh viễn, key sẽ hết hạn sau 24h

Nếu video từ link không phát được, hãy thử dùng file để ổn định hơn

Hãy kiểm tra kỹ Stream Key và RTMP URL trước khi stream



---

🛠️ Troubleshooting

Nếu không chạy được ffmpeg, hãy kiểm tra xem đã thêm vào PATH chưa

Nếu không hiện trang web: đảm bảo app chạy không lỗi và cổng 5000 không bị chặn

Với video YouTube không chạy: hãy cập nhật yt-dlp bằng:


pip install -U yt-dlp


---

🤝 Hợp tác & Liên hệ

Bạn muốn đóng góp, chỉnh sửa hoặc phát triển thêm tính năng? Hãy inbox ngay nhé!

Zalo: 0766459014

Email: monstertattoovn696@gmail.com

Facebook: https://www.facebook.com/dungmoi2k3



---

<p align="center"><strong>Chúc bạn livestream thành công, mượt mà, và viral cháy máy nhé! 🔥</strong></p>
