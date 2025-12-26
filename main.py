from processing.load_data import from_csv
from processing.cleaning import clean_data
from processing.transform import transform_spotify_data
from analysis.statistics import get_top_artists, get_summary_stats
from visualization.charts import plot_all_charts

def main():
    print("=== CHƯƠNG TRÌNH PHÂN TÍCH DỮ LIỆU SPOTIFY 2025 ===")
    
    # Bước 1: Nạp dữ liệu
    file_path = 'data/spotify_2025.csv'
    df = from_csv(file_path)
    
    if df is None:
        return

    processed_df = None

    while True:
        print("\n--- MENU CHỨC NĂNG ---")
        print("1. Xem dữ liệu thô (Trước khi xử lý)")
        print("2. Thực hiện làm sạch và chuẩn hóa dữ liệu")
        print("3. Phân tích thống kê ")
        print("4. Xuất các biểu đồ trực quan hóa (Matplotlib)")
        print("5. Thoát")
        
        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            print("\n[Dữ liệu thô]")
            print(df.info())
            print(df.head())
            print("\nCác ô trống tìm thấy:")
            print(df.isnull().sum())

        elif choice == '2':
            # Thực hiện các bước xử lý dữ liệu [cite: 17, 18]
            print("\nĐang tiến hành xử lý...")
            cleaned_df = clean_data(df.copy()) # Làm sạch [cite: 20]
            processed_df = transform_spotify_data(cleaned_df) # Chuẩn hóa [cite: 21]
            print("Xử lý hoàn tất! Dữ liệu đã sạch và sẵn sàng.")

        elif choice == '3':
            if processed_df is not None:
                print("\n=== KẾT QUẢ PHÂN TÍCH LOGIC ===")
                # Gọi các hàm từ module analysis/statistics.py
                top_artists = get_top_artists(processed_df)
                avg_stats = get_summary_stats(processed_df)
                
                print("\n1. Top 10 nghệ sĩ có tổng lượt stream khủng nhất:")
                print(top_artists)
                
                print(f"\n2. Chỉ số âm nhạc trung bình của năm 2025:")
                print(f"- Độ nhảy được (Danceability): {avg_stats['danceability']:.2f}")
                print(f"- Năng lượng (Energy): {avg_stats['energy']:.2f}")
                print(f"- Nhịp độ trung bình (Tempo): {avg_stats['tempo']:.1f} BPM")
                
                print("\n3. Nhận xét sơ bộ:")
                if avg_stats['energy'] > 0.6:
                    print("=> Xu hướng nhạc năm 2025 rất sôi động và mạnh mẽ.")
                else:
                    print("=> Xu hướng nhạc năm 2025 thiên về sự nhẹ nhàng, chill-out.")
            else:
                print("Lỗi: Bạn cần chạy chức năng 2 để xử lý dữ liệu trước!")

        elif choice == '4':
            if processed_df is not None:
                print("\nĐang khởi tạo các biểu đồ trực quan hóa[cite: 23]...")
                plot_all_charts(processed_df) # Vẽ đa dạng các loại biểu đồ 
                print("Đã lưu các file biểu đồ (.png) vào thư mục gốc.")
            else:
                print("Vui lòng chọn chức năng 2 để xử lý dữ liệu trước!")

        elif choice == '5':
            print("Kết thúc chương trình. ")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()