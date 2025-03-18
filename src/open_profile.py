import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromeoptions_auto.chrome_options_auto import chromeoptions_auto,chrome_option_webgl
from concurrent.futures import ThreadPoolExecutor
from autoweb.gmail import gmail
from autoweb.createmetamask import create_metamask
from autoweb.cygnus import cygnus
from login_gmail import open_profiles_with_gmails
import time
chrome_path = r"/opt/google/chrome/chrome"
#from auto_diskpay import arrange_windows

chrome_driver_path = r"/home/zik/Documents/auto/chromedriver"
profile_file = "profiles.txt"

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

def open_multiple_profiles(profiles, drivers):
    """Mở tất cả các trình duyệt với danh sách profile song song"""
    # Sử dụng ThreadPoolExecutor để mở các profile đồng thời
    with ThreadPoolExecutor() as executor:
        futures = []
        for profile in profiles:
            
            chrome_options = chromeoptions_auto()  # Khởi tạo chrome_options
            chrome_options.add_argument(f"--user-data-dir={profile}")  # Thêm tùy chọn cho profile
            chrome_options.binary_location = chrome_path
            # Tạo futures cho mỗi profile với chrome_options được truyền vào
            futures.append(executor.submit(open_single_profile_with_options, profile, chrome_options))

        # Chờ các thread hoàn tất và thu kết quả
        for future in futures:
            driver = future.result()  # Chờ và lấy kết quả từ từng luồng
            drivers.append(driver)

def open_single_profile_with_options(profile_path, chrome_options):
    """Mở một trình duyệt với profile cụ thể và trả về driver, sử dụng chrome_options đã thiết lập"""
    print(f"\n🚀 Đang mở trình duyệt với profile: {profile_path}")
    
    service = Service(chrome_driver_path)
    try:
        chrome_options = chromeoptions_auto()
        chrome_options.binary_location = chrome_path
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        
        cygnus(driver)
        time.sleep(5)
        # Giả sử đây là một hàm thực hiện hành động gì đó trên driver
        
        return driver  # Trả về driver sau khi mở trình duyệt thành công
    except Exception as e:
        print(f"❌ Lỗi khi mở profile {profile_path}: {e}")
        return None  # Trả về None nếu có lỗi xảy ra

    return driver 
if __name__ == "__main__":
    open_profiles()