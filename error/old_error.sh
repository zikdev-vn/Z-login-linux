#!/bin/bash

# cai nay dung cho thang nao doi ten thiet bi ma bi loi profile giong tao :))






# Định nghĩa đường dẫn thư mục chứa các profile (đường dẫn tuyệt đối)
PROFILE_DIR="/home/zik/Documents/auto/profile_chrome"

# Kiểm tra thư mục có tồn tại không
for i in {1..10}
do
    PROFILE_NAME="profile_$i"
    PROFILE_PATH="$PROFILE_DIR/$PROFILE_NAME"
    
    if [ -d "$PROFILE_PATH" ]; then
        echo "Đang kiểm tra profile: $PROFILE_NAME"
        
        # Kiểm tra các liên kết tượng trưng và xóa nếu tồn tại
        if [ -L "$PROFILE_PATH/SingletonLock" ]; then
            echo "Liên kết SingletonLock tồn tại trong $PROFILE_NAME, đang xóa..."
            rm -f "$PROFILE_PATH/SingletonLock"
        fi
        
        if [ -L "$PROFILE_PATH/SingletonSocket" ]; then
            echo "Liên kết SingletonSocket tồn tại trong $PROFILE_NAME, đang xóa..."
            rm -f "$PROFILE_PATH/SingletonSocket"
        fi
        
        if [ -L "$PROFILE_PATH/SingletonCookie" ]; then
            echo "Liên kết SingletonCookie tồn tại trong $PROFILE_NAME, đang xóa..."
            rm -f "$PROFILE_PATH/SingletonCookie"
        fi
    else
        echo "Profile $PROFILE_NAME không tồn tại trong thư mục $PROFILE_DIR."
    fi
done

echo "Kiểm tra và xóa các liên kết tượng trưng hoàn tất!"

