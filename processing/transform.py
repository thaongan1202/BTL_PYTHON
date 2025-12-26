import pandas as pd
import numpy as np

def transform_spotify_data(df):
    """Thực hiện chuẩn hóa và biến đổi dữ liệu"""
    print("Bắt đầu quá trình chuẩn hóa và biến đổi")

    # 1. CHUẨN HÓA DỮ LIỆU (Data Standardization)

    #Chuẩn hóa định dạng ngày tháng: Chuyển cột release_date về định dạng datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    
    #Chuẩn hóa tên thể loại (genre) về chữ hoa chữ thường
    df['genre'] = df['genre'].str.title()

    # 2. CHUYỂN ĐỔI ĐƠN VỊ 
    
    # Chuyển đổi độ dài bài hát từ milliseconds sang phút, làm tròn đến 2 chữ số thập phân
    df['duration_min'] = np.round(df['duration_ms'] / 60000, 2)

    # 3. TẠO CÁC BIẾN MỚI 
    # Tạo biến mới popularity_rank dựa trên giá trị popularity
    conditions = [
        (df['popularity'] >= 80),
        (df['popularity'] >= 50) & (df['popularity'] < 80),
        (df['popularity'] < 50)
    ]
    choices = ['Top Hit', 'Popular', 'Rising']
    df['popularity_rank'] = np.select(conditions, choices, default='Unknown')

    # Tạo biến log_stream_count để giảm thiểu độ lệch của dữ liệu stream_count
    df['stream_log'] = np.log1p(df['stream_count'])

    print("Hoàn thành chuẩn hóa dữ liệu.")
    return df