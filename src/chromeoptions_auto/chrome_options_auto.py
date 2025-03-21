import random
from selenium import webdriver
#from openprofile import profile_path
def chromeoptions_auto(profile_path=None):
    """Tạo ChromeOptions với các cấu hình cần thiết"""
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument("--force-device-scale-factor=0.75")  # Đặt tỷ lệ zoom là 75%
    chrome_options.add_argument("--window-size=300,490")


    # webgl
    #chrome_options.add_argument("--use-gl=desktop")
    #chrome_options.add_argument("--ignore-gpu-blacklist")
    #chrome_options.add_argument("--enable-gpu-rasterization")
    chrome_options.add_argument("--enable-webgl")
      # Ẩn thanh thông tin Chrome
    # 1️⃣ Giảm phát hiện Selenium
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # 2️⃣ Tăng tốc Chrome
    #chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-session-crashed-bubble")


    # 3️⃣ Fake User-Agent
    user_agents = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3',
    'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
    'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.93 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; U; Android 2.2; en-us; SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true',
    'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.0.1; en-US) AppleWebKit/535.8+ (KHTML, like Gecko) Version/7.2.0.1 Safari/535.8+',
    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH-i917)',
    'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+',
    'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba',
    'Mozilla/5.0 (BlackBerry; U; BlackBerry 9930; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.241 Mobile Safari/534.11+',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0)',
    'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/12.0.024; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.12344',
    'Mozilla/5.0 (Android; Mobile; rv:27.0) Gecko/27.0 Firefox/27.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Thunderbird/38.2.0 Lightning/4.0.2',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; Microsoft Outlook 15.0.4420)',
    'Mozilla/5.0 (X11; CrOS i686 0.12.433) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.77 Safari/534.30'

]
    random_user_agent = random.choice(user_agents)
    chrome_options.add_argument(f"user-agent={random_user_agent}")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")

    
    # 4️⃣ Chặn WebRTC
    #chrome_options.add_argument("--disable-webrtc")

    # 5️⃣ Chặn thông báo, pop-up
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
    }
    chrome_options.add_experimental_option("prefs", prefs)

    return chrome_options



