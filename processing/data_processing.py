import pandas as pd
import numpy as np

# 1. Đọc dữ liệu từ file bạn đã cung cấp
df = pd.read_csv('spotify_2025.csv')

# --- CHUẨN HÓA DỮ LIỆU (DATA PROCESSING) ---
# Chuyển đổi ngày tháng sang định dạng chuẩn YYYY-MM-DD
df['release_date'] = pd.to_datetime(df['release_date'])

# Chuyển đổi miliseconds sang seconds cho dễ quản lý
df['duration_sec'] = df['duration_ms'] / 1000

# Xử lý các giá trị thiếu ở cột album_name (nếu có)
df['album_name'] = df['album_name'].fillna('Unknown')

# --- TÍNH TOÁN THỐNG KÊ (NUMPY & PANDAS) ---
# Lọc ra các cột số quan trọng
numeric_cols = ['popularity', 'danceability', 'energy', 'stream_count']

# Tính Mean bằng NumPy
mean_values = {col: np.mean(df[col]) for col in numeric_cols}

# Tính Median bằng Pandas
median_values = df[numeric_cols].median()

# --- XUẤT KẾT QUẢ ---
print("--- CHỈ SỐ THỐNG KÊ SPOTIFY 2025 ---")
for col in numeric_cols:
    print(f"Thuộc tính: {col.upper()}")
    print(f"  - Mean (Trung bình): {mean_values[col]:.2f}")
    print(f"  - Median (Trung vị): {median_values[col]:.2f}")
    print("-" * 30)

# Lưu lại file đã chuẩn hóa để push lên nhánh mới trên GitHub
df.to_csv('spotify_2025_processed.csv', index=False)