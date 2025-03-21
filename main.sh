#!/bin/bash

# Đảm bảo có đúng 10 proxy trong proxys.txt
counter=1  # Biến đếm số profile
remote_port=9222  # Đặt cổng remote debugging mặc định

# Đọc từng dòng proxy từ file proxys.txt
while IFS= read -r proxy; do
  # Kiểm tra nếu proxy không phải là dòng trống và số profile không vượt quá 10
  if [[ ! -z "$proxy" && $counter -le 10 ]]; then
    # Kiểm tra loại proxy (SOCKS4, SOCKS5, HTTP)
    echo "Đang kiểm tra proxy: $proxy..."
    
    # Kiểm tra kết nối tới proxy (sử dụng curl để kiểm tra)
    if curl --silent --max-time 10 --proxy "$proxy" http://www.google.com > /dev/null; then
      echo "Proxy $proxy hoạt động tốt!"
      
      # Mở Chrome với proxy cho profile tương ứng và các options thêm vào
      google-chrome --proxy-server="$proxy" \
                    --user-data-dir="/path/to/profile_chrome" \
                    --profile-directory="profile_$counter" \
                    --window-size=300,490 \
                    --force-device-scale-factor=0.75 \
                    --remote-debugging-port=$remote_port &
      
      # Ghi cổng remote debugger vào file (remote_port.txt)
      echo "Remote debugging port for profile $counter: $remote_port" >> remote_port.txt
      
      # Tăng số profile và remote port
      ((counter++))  # Tăng số profile sau mỗi lần mở Chrome
      ((remote_port++))  # Tăng cổng remote debugging cho lần sau
    else
      echo "Lỗi: Proxy $proxy không thể kết nối. Bỏ qua proxy này."
    fi
  fi
done < working_proxies.txt
