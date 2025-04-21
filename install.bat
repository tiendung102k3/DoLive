@echo off
echo 🚀 Đang cài thư viện Python...
pip install -r requirements.txt
pip install yt-dlp

echo ⚠️ Nhớ cài ffmpeg và thêm vào PATH nhé!
echo Link: https://ffmpeg.org/download.html

echo ✅ Cài xong rồi! Đang chạy tool...
python app.py
pause
