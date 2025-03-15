import random
from selenium import webdriver
#from openprofile import profile_path
def chromeoptions_auto(profile_path=None):
    """Tạo ChromeOptions với các cấu hình cần thiết"""
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument("--force-device-scale-factor=0.75")  # Đặt tỷ lệ zoom là 75%
    chrome_options.add_argument("--window-size=300,490")

    # 1️⃣ Giảm phát hiện Selenium
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # 2️⃣ Tăng tốc Chrome
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-session-crashed-bubble")


    # 3️⃣ Fake User-Agent
    #user_agents = [
    #    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    #    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    #    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    #]
    #random_user_agent = random.choice(user_agents)
    #chrome_options.add_argument(f"user-agent={random_user_agent}")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    # 4️⃣ Chặn WebRTC
    chrome_options.add_argument("--disable-webrtc")

    # 5️⃣ Chặn thông báo, pop-up
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # 6️⃣ Load profile nếu có 

    return chrome_options  
    # 🔥 Phải return để file `main.py` có thể sử dụng
    # how to import // from chromeoptions_auto.chrome_options_auto import chromeoptions_auto
    