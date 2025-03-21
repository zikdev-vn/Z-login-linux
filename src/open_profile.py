import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.chromeoptions_auto.chrome_options_auto import chromeoptions_auto
from concurrent.futures import ThreadPoolExecutor
from script_auto.gmail import gmail
from script_auto.createmetamask import create_metamask
from script_auto.cygnus import cygnus
#from login_gmail import open_profiles_with_gmails
import time
chrome_path = r"/opt/google/chrome/chrome"
#from auto_diskpay import arrange_windows

chrome_driver_path = r"/home/zik/Documents/auto/chromedriver"
profile_file = "data/profiles.txt"

def open_profiles():
    
    if not os.path.exists(profile_file):
        print("⚠️ Không tìm thấy file profiles.txt! Hãy tạo profile trước.")
        return

    # Đọc danh sách profile từ file
    with open(profile_file, "r") as f:
        profiles = [line.strip() for line in f.readlines()]

    if not profiles:
        print("⚠️ Không có profile nào để mở!")
        return

    # Hiển thị danh sách profile
    print("\n📂 Danh sách profile có sẵn:")
    for idx, profile in enumerate(profiles, start=1):
        print(f"{idx}. {profile}")
    print("999. 🔥 Mở tất cả profiles")

    drivers = []  # Danh sách driver đang chạy

    # Cho phép mở nhiều profile liên tiếp
    while True:
        try:
            choice = int(input("\n🔹 Nhập số profile muốn mở (0 để thoát, 999 để mở tất cả): "))

            if choice == 0:
                print("❌ Đóng tất cả trình duyệt...")
                for driver in drivers:
                    driver.quit()
                break  # Thoát khỏi vòng lặp

            elif choice == 999:
                print("\n🚀 Đang mở tất cả profiles...")
                open_multiple_profiles(profiles, drivers)
            
            elif 1 <= choice <= len(profiles):
                selected_profile = profiles[choice - 1]
                driver = open_single_profile(selected_profile)
                drivers.append(driver)  # Lưu lại driver đang chạy

            else:
                print("⚠️ Số không hợp lệ! Vui lòng nhập lại.")

        except ValueError:
            print("⚠️ Vui lòng nhập số!")


def open_single_profile(profile_path):
    
    """Mở một trình duyệt với profile cụ thể và trả về driver"""
    
    print(f"\n🚀 Đang mở trình duyệt với profile: {profile_path}")
    chrome_options = chromeoptions_auto()
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

    #mo chrome path
    chrome_options.binary_location = chrome_path

    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://abrahamjuliot.github.io/creepjs/')
    time.sleep(5)
    
    
    return driver  # Trả về driver để có thể đóng sau này

def open_multiple_profiles(profiles, drivers, start_port=9222, port_file="ports.txt"):
    
    """Mở tất cả các trình duyệt với danh sách profile song song"""
    
    with ThreadPoolExecutor() as executor, open(port_file, "w") as f:
        futures = []
        for i, profile in enumerate(profiles):
            port = start_port + i  # Mỗi profile có một cổng riêng
            chrome_options = chromeoptions_auto()
            chrome_options.add_argument(f"--user-data-dir={profile}")
            chrome_options.add_argument(f"--remote-debugging-port={port}")  # Thêm remote port
            chrome_options.binary_location = chrome_path
            
            futures.append(executor.submit(open_single_profile_with_options, profile, chrome_options, port, f))

        for future in futures:
            driver = future.result()
            if driver:
                drivers.append(driver)

def open_single_profile_with_options(profile_path, chrome_options, port, file):

    """Mở một trình duyệt với profile cụ thể và trả về driver, sử dụng chrome_options đã thiết lập"""
    
    print(f"\n🚀 Đang mở trình duyệt với profile: {profile_path} trên cổng {port}")
    file.write(f"Profile: {profile_path}, Port: {port}\n")  # Ghi thông tin vào file
    
    service = Service(chrome_driver_path)
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        cygnus(driver)  # Gọi hàm xử lý riêng nếu cần
        time.sleep(5)
        
        return driver
    except Exception as e:
        print(f"❌ Lỗi khi mở profile {profile_path}: {e}")
        return None

if __name__ == "__main__":
    open_profiles()
    