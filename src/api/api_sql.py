import sqlite3
import os
import random
import time
import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_FILE = "data/profiles.db"

# 🛠 Tạo database nếu chưa có
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            profile_path TEXT UNIQUE,
                            remote_debugging_port INTEGER,
                            is_masked_font BOOLEAN,
                            is_masked_media_device BOOLEAN,
                            is_masked_webgl_data BOOLEAN,
                            is_noise_audio_context BOOLEAN,
                            is_noise_canvas BOOLEAN,
                            is_noise_client_rect BOOLEAN,
                            is_noise_webgl BOOLEAN,
                            is_random_screen BOOLEAN,
                            browser TEXT,
                            status TEXT DEFAULT 'closed'
                          )''')
        conn.commit()

# 🛠 Hàm lấy cổng ngẫu nhiên >10000
def generate_random_port():
    return random.randint(10000, 60000)

# ✅ API: Tạo profile mới
@app.route('/create_profile', methods=['POST'])
def create_profile():
    data = request.json
    profile_path = data.get("profile_path")

    if not profile_path:
        return jsonify({"error": "Thiếu profile_path!"}), 400

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # Kiểm tra nếu profile đã tồn tại
        cursor.execute("SELECT * FROM profiles WHERE profile_path=?", (profile_path,))
        if cursor.fetchone():
            return jsonify({"error": "Profile đã tồn tại!"}), 400

        # Tạo profile
        port = generate_random_port()
        cursor.execute('''INSERT INTO profiles (name, profile_path, remote_debugging_port, browser,
                        is_masked_font, is_masked_media_device, is_masked_webgl_data, is_noise_audio_context,
                        is_noise_canvas, is_noise_client_rect, is_noise_webgl, is_random_screen)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (f"Profile_{port}", profile_path, port, "Chrome", True, True, True, True, False, False, False, False))
        conn.commit()

    return jsonify({"message": "Profile created!", "profile_path": profile_path, "port": port}), 201

# ✅ API: Lấy danh sách profile
@app.route('/get_profiles', methods=['GET'])
def get_profiles():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profiles")
        profiles = [{"id": row[0], "name": row[1], "profile_path": row[2], "port": row[3], "status": row[13]} for row in cursor.fetchall()]

    return jsonify({"profiles": profiles})

# ✅ API: Cập nhật profile
@app.route('/update_profile/<int:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    data = request.json
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # Kiểm tra profile có tồn tại không
        cursor.execute("SELECT * FROM profiles WHERE id=?", (profile_id,))
        if not cursor.fetchone():
            return jsonify({"error": "Profile không tồn tại!"}), 404

        # Cập nhật profile
        for key, value in data.items():
            cursor.execute(f"UPDATE profiles SET {key}=? WHERE id=?", (value, profile_id))
        conn.commit()

    return jsonify({"message": "Profile updated!"}), 200

# ✅ API: Mở profile (Khởi chạy trình duyệt)
@app.route('/open_profile/<int:profile_id>', methods=['POST'])
def open_profile(profile_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT profile_path, remote_debugging_port FROM profiles WHERE id=?", (profile_id,))
        profile = cursor.fetchone()

    if not profile:
        return jsonify({"error": "Profile không tồn tại!"}), 404

    profile_path, port = profile

    # Khởi chạy trình duyệt với profile
    chrome_cmd = f"google-chrome --user-data-dir={profile_path} --remote-debugging-port={port} &"
    subprocess.Popen(chrome_cmd, shell=True)

    # Cập nhật trạng thái profile thành "open"
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE profiles SET status='open' WHERE id=?", (profile_id,))
        conn.commit()

    return jsonify({"message": f"Profile {profile_id} đã mở trên port {port}!"}), 200

# ✅ API: Đóng profile (Kill trình duyệt)
@app.route('/close_profile/<int:profile_id>', methods=['POST'])
def close_profile(profile_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT remote_debugging_port FROM profiles WHERE id=?", (profile_id,))
        profile = cursor.fetchone()

    if not profile:
        return jsonify({"error": "Profile không tồn tại!"}), 404

    port = profile[0]

    # Kill process chạy trên port đó
    os.system(f"fuser -k {port}/tcp")

    # Cập nhật trạng thái profile thành "closed"
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE profiles SET status='closed' WHERE id=?", (profile_id,))
        conn.commit()

    return jsonify({"message": f"Profile {profile_id} đã đóng!"}), 200
# ✅ API: Cập nhật các profile cũ từ profiles.txt
@app.route('/update_old_profiles', methods=['POST'])
def update_old_profiles():
    profile_file = "data/profiles.txt"
    
    if not os.path.exists(profile_file):
        return jsonify({"error": "File profiles.txt không tồn tại!"}), 404

    updated_profiles = []

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        with open(profile_file, "r") as f:
            for line in f.readlines():
                profile_path = line.strip()
                if not profile_path:
                    continue
                
                # Kiểm tra xem profile có trong database chưa
                cursor.execute("SELECT id FROM profiles WHERE profile_path=?", (profile_path,))
                profile = cursor.fetchone()

                if profile:
                    # Nếu có thì cập nhật lại cấu hình mới
                    profile_id = profile[0]
                    port = generate_random_port()
                    cursor.execute('''UPDATE profiles SET remote_debugging_port=?, 
                                        is_masked_font=?, is_masked_media_device=?, 
                                        is_masked_webgl_data=?, is_noise_audio_context=?, 
                                        is_noise_canvas=?, is_noise_client_rect=?, 
                                        is_noise_webgl=?, is_random_screen=? 
                                        WHERE id=?''',
                                   (port, True, True, True, True, False, False, False, False, profile_id))
                    updated_profiles.append({"id": profile_id, "profile_path": profile_path, "port": port})
                else:
                    # Nếu chưa có, thêm mới profile vào database
                    port = generate_random_port()
                    cursor.execute('''INSERT INTO profiles (name, profile_path, remote_debugging_port, browser,
                                    is_masked_font, is_masked_media_device, is_masked_webgl_data, is_noise_audio_context,
                                    is_noise_canvas, is_noise_client_rect, is_noise_webgl, is_random_screen)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (f"Profile_{port}", profile_path, port, "Chrome", True, True, True, True, False, False, False, False))
                    updated_profiles.append({"profile_path": profile_path, "port": port})

        conn.commit()

    return jsonify({"message": "Đã cập nhật các profile cũ từ profiles.txt!", "updated_profiles": updated_profiles})
def api_sql():
    init_db()
    app.run(debug=True)
if __name__ == '__main__':
    api_sql()
