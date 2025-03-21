import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from src.chromeoptions_auto.chrome_options_auto import chromeoptions_auto


# Đường dẫn ChromeDriver
chrome_driver_path = r"/home/zik/Documents/auto/chromedriver"

# File chứa danh sách profile và Gmail
profile_file = "data/profiles.txt"
gmail_file = "data/gmail.txt"

def get_profiles():
    """Đọc danh sách profile từ file"""
    if not os.path.exists(profile_file):
        print("⚠️ Không tìm thấy file profiles.txt! Hãy tạo profile trước.")
        return []

    with open(profile_file, "r", encoding="utf-8") as f:
        profiles = [line.strip() for line in f if line.strip()]

    if not profiles:
        print("⚠️ Không có profile nào để mở!")
        return []

    return profiles

def get_gmails():
    """Đọc danh sách Gmail từ file"""
    if not os.path.exists(gmail_file):
        print(f"⚠️ Không tìm thấy file {gmail_file}! Hãy tạo Gmail trước.")
        return []

    with open(gmail_file, "r", encoding="utf-8") as f:
        gmails = [line.strip() for line in f if line.strip()]

    if not gmails:
        print("⚠️ Không có Gmail nào trong file!")
        return []

    return gmails


def login_gmail(driver, gmail):
    """Đăng nhập Gmail với tài khoản được chỉ định"""
    driver.get("https://workspace.google.com/intl/vi/gmail/")
    time.sleep(5)

    # Nút đăng nhập
    try:
        login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div/div[5]/a[2]/span')
        login_button.click()
        time.sleep(5)

        # Nhập Gmail
        email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email_input.send_keys(gmail)
        print(f"✅ Đã nhập email: {gmail}")
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        # element nhap password
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        password_input.send_keys("Thao2004")
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        print("✅ Đã nhập mật khẩu")
        try:
            element_exit = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div/div/div[2]/button[1]/div[1]')

            if element_exit.is_displayed():
                element_exit.click()
                print("✅ chuyen tiep")
            else:
                print("❌ Khong chuyen tiep")
        except NoSuchElementException:
            print("❌ Khong chuyen tiep")


    except NoSuchElementException:
        print("❌ Không tìm thấy nút đăng nhập!")
    

def open_single_profile(profile, gmail):
    """Mở một trình duyệt với profile và đăng nhập Gmail"""
    try:
        print(f"\n🚀 Mở profile: {profile} với Gmail: {gmail}")

        chrome_options = chromeoptions_auto()
        chrome_options.add_argument(f"--user-data-dir={profile}")  # Mở Chrome với profile riêng

        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        login_gmail(driver, gmail)  # Đăng nhập Gmail

        input(f"Nhấn Enter để đóng trình duyệt {profile}...")
        driver.quit()  # Đóng trình duyệt sau khi hoàn tất

    except Exception as e:
        print(f"❌ Lỗi khi mở profile {profile}: {e}")

# Hàm chạy nhiều profile song song
def open_profiles_with_gmails():
    """Mở tất cả profile với Gmail tương ứng (đa luồng)"""
    profiles = get_profiles()
    gmails = get_gmails()

    if not profiles or not gmails:
        print("⚠️ Không thể mở trình duyệt vì thiếu profile hoặc Gmail!")
        return

    num_profiles = min(len(profiles), len(gmails))  # Chạy theo số lượng nhỏ hơn giữa profiles và gmails
    print(f"🚀 Đang mở {num_profiles} profile cùng lúc...\n")

    with ThreadPoolExecutor(max_workers=num_profiles) as executor:
        for i in range(num_profiles):
            executor.submit(open_single_profile, profiles[i], gmails[i])

    print("✅ Đã khởi chạy xong tất cả trình duyệt!")


def main_gmail():
    print("Chọn thao tác:")
    print("1. Mở profile Gmail")
    print("2. Thoát")
    
    choice = input("Nhập lựa chọn: ").strip()
    if choice == "1":
        open_profiles_with_gmails()
    elif choice == "2":
        print("Thoát chương trình!")
        exit()

if __name__ == "__main__":
    main_gmail()
