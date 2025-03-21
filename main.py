
from src.create_gmail import gmail
from src.open_profile import open_profiles
from src.create_profile import create_profiles
from script_auto.createmetamask import create_metamask
from script_auto.cygnus import cygnus
from script_auto.gmail import gmail
from src.api.api_sql import api_sql
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src import open_profile
#from src import xapxepcuaso 
from src import create_profile
from src.login_gmail import main_gmail
import curses

def menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    menu_items = ["Mở profile trình duyệt", "Sắp xếp cửa sổ trình duyệt", "Tạo profile trình duyệt", "Mở API", "Thoát"]
    current_index = 0

    while True:
        stdscr.clear()
        stdscr.addstr("\n===== MENU CHÍNH =====\n")
        for i, item in enumerate(menu_items):
            if i == current_index:
                stdscr.addstr(f"➡️  {item}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"   {item}\n")
        
        key = stdscr.getch()
        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < len(menu_items) - 1:
            current_index += 1
        elif key == ord("\n"):  # Nhấn Enter để chọn
            if current_index == 0:
                open_profiles()
            elif current_index == 1:
                print("Đang phát triển\n")
            elif current_index == 2:
                create_profiles()
            elif current_index == 3:
                api_sql()
            elif current_index == 4:
                stdscr.addstr("👋 Thoát chương trình. Hẹn gặp lại!\n")
                stdscr.refresh()
                curses.napms(1000)
                break

if __name__ == "__main__":
    curses.wrapper(menu)