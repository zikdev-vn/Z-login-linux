#!/bin/bash

# Lấy danh sách các cửa sổ chứa "Google Chrome"
windows=$(wmctrl -l | grep -i "Google Chrome")

# Kiểm tra nếu không có cửa sổ "Google Chrome" nào
if [ -z "$windows" ]; then
  echo "⚠️ Không tìm thấy cửa sổ trình duyệt Google Chrome!"
  exit 1
fi

# Đếm số lượng cửa sổ
window_count=$(echo "$windows" | wc -l)

# Lấy chiều rộng và chiều cao màn hình
screen_width=$(xdpyinfo | grep 'dimensions:' | awk '{print $2}' | cut -d 'x' -f 1)
screen_height=$(xdpyinfo | grep 'dimensions:' | awk '{print $2}' | cut -d 'x' -f 2)

# Yêu cầu người dùng nhập chiều rộng và chiều cao cho cửa sổ
echo "Nhập chiều rộng của cửa sổ mong muốn (mặc định: $((screen_width / 5))):"
read -r win_width
if [ -z "$win_width" ]; then
  win_width=$((screen_width / 5))   # Mặc định: chia màn hình thành 5 cột
fi

echo "Nhập chiều cao của cửa sổ mong muốn (mặc định: $((screen_height / 10))):"
read -r win_height
if [ -z "$win_height" ]; then
  win_height=$((screen_height / 10))  # Mặc định: chia màn hình thành 10 hàng
fi

# Vị trí bắt đầu
x_pos=0
y_pos=0

# Di chuyển và thay đổi kích thước cửa sổ
counter=1
echo "$windows" | while read -r line; do
  # Lấy ID cửa sổ từ dòng đầu tiên của danh sách
  window_id=$(echo "$line" | awk '{print $1}')
  
  # Di chuyển cửa sổ với xdotool
  xdotool windowmove "$window_id" "$x_pos" "$y_pos"
  xdotool windowsize "$window_id" "$win_width" "$win_height"
  
  # Cập nhật vị trí (di chuyển cửa sổ tiếp theo)
  x_pos=$((x_pos + win_width))
  if ((x_pos + win_width > screen_width)); then
    x_pos=0
    y_pos=$((y_pos + win_height))
  fi

  counter=$((counter + 1))
  
  # Nếu đã xử lý hết số lượng cửa sổ tối đa (50)
  if [ "$counter" -gt 50 ]; then
    break
  fi
done

echo "Đã sắp xếp $counter cửa sổ Google Chrome."
