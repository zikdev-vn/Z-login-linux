import requests
import re

# Link đầy đủ của extension từ Chrome Web Store
url_input = "https://chromewebstore.google.com/detail/bless/pljbjcehnhcnofmkdbjolghdcjnmekia?hl=vi&authuser=0"

# Trích xuất ID từ URL
match = re.search(r"/detail/[^/]+/([a-z]{32})", url_input)
if match:
    EXTENSION_ID = match.group(1)
    print(f"ID của extension: {EXTENSION_ID}")

    # Phiên bản Chrome (Cập nhật nếu cần)
    CHROME_VERSION = "120.0"

    # Tạo link tải file .crx
    crx_url = f"https://clients2.google.com/service/update2/crx?response=redirect&prodversion={CHROME_VERSION}&x=id%3D{EXTENSION_ID}%26installsource%3Dondemand%26uc"

    # Tải file về
    response = requests.get(crx_url, stream=True)
    if response.status_code == 200:
        with open(f"{EXTENSION_ID}.crx", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Tải thành công: {EXTENSION_ID}.crx")
    else:
        print("Không thể tải file! Kiểm tra lại ID hoặc phiên bản Chrome.")
else:
    print("Không tìm thấy ID trong URL!")
