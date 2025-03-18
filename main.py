from chromeoptions_auto.chrome_options_auto import chromeoptions_auto 
from src.create_gmail import gmail
from src.open_profile import open_profiles
from src.autoweb.createmetamask import create_metamask
from src.autoweb.cygnus import cygnus
from src.autoweb.gmail import gmail

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src import open_profile
#from src import xapxepcuaso 
from src import create_profile
from src import gmail


def main():
    while True:
        print("\n===== MENU CHÍNH =====")
        print("1️⃣ Mở profile trình duyệt")
        print("2️⃣ Sắp xếp cửa sổ trình duyệt")
        print("3️⃣ Tạo profile trình duyệt")
        print("4️⃣ Mở Gmail")
        print("0️⃣ Thoát")

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            open_profile.open_profiles()
        elif choice == "2":
            print("dang phat trien \n")
            #xapxepcuaso.arrange_windows()
        elif choice == "3":
            create_profile.create_profiles()
        
        elif choice == "0":
            print("👋 Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ! Vui lòng nhập lại.")

if __name__ == "__main__":
    main()