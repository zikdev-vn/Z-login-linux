from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


def remote_connect_from_ports(port_file="ports.txt"):
    """Đọc file ports.txt và kết nối tới các trình duyệt từ xa"""
    try:
        with open(port_file, "r") as f:
            lines = f.readlines()
        
        drivers = []
        for line in lines:
            parts = line.strip().split(", Port: ")
            if len(parts) == 2:
                port = parts[1]
                print(f"🔗 Đang kết nối tới trình duyệt trên cổng {port}")
                options = webdriver.ChromeOptions()
                options.debugger_address = f"localhost:{port}"
                driver = webdriver.Chrome(options=options)
                drivers.append(driver)
        
        return drivers
    except Exception as e:
        print(f"❌ Lỗi khi kết nối từ xa: {e}")
        return []

if __name__ == "__main__":
    drivers = remote_connect_from_ports()
    for driver in drivers:
        driver.get("ttps://i.cygnus.finance/#")
        time.sleep(5)
        driver.quit()