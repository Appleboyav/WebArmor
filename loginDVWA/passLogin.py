from selenium import webdriver
from selenium.webdriver.support.ui import Select

BASE_URL = "http://127.0.0.1:80/DVWA"

username = 'admin'
password = 'password'


def pass_login():

    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    # Find the username and password input fields on the login page using various locators
    username_field = driver.find_element('name', 'username')  
    password_field = driver.find_element('name', 'password') 

    # Enter the username and password into their respective fields
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element('name', 'Login')  
    login_button.click()

