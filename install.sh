#!/bin/bash
echo "🚀 Đang cập nhật hệ thống..."
pkg update -y && pkg upgrade -y
pkg install ffmpeg -y
pkg install yt-dlp -y
pkg install python -y

echo "📦 Đang cài thư viện Python..."
pip install -r requirements.txt

echo "✅ Hoàn tất! Đang chạy tool..."
python app.py
