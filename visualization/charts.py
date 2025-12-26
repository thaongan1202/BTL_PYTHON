import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_all_charts(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_context("talk") 

    #Bieu do 1: Top 10 The loai nhac
    plt.figure(figsize=(12, 7))
    genre_data = df['genre'].value_counts().head(10)
    
    bars = plt.bar(genre_data.index, genre_data.values, color=plt.cm.Paired(range(10)), edgecolor='black')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontweight='bold')

    plt.title('Top 10 Thể loại nhạc chiếm ưu thế năm 2025', fontsize=16, pad=20)
    plt.xlabel('Thể loại (Genre)', fontsize=12)
    plt.ylabel('Số lượng bài hát', fontsize=12)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('1_top_genres_bar.png')
    plt.close()

    #bieu do 2: Cơ cấu nội dung âm nhạc (Explicit vs Clean)
    plt.figure(figsize=(8, 8))
    explicit_counts = df['explicit'].value_counts()
    
    plt.pie(explicit_counts, 
            labels=['Nhạc sạch (Clean)', 'Nhạc dán nhãn (Explicit)'], 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=['#72bcd4', '#ff7f7f'], 
            explode=(0, 0.1), # Làm nổi bật phần nhạc Explicit
            shadow=True,
            textprops={'fontsize': 14, 'fontweight': 'bold'})
    
    plt.title('Cơ cấu nội dung âm nhạc trên Spotify 2025', fontsize=16)
    plt.savefig('2_explicit_pie.png')
    plt.close()

    #bieu do 3: Xu hướng phát hành bài hát theo thời gian
    plt.figure(figsize=(12, 6))
    # Nhóm dữ liệu theo tháng
    df['month'] = df['release_date'].dt.to_period('M')
    trend = df.groupby('month').size()
    trend.index = trend.index.to_timestamp()
    
    plt.plot(trend.index, trend.values, color='#2ecc71', marker='o', linewidth=3, markersize=8, label='Số bài hát mới')
    plt.fill_between(trend.index, trend.values, color='#2ecc71', alpha=0.1) # Thêm mảng màu cho đẹp
    
    plt.title('Biến động số lượng bài hát phát hành trong năm 2025', fontsize=16)
    plt.xlabel('Thời gian', fontsize=12)
    plt.ylabel('Số lượng bài hát', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('3_release_trend_line.png')
    plt.close()

   #bieu do 4: Scatter plot Energy vs Danceability
    plt.figure(figsize=(12, 8))
    
    scatter = plt.scatter(df['energy'], df['danceability'], 
                         c=df['popularity'], cmap='viridis', 
                         alpha=0.2, s=15, edgecolors='none')
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Mức độ phổ biến (Popularity)', fontsize=12)

    plt.axvline(x=0.5, color='red', linestyle='--', alpha=0.5) # Đường chia năng lượng
    plt.axhline(y=0.5, color='red', linestyle='--', alpha=0.5) # Đường chia độ nhảy
    
    # Thêm nhãn cho 4 vùng để dễ báo cáo
    plt.text(0.1, 0.9, 'Trầm lắng - Dễ nhảy', color='darkred', fontsize=12, fontweight='bold', alpha=0.7)
    plt.text(0.7, 0.9, 'Sôi động - Dễ nhảy (Hits)', color='darkred', fontsize=12, fontweight='bold', alpha=0.7)
    plt.text(0.1, 0.1, 'Buồn / Classical', color='darkred', fontsize=12, fontweight='bold', alpha=0.7)
    plt.text(0.7, 0.1, 'Năng lượng cao / Khó nhảy', color='darkred', fontsize=12, fontweight='bold', alpha=0.7)

    plt.title('Tương quan giữa Năng lượng và Khả năng khiêu vũ (2025)', fontsize=16)
    plt.xlabel('Energy (Năng lượng) --->', fontsize=12)
    plt.ylabel('Danceability (Độ nhảy được) --->', fontsize=12)
    plt.tight_layout()
    plt.savefig('4_energy_dance_scatter.png')
    plt.close()

    print("Đã tạo và lưu tất cả biểu đồ trực quan hóa thành công!")

    