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

def cygnus(driver):
    driver.get("https://i.cygnus.finance/#_")

    time.sleep(5)




    #except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
    #    print("Không tìm thấy nút cài đặt MetaMask, thử cách khác...")