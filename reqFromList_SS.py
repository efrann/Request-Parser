import requests
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_urls_with_200_response(url_list):
    for url in url_list:
        try:
            response = requests.get(url)
            webbrowser.open_new_tab(url)
            take_screenshot(url)
        except requests.exceptions.RequestException as e:
            print(f"Req Error: {e}")

def take_screenshot(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot(f"{url.replace('/', '_')}.png")
    driver.quit()

# URLler 
def read_urls_from_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
        # URL satir sonlari
        urls = [url.strip() for url in urls]
    return urls

url_list = read_urls_from_file('test.txt')
open_urls_with_200_response(url_list)
