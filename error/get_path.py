import sqlite3
import json

DB_FILE = "data/profiles.db"  # Thay bằng đường dẫn file SQLite thực tế

def get_profiles():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT profile_path FROM profiles")
        profiles = [row[0] for row in cursor.fetchall()]
    return profiles

if __name__ == "__main__":
    profiles = get_profiles()
    print(json.dumps(profiles))  # Xuất dưới dạng JSON để Bash đọc được
