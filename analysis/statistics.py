import pandas as pd

def get_top_artists(df, n=10):
    """Tìm Top n nghệ sĩ có tổng lượt stream cao nhất"""
    top_artists = df.groupby('artist_name')['stream_count'].sum().sort_values(ascending=False).head(n)
    return top_artists

def get_summary_stats(df):
    """Tính toán các chỉ số trung bình để ghi vào báo cáo"""
    # Trả về trung bình các đặc tính âm thanh quan trọng
    return df[['popularity', 'danceability', 'energy', 'tempo']].mean()

def count_by_country(df):
    """Thống kê số lượng bài hát theo quốc gia"""
    return df['country'].value_counts().head(5)