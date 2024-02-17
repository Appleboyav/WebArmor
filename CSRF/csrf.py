from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helpers import helper_dvwa


class CSRF:
    @staticmethod
    def setup_selenium_driver(cookies_dict, url="http://127.0.0.1:80/DVWA/vulnerabilities/csrf"):
        driver_options = Options()
        # driver_options.add_argument("headless")  # Headless = work in the background
        driver = webdriver.Chrome(options=driver_options)
        # for key, val in cookies_dict.items():
        #     driver.add_cookie({'name': key, 'value': val})
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            full_html = driver.page_source

        except Exception as e:
            print(f"An error occurred while fetching the HTML: {e}")
            full_html = ""

        finally:
            driver.quit()

        return full_html

    @staticmethod
    def check_csrf_success():
        pass

    @staticmethod
    def main():
        # http://127.0.0.1:80/DVWA/login.php
        login_page_url = input("Enter login page url (to bypass it): ")
        user_token = helper_dvwa.DVWA.get_user_token(login_page_url)

        cookies_dict = {
            "PHPSESSID": user_token,
            "security": "low"
            # "security": "medium"
        }
        print(cookies_dict)
        print(CSRF.setup_selenium_driver(cookies_dict))
        # chrome_driver = CSRF.setup_selenium_driver(cookies_dict)
        # chrome_driver.get("http://127.0.0.1:80/DVWA/vulnerabilities/csrf")



if __name__ == "__main__":
    CSRF.main()
