import pandas as pd

def clean_data(df):
    """Làm sạch dữ liệu """
    
    print("Bắt đầu quá trình làm sạch dữ liệu")

    #1.KIỂM TRA TỔNG QUÁT: Kiểm tra các giá trị trống trong từng cột
    missing_info = df.isnull().sum()
    print("Số lượng ô trống trong từng cột:")
    print(missing_info[missing_info > 0]) # Chỉ in ra những cột có lỗi

    #2.XỬ LÝ TRÙNG LẶP: Tự động kiểm tra dựa trên ID duy nhất
    duplicate_count = df.duplicated(subset=['track_id']).sum()
    if duplicate_count > 0:
        print(f"Phát hiện {duplicate_count} dòng trùng lặp. Đang tiến hành xóa...")
        df.drop_duplicates(subset=['track_id'], keep='first', inplace=True)

    #3.XỬ LÝ GIÁ TRỊ THIẾU 
    
    # Xoá các dòng có giá trị thiếu ở các cột quan trọng
    critical_cols = ['track_id', 'track_name', 'artist_name']
    df.dropna(subset=critical_cols, inplace=True)

    # Điền giá trị mặc định cho các cột text và số
    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(0)

    print("Hoàn thành làm sạch dữ liệu")
    return df