import pandas as pd

def from_csv(file_path):
    """Đọc dữ liệu từ file CSV """
    try:
        df = pd.read_csv(file_path)
        print("Nạp dữ liệu thành công!")
        return df
    except Exception as e:
        print(f"Lỗi khi nạp dữ liệu: {e}")
        return None