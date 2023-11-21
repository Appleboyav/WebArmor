import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://alf.nu/alert1?world=alert&level=alert0"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Users\test0\Downloads\Chrome Downloads\chrome-win64 zip\chrome-win64\chrome.exe"

# Add the path to the directory containing chromedriver.exe to the system PATH
chrome_path = r"C:\Users\test0\Downloads\Chrome Downloads\chrome-win64 zip\chrome-win64\chrome.exe"
chrome_options.add_argument("webdriver.chrome.driver=" + chrome_path)

wdriver = webdriver.Chrome(options=chrome_options)

page = wdriver.get(url)
sleep(3)
# print(page)

element = wdriver.find_elements(By.NAME, 'body')

print(element)
