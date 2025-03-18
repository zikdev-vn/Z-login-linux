#!/bin/bash

# Lấy danh sách cửa sổ chứa "Google Chrome"
windows=$(wmctrl -l | grep -i "Google Chrome")

# Kiểm tra nếu không có cửa sổ Chrome nào
if [ -z "$windows" ]; then
  echo "⚠️ Không tìm thấy cửa sổ trình duyệt Google Chrome!"
  exit 1
fi

# Lấy kích thước màn hình
screen_width=$(xdpyinfo | awk '/dimensions:/ {print $2}' | cut -dx -f1)
screen_height=$(xdpyinfo | awk '/dimensions:/ {print $2}' | cut -dx -f2)

# Kích thước cố định của cửa sổ
win_width=250
win_height=400

# Khoảng cách giữa các cửa sổ
gap=20  # 5px

# Tính số cột có thể đặt trên màn hình
cols=$(( screen_width / (win_width + gap) ))

# Bắt đầu sắp xếp cửa sổ từ vị trí (0,0)
x_pos=0
y_pos=0

# Di chuyển và thay đổi kích thước từng cửa sổ
counter=0
echo "$windows" | while read -r line; do
  window_id=$(echo "$line" | awk '{print $1}')

  echo "📌 Di chuyển cửa sổ ID: $window_id đến ($x_pos, $y_pos)"

  # Kích hoạt và di chuyển cửa sổ
  xdotool windowactivate "$window_id"
  sleep 0.1

  xdotool windowmove "$window_id" "$x_pos" "$y_pos"
  xdotool windowsize "$window_id" "$win_width" "$win_height"

  sleep 0.1  # Chờ cập nhật vị trí

  # Cập nhật vị trí tiếp theo
  x_pos=$((x_pos + win_width + gap))  # Cộng thêm khoảng cách

  # Nếu hết cột, xuống hàng mới
  if (( x_pos + win_width > screen_width )); then
    x_pos=0
    y_pos=$((y_pos + win_height + gap))  # Cộng thêm khoảng cách
  fi

  counter=$((counter + 1))
  
  # Giới hạn tối đa 50 cửa sổ
  if [ "$counter" -ge 50 ]; then
    break
  fi
done

echo "✅ Đã sắp xếp $counter cửa sổ Google Chrome với kích thước $win_width x $win_height và khoảng cách $gap px!"
