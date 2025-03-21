from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Đọc cổng remote từ file remote_port.txt
with open('remote_port.txt', 'r') as file:
    lines = file.readlines()
    last_line = lines[-1]
    remote_port = last_line.split(':')[-1].strip()

# Cấu hình Selenium để kết nối với Chrome đã mở sẵn qua remote debugging
options = Options()
options.add_argument(f'--remote-debugging-port={remote_port}')

# Sử dụng Remote WebDriver để kết nối với phiên bản Chrome đã mở sẵn
driver = webdriver.Remote(
    command_executor=f'http://localhost:{remote_port}/wd/hub',  # Địa chỉ WebDriver từ remote
    options=options
)

# Mở trang web với Selenium
driver.get('https://i.cygnus.finance/#_')

# Chờ kết quả
time.sleep(5)

# Đóng trình duyệt
driver.quit()
