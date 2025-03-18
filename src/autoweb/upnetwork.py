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

def upnetwork(driver):
    driver.get("https://nodes.upnetwork.xyz/login")
    time.sleep(5)

    try:
        element1 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=btn-login-privy']"))
            )
        if element1.is_displayed():
            print("Tìm thấy nút login, tiến hành click...")
            time.sleep(2)
            element1.click()

        element2 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='privy-modal-content']/div/div[1]/div[3]/div/button[1]"))
            )
        if element2.is_displayed():
                print("Tìm thấy nút login bang google, tiến hành click...")
                time.sleep(2)
                element2.click()
                time.sleep(5)
        element3 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div"))
            )
        
        if element3.is_displayed():
            print("Tìm thấy nút chọn tài khoản google, tiến hành click...")
            time.sleep(2)
            element3.click()
            time.sleep(5)
        element4 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span"))
            )
        if element4.is_displayed(): 
            print("Tìm thấy nút đăng nhập, tiến hành click...")
            time.sleep(2)
            element4.click()
            time.sleep(5)
        element5 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='form-claim-points']/button/span"))
            )
        if element5.is_displayed():
            print("Tìm thấy nút claim, tiến hành click...")
            time.sleep(2)
            element5.click()
            time.sleep(5)
    except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
        print("Không tìm thấy nút login, thử cách khác...")