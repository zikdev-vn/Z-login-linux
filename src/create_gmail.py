import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.chromeoptions_auto.chrome_options_auto import chromeoptions_auto



chrome_driver_path = r"auto/chromedriver"
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
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    gmail(driver)
    
    return driver  # Trả về driver để có thể đóng sau này

def open_multiple_profiles(profiles, drivers):
    """Mở tất cả các trình duyệt với danh sách profile"""
    for profile in profiles:
        print(f"\n🚀 Mở profile: {profile}")
        chrome_options = chromeoptions_auto()
        chrome_options.add_argument(f"--user-data-dir={profile}")

        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.google.com")
        gmail(driver)

import time
from selenium.webdriver.common.by import By
from faker import Faker
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker("en_US")
namegmail = [
    "thao", "hoang", "thanh", "mao", "thuy", "huong",
    "thu", "mon", "thien", "chill", "thinh", "cuong",
    "thien", "lam", "tieu", "phong", "thanh", "vuong",
    "thao", "nguyen", "viem"
]

hogmail = [
    "config", "vn", "us", "lao", "jp", "gtk", "nvt", "momo",
    "dbd", "bina", "bida", "dubai", "any", "zozo", "onion",
    "zikdev", "zik"
]
def generate_unique_gmail_name():
    while True:
        first_name = random.choice(namegmail)  # Chọn ngẫu nhiên từ namegmail
        last_name = random.choice(hogmail)  # Chọn ngẫu nhiên từ hogmail
        number = random.randint(100, 999)  # Thêm số tránh trùng
        gmail_name = f"{first_name}{last_name}{number}"

        if not is_email_exists(gmail_name):

            return gmail_name

# Kiểm tra xem tên Gmail đã tồn tại trong file chưa
def is_email_exists(gmail_name):
    if not os.path.exists("data/gmail_accounts.txt"):
        return False  # Nếu file chưa tồn tại thì không có email nào trùng

    with open("data/gmail_accounts.txt", "r") as file:
        emails = file.read().splitlines()
        return gmail_name in emails

# Lưu Gmail vào file
def save_email(gmail_name):
    with open("data/gmail_accounts.txt", "a") as file:
        file.write(gmail_name + "\n")
    print(f"Đã lưu Gmail: {gmail_name}")


def gmail(driver):
    #fake = Faker("vi_VN")
    first_name = fake.first_name()
    last_name = fake.last_name()
    day = random.randint(1, 30)  
    year = random.randint(1979, 2005)
    unique_gmail_name = generate_unique_gmail_name()  # Tạo Gmail ngẫu nhiên
    save_email(unique_gmail_name) # Lưu Gmail vào file


    print("Chương trình tạo Gmail")
    driver.get("https://www.youtube.com")  # Sửa link YouTube đúng
    time.sleep(5)

    # Sửa lỗi dấu nháy kép trong XPath
    element1 = driver.find_element(By.XPATH, "//*[@id='buttons']/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
    element1.click()
    time.sleep(5)

    element2 = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button/span")
    element2.click()
    time.sleep(5)

    element3 = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[3]")
    element3.click()
    time.sleep(5)

    # Tìm ô nhập họ và tên
    element4 = driver.find_element(By.XPATH, "//*[@id='lastName']")
    time.sleep(2)
    element5 = driver.find_element(By.XPATH, "//*[@id='firstName']")

    # Nhập họ và tên vào form
    element4.send_keys(last_name)
    element5.send_keys(first_name)

    element6 = driver.find_element(By.XPATH, "//*[@id='collectNameNext']/div/button/span")
    element6.click()
    time.sleep(5)

    element7 = driver.find_element(By.XPATH, "//*[@id='day']")
    time.sleep(2)
    element8 = driver.find_element(By.XPATH, "//*[@id='year']")

    element7.send_keys(day)
    element8.send_keys(year)

    month_element = driver.find_element(By.XPATH, "//*[@id='month']")

# Tạo danh sách tháng từ 1 - 12
    month_index = random.randint(1, 12)  # Vì các option thường bắt đầu từ 1 đến 12

# Sử dụng Select để chọn ngẫu nhiên
    select9 = Select(month_element)
    select9.select_by_index(month_index)

    print(f"Đã chọn tháng: {month_index}")

    print(f"Đã nhập họ và tên: {first_name} {last_name}")


    gioitinh = random.randint(1,2)
    gioitinh_element = driver.find_element(By.XPATH, "//*[@id='gender']")
    select10 = Select(gioitinh_element)
    select10.select_by_index(gioitinh)

    time.sleep(2)

    element11 = driver.find_element(By.XPATH, "//*[@id='birthdaygenderNext']/div/button/span")
    element11.click()
    time.sleep(5)

    try:
        element12 = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[2]/button")
        print("Có if thứ 1 ở đây")

        if element12.is_displayed():
            element12.click()
            time.sleep(5)
            print("Đã click vào button thành công!")

        # Thử nhập Gmail vào ô đầu tiên
        try:
            element13 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input"))
            )

            if element13.is_displayed():
                print("Tìm thấy ô nhập Gmail, tiến hành nhập...")
                element13.send_keys(unique_gmail_name)
                time.sleep(2)
                element13.send_keys(Keys.ENTER)
                time.sleep(2)
            else:
                print("Phần tử không hiển thị được, bỏ qua!")

        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy ô nhập Gmail, thử cách khác...")

        # Nếu không tìm thấy ô nhập Gmail đầu tiên, thử click vào nút mở ô khác
        try:
            element_next_o_gmail = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/span/div[3]/div/div[1]/div/div[3]/div"))
            )
            element_next_o_gmail.click()
            print("Đã click vào nút mở ô nhập Gmail khác.")
            time.sleep(2)

            # Nhập Gmail vào ô thay thế
            element_next_o_gmail1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input"))
            )
            element_next_o_gmail1.send_keys(unique_gmail_name)
            print(f"Đã nhập Gmail vào ô thay thế: {unique_gmail_name}")
            time.sleep(2)
            element_next_o_gmail1.send_keys(Keys.ENTER)

        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy ô nhập Gmail thay thế, bỏ qua!")

        # Kiểm tra xem có bước chọn tài khoản không
        try:
            element14 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='selectionc3']"))
            )
            print("Có if thứ 2 ở đây")
            if element14.is_displayed():
                element14.click()
                time.sleep(3)
            else:
                print("Không tìm thấy phần tử checkpass, bỏ qua!")
        except NoSuchElementException:
                    print("Không tìm thấy phần tử chọn tài khoản, bỏ qua!")
            # Nhập mật khẩu
        try:
                element15 = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='passwd']/div[1]/div/div[1]/input"))
                )
                element15.send_keys("Thao2004")
                time.sleep(2)

                element16 = driver.find_element(By.XPATH, "//*[@id='confirm-passwd']/div[1]/div/div[1]/input")
                element16.send_keys("Thao2004")
                time.sleep(2)
                element16.send_keys(Keys.ENTER)

        except NoSuchElementException:
                print("Không tìm thấy ô nhập mật khẩu, bỏ qua!")

        

    except NoSuchElementException:
        print("Không tìm thấy button đầu tiên, bỏ qua!")
if __name__ == "__main__":
    open_profiles()