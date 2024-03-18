import requests
from Helpers import helper_dvwa
from Helpers import helper_generic_tags
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CSRF:
    @staticmethod
    def check_csrf_success():
        pass

    @staticmethod
    def main():
        result = ()

        # http://127.0.0.1:80/DVWA/login.php
        login_page_url = input("Enter login page url (to bypass it): ")
        user_token = helper_dvwa.DVWA.get_user_token(login_page_url)

        cookies_dict = {
            "PHPSESSID": user_token,
            "security": "low"
            # "security": "medium"
        }

        # print(f"{__name__}:{id(cookies_dict)}:{cookies_dict}")  #TODO: remove debug
        # cookies_dict["security"] = "impossible"
        print(f"{__name__}:{id(cookies_dict)}:{cookies_dict}")  #TODO: remove debug

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            # http://127.0.0.1:80/DVWA/vulnerabilities/csrf/
            url = input("Please enter a website url to check CSRF: ")
            res = sess.get(url)
            print(res.text)

            forms = helper_generic_tags.GetGenericTags.get_tags(res.text, "form", {})

            for form in forms:
                form = str(form)
                print(form)
                print(type(form))

                if "user_token" in form:
                    scan_result = False, "CSRF attack wasn't found."
                else:
                    scan_result = True, "CSRF attack was found in your website."

            print(scan_result)




if __name__ == "__main__":
    CSRF.main()
