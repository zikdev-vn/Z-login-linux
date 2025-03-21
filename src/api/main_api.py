import os
import time
import random
import json
from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

# Đường dẫn chromedriver (CẬP NHẬT THEO MÁY CỦA BẠN)
CHROME_DRIVER_PATH = r"/home/zik/Documents/auto/chromedriver"
PROFILE_FOLDER = "/home/zik/.config/google-chrome"
PROFILE_FILE = "profiles.json"

# Tải dữ liệu từ file JSON nếu có
try:
    with open(PROFILE_FILE, "r") as f:
        profiles = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    profiles = {}

profile_counter = max(map(int, profiles.keys()), default=0) + 1  # ID tiếp theo


def generate_random_port():
    """Tạo một cổng ngẫu nhiên từ 10000 đến 65000"""
    return random.randint(10000, 65000)


def save_profiles():
    """Lưu danh sách profile vào file JSON"""
    with open(PROFILE_FILE, "w") as f:
        json.dump(profiles, f, indent=4)


@app.route('/create_profiles', methods=['POST'])
def create_profiles():
    global profile_counter

    data = request.json
    if not data or 'count' not in data:
        return jsonify({"error": "Thiếu tham số 'count'!"}), 400

    count = data['count']
    if count < 2:
        return jsonify({"error": "Số lượng profile phải lớn hơn hoặc bằng 2!"}), 400

    created_profiles = []

    for i in range(count):
        profile_id = profile_counter
        profile_counter += 1

        profile_path = os.path.join(PROFILE_FOLDER, f"profile_{profile_id}")
        os.makedirs(profile_path, exist_ok=True)  # Tạo thư mục profile

        profiles[str(profile_id)] = {
            "name": f"Profile_{profile_id}",
            "profile_path": profile_path,
            "browser": "Chrome",
            "--remote-debugging-port": generate_random_port(),
            "is_masked_font": True,
            "is_noise_canvas": False,
            "is_noise_webgl": False,
            "is_noise_client_rect": False,
            "is_noise_audio_context": True,
            "is_random_screen": False,
            "is_masked_webgl_data": True,
            "is_masked_media_device": True
        }

        created_profiles.append(profiles[str(profile_id)])

    save_profiles()  # Lưu vào JSON

    return jsonify({"message": f"Đã tạo {count} profile!", "profiles": created_profiles}), 201


@app.route('/start_browser/<int:profile_id>', methods=['GET'])
def start_browser(profile_id):
    """Mở trình duyệt với profile đã tạo"""
    profile = profiles.get(str(profile_id))
    if not profile:
        return jsonify({"error": "Profile không tồn tại!"}), 404

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile['profile_path']}")

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.google.com")
    time.sleep(5)  
    driver.quit()

    return jsonify({"message": f"Đã mở Chrome với profile {profile_id}!"})


@app.route('/list_profiles', methods=['GET'])
def list_profiles():
    """Hiển thị danh sách tất cả profile"""
    if not profiles:
        return jsonify({"message": "Chưa có profile nào được tạo!"}), 200

    profile_list = [{"id": int(pid), **info} for pid, info in profiles.items()]
    return jsonify({"profiles": profile_list})




@app.route('/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    """Lấy thông tin profile"""
    profile = profiles.get(str(profile_id))
    if profile:
        return jsonify({"id": profile_id, **profile})
    return jsonify({"error": "Profile không tồn tại!"}), 404



PROFILE_TXT_FILE = "profiles.txt"

def load_old_profiles():
    """Đọc danh sách profile cũ từ profiles.txt"""
    old_profiles = []
    if os.path.exists(PROFILE_TXT_FILE):
        with open(PROFILE_TXT_FILE, "r") as f:
            old_profiles = [line.strip() for line in f.readlines() if line.strip()]
    return old_profiles

@app.route('/update_old_profiles', methods=['POST'])
def update_old_profiles():
    """Kiểm tra & cập nhật cấu hình cho các profile cũ từ profiles.txt"""
    old_profiles = load_old_profiles()
    updated_profiles = []
    global profile_counter

    for profile_path in old_profiles:
        # Tạo ID dựa trên danh sách profile hiện có
        profile_id = str(profile_counter)
        profile_counter += 1

        if profile_path in [p["profile_path"] for p in profiles.values()]:
            continue  # Nếu profile đã có, bỏ qua

        profiles[profile_id] = {
            "name": f"Profile_{profile_id}",
            "profile_path": profile_path,
            "browser": "Chrome",
            "--remote-debugging-port": generate_random_port(),
            "is_masked_font": True,
            "is_noise_canvas": False,
            "is_noise_webgl": False,
            "is_noise_client_rect": False,
            "is_noise_audio_context": True,
            "is_random_screen": False,
            "is_masked_webgl_data": True,
            "is_masked_media_device": True
        }

        updated_profiles.append(profiles[profile_id])

    save_profiles()

    if updated_profiles:
        return jsonify({"message": "Đã cập nhật các profile cũ từ profiles.txt!", "updated_profiles": updated_profiles}), 200
    return jsonify({"message": "Tất cả profile cũ đã được cập nhật trước đó!"}), 200



if __name__ == '__main__':
    app.run(debug=True, port=5000)
