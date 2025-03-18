#sudo pip install base  

import os
import time
import threading
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


app = Flask(__name__)
chrome_driver_path = r"/home/zik/Documents/auto/chromedriver"

# File lưu danh sách profile
profile_file = "profiles.txt"

def create_profiles():
    while True:
        try:
            chose = int(input("Nhập số lượng profile (tối thiểu 2): "))
            if chose < 2:
                print("⚠️ Bạn phải nhập số lớn hơn hoặc bằng 2!")
                continue
            break
        except ValueError:
            print("⚠️ Vui lòng nhập số hợp lệ!")
    profiles = []
    for i in range(1, chose + 1):  # Tạo 5 profile
        profile_path = f"profile_chrome/profile_{i}"
        os.makedirs(profile_path, exist_ok=True)  # Tạo thư mục nếu chưa có

        # Lưu vào danh sách
        profiles.append(profile_path)

        # Cấu hình ChromeOptions
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--user-data-dir={profile_path}")

        # Khởi tạo WebDriver
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Mở trình duyệt
        driver.get('https://www.google.com')

        # Chờ 5 giây rồi đóng (hoặc bỏ dòng này nếu muốn giữ trình duyệt mở)
        time.sleep(5)
        driver.quit()

    # Lưu danh sách profile vào file
    with open(profile_file, "w") as f:
        for profile in profiles:
            f.write(profile + "\n")

    print("✅ Đã tạo xong profile và lưu vào profiles.txt")


@app.route("/create_profiles", methods=["POST"])
def api_create_profiles():
    """API tạo profile từ xa"""
    data = request.json
    num_profiles = data.get("num_profiles", 2)
    threading.Thread(target=create_profiles, args=(num_profiles,)).start()
    return jsonify({"message": f"Đang tạo {num_profiles} profile..."}), 202

def start_api():
    """Chạy Flask API"""
    app.run(host="0.0.0.0", port=5000, debug=False)

if __name__ == "__main__":
    # Chạy API trên một luồng riêng
    #api_thread = threading.Thread(target=start_api)
    #api_thread.start()

    # Khởi tạo profile ngay khi script chạy
    create_profiles()