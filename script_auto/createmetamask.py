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
from selenium.webdriver.common.alert import Alert

def create_metamask(driver):
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome")

    time.sleep(5)
    try:
        element1 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='onboarding__terms-checkbox']"))
            )
        if element1.is_displayed():
            print("Tìm thấy nút cài đặt MetaMask, tiến hành click...")
            time.sleep(2)
            element1.click()
            time.sleep(5)
        try:
            element2 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/ul/li[2]/button"))
            )
            if element2.is_displayed():
                print("Tìm thấy nút tiếp theo, tiến hành click...")
                time.sleep(2)
                element2.click()
                time.sleep(5)   
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy nút tiếp theo, thử cách khác...")
        try:
            element3 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button[1]"))
            )
            if element3.is_displayed():
                print("Tìm thấy nút tiếp theo, tiến hành click...")
                time.sleep(2)
                element3.click()
                time.sleep(5)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy nút tiếp theo, thử cách khác...")
        try:
            element4 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))
            )
            if element4.is_displayed():
                print("Tìm thấy nút tiếp theo, tiến hành click...")
                time.sleep(2)
                element4.send_keys("Thao2004")
                time.sleep(5)

                element5 = driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/div[2]/label/input")
                element5.send_keys("Thao2004")
                time.sleep(5)
                element6 = driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/div[3]/label/span[1]/input")
                element6.click()
                time.sleep(5)
                element66 = driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/button")
                element66.click()
                time.sleep(5)

        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy nút passwd")

        try:
            element7 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[3]/button[1]"))
            )
            if element7.is_displayed():
                print("Tìm thấy nút (nhac toi sau)")
                
                element7.click()
                time.sleep(5)

                element8 = driver.find_element(By.XPATH, "//*[@id='popover-content']/div/div/section/div[1]/div/div/label/input")
                element8.click()
                time.sleep(5)
                element9 = driver.find_element(By.XPATH, "//*[@id='popover-content']/div/div/section/div[2]/div/button[2]")
                element9.click()
                time.sleep(5)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy nút (nhac toi sau)")

        try:
            element10 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[3]/button"))
            )
            if element10.is_displayed():
                print("Tìm thấy nút (hoan tat)")
                element10.click()
                time.sleep(5)

                element11 = driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button")
                element11.click()
                time.sleep(5)

                element12 = driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button")
                element12.click()
                time.sleep(5)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("Không tìm thấy nút (hoan tat)")
        
        
        except Exception as e:
            # Nếu gặp lỗi không mong muốn nào khác
            print(f"Đã gặp lỗi không xác định: {e}")
    except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
        print("khong tim thay thong tin gi") 