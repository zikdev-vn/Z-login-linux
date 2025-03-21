import time
from selenium.webdriver.common.by import By
from faker import Faker
import os
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
        number = random.randint(1000, 9999)  # Thêm số tránh trùng
        gmail_name = f"{first_name}{last_name}{number}"

        if not is_email_exists(gmail_name):

            return gmail_name

# Kiểm tra xem tên Gmail đã tồn tại trong file chưa
def is_email_exists(gmail_name):
    if not os.path.exists("gmail_accounts.txt"):
        return False  # Nếu file chưa tồn tại thì không có email nào trùng

    with open("gmail_accounts.txt", "r") as file:
        emails = file.read().splitlines()
        return gmail_name in emails

# Lưu Gmail vào file
def save_email(gmail_name):
    with open("gmail_accounts.txt", "a") as file:
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
            element14 = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='selectionc3']"))
            )
            print("Có if thứ 2 ở đây")
            if element14.is_displayed():
                element14.click()
                time.sleep(3)
            else:
                print("Không tìm thấy phần tử checkpass, bỏ qua!")
        except ( NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy phần tử chọn tài khoản, bỏ qua!")
            # Nhập mật khẩu
        except Exception as e:
            # Nếu gặp lỗi không mong muốn nào khác
            print(f"Đã gặp lỗi không xác định: {e}")
        try:
            print("dang nhap mat khau")
            element15 = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='passwd']/div[1]/div/div[1]/input"))
            )
            element15.send_keys("Thao2004")
            time.sleep(2)

            element16 = driver.find_element(By.XPATH, "//*[@id='confirm-passwd']/div[1]/div/div[1]/input")
            element16.send_keys("Thao2004")
            time.sleep(2)
            element16.send_keys(Keys.ENTER)

        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy ô nhập mật khẩu, bỏ qua!")

        time.sleep(20)

    except NoSuchElementException:
        print("Không tìm thấy button đầu tiên, bỏ qua!")
    

    print("Đã tạo Gmail thành công!")
    
    