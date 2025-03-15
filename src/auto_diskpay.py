import subprocess

# Đảm bảo đường dẫn tới tệp shell chính xác
shell_script_path = './array.sh'
def auto_array():
    try:
        # Chạy shell script
        result = subprocess.run([shell_script_path], check=True, text=True, capture_output=True)
        
        # In kết quả
        print("Kết quả đầu ra:", result.stdout)
        print("Kết quả lỗi:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Đã xảy ra lỗi khi chạy shell script: {e}")
    except FileNotFoundError:
        print(f"Tệp {shell_script_path} không tìm thấy!")
