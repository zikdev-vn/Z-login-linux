import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor







proxy_urls = [
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
    "https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/All_proxies.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/blob/main/cnfree.txt",
    "https://raw.githubusercontent.com/fyvri/fresh-proxy-list/archive/storage/classic/all.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks4.txt",
    "https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks5.txt",
    "https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/http.txt",
    "https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/https.txt"
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/blob/master/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/blob/master/https.txt",




]




def fetch_proxies_from_urls(urls):
    proxies = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            url_proxies = response.text.splitlines()  # Mỗi dòng là một proxy
            proxies.extend(url_proxies)
            print(f"Lấy dữ liệu từ {url} thành công. Số proxy: {len(url_proxies)}")
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu từ {url}: {e}")
    return proxies

# Ghi danh sách proxy vào file data.txt
def save_proxies_to_file(proxies, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for proxy in proxies:
            file.write(proxy + "\n")
    print(f"Đã lưu {len(proxies)} proxy vào file: {output_file}")

# Đọc danh sách proxy từ file
def read_proxies(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

# Kiểm tra proxy:
# Chỉ in ra và ghi proxy nếu có ít nhất một test_url trả về thành công với tốc độ < 1 giây
def check_and_save_proxy(proxy, output_file, test_urls=None):
    if test_urls is None:
        test_urls = [
            "http://httpbin.org/ip",
            "http://example.com",
            "http://icanhazip.com",
            "http://ifconfig.me",
            "https://api.ipify.org?format=json",
            "https://checkip.amazonaws.com"
        ]
    proxy_dict = {"http": proxy, "https": proxy}
    all_success = True  # Giả sử proxy hoạt động tốt trên tất cả các URL
    for url in test_urls:
        try:
            start_time = time.time()
            response = requests.get(url, proxies=proxy_dict, timeout=9)
            elapsed_time = time.time() - start_time
            # Nếu không trả về mã 200 hoặc thời gian phản hồi >= 1 giây
            if response.status_code != 200 or elapsed_time >= 3:
                print(f"Proxy {proxy} không đạt yêu cầu tại {url} - Tốc độ: {elapsed_time:.2f} giây (Mã: {response.status_code})")
                all_success = False
                break  # Dừng kiểm tra nếu có URL không đạt yêu cầu
            else:
                print(f"Proxy {proxy} hoạt động với {url} - Tốc độ: {elapsed_time:.2f} giây")
        except Exception as e:
            print(f"Proxy {proxy} gặp lỗi tại {url}: {e}")
            all_success = False
            break

    # Nếu proxy vượt qua tất cả các test_url với tốc độ dưới 1 giây, ghi vào file
    if all_success:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(proxy + "\n")
if __name__ == "__main__":
    data_file = "data/data.txt"
    working_file = "data/working_proxies.txt"
    
    # Xóa file nếu đã tồn tại
    if os.path.exists(data_file):
        os.remove(data_file)
    if os.path.exists(working_file):
        os.remove(working_file)
    
    # Lấy proxy từ các URL và lưu vào file data.txt
    all_proxies = fetch_proxies_from_urls(proxy_urls)
    save_proxies_to_file(all_proxies, data_file)
    
    # Đọc danh sách proxy từ file data.txt
    proxies_list = read_proxies(data_file)

    # Danh sách URL kiểm tra, bạn có thể bổ sung thêm URL ở đây
    test_urls = [
        "http://httpbin.org/ip",
        "http://example.com",
        "http://icanhazip.com",
        "http://ifconfig.me",
        "https://api.ipify.org?format=json",
        "https://checkip.amazonaws.com"
    ]

    # Cấu hình số lượng luồng và batch size
    max_threads = 70
    batch_size = 50

    # Sử dụng ThreadPoolExecutor để kiểm tra proxy song song
    with ThreadPoolExecutor(max_threads) as executor:
        for i in range(0, len(proxies_list), batch_size):
            batch = proxies_list[i:i + batch_size]
            executor.map(lambda proxy: check_and_save_proxy(proxy, working_file, test_urls), batch)

    print(f"\nKiểm tra hoàn tất. Proxy hoạt động (tốc độ < 1 giây) được lưu trong file: {working_file}")