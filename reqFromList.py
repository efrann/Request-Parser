## 2_output_temiz.txt dosyasındaki urllere tek tek yeni sekmede açar.

import requests
import webbrowser

def open_urls_with_200_response(url_list):
    for url in url_list:
        try:
            response = requests.get(url)
            webbrowser.open_new_tab(url)
        except requests.exceptions.RequestException as e:
            print(f"İstek hatası: {e}")

# URL listesini txt dosyasından oku
def read_urls_from_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
        # Her bir URL'yi temizle (boşlukları kaldır, satır sonu karakterini kaldır)
        urls = [url.strip() for url in urls]
    return urls

# URL'leri txt dosyasından oku, istek gönder ve yeni sekmelerde aç
url_list = read_urls_from_file('2_output_temiz.txt')
open_urls_with_200_response(url_list)
