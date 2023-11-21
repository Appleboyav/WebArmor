# ! This code works for that current websites -> https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content ; https://juice-shop.herokuapp.com/#/search
# todo: make the code better and cleaner

from selenium import webdriver
from bs4 import BeautifulSoup
import time

option_headless = webdriver.ChromeOptions()
# allows the browser to open as a process in the background
option_headless.add_argument("headless")

# start web browser
browser = webdriver.Chrome(options=option_headless)

# url = "https://juice-shop.herokuapp.com/#/search"
url = "https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content"

# get source code
browser.get(url)

html = browser.page_source
time.sleep(8)
# print(html)

browser.close()

soup = BeautifulSoup(html, 'html.parser')
user_input = input('Enter the tag you want to search for: ')
inputs = soup.find_all(user_input)
print(inputs)

# if inputs:
#     first_input_id = inputs[0].get('id')
#     print("ID of the first input:", first_input_id)
# else:
#     print("No input elements found on the page.")

# print(inputs[0].id)
# print(inputs[0].name)
