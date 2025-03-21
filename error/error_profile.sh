#!/bin/bash

# Định nghĩa database SQLite
DB_FILE="profiles.db"

# Lấy danh sách profile từ SQLite
PROFILE_LIST=$(python3 - <<END
import sqlite3
import json

DB_FILE = "$DB_FILE"

def get_profiles():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT profile_path FROM profiles")
        profiles = [row[0] for row in cursor.fetchall()]
    print(json.dumps(profiles))

get_profiles()
END
)

# Chuyển danh sách profile từ JSON sang mảng Bash
PROFILES=$(echo "$PROFILE_LIST" | jq -r '.[]')

# Kiểm tra và xóa các liên kết tượng trưng trong từng profile
for PROFILE_PATH in $PROFILES; do
    if [ -d "$PROFILE_PATH" ]; then
        echo "Đang kiểm tra profile: $PROFILE_PATH"
        
        # Kiểm tra và xóa các liên kết tượng trưng nếu tồn tại
        for FILE in SingletonLock SingletonSocket SingletonCookie; do
            if [ -L "$PROFILE_PATH/$FILE" ]; then
                echo "Liên kết $FILE tồn tại trong $PROFILE_PATH, đang xóa..."
                rm -f "$PROFILE_PATH/$FILE"
            fi
        done
    else
        echo "Profile không tồn tại: $PROFILE_PATH"
    fi
done

echo "✅ Kiểm tra và xóa các liên kết tượng trưng hoàn tất!"
