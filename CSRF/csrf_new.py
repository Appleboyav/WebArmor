import requests
from Helpers import helper_dvwa
from Helpers import helper_generic_tags
from Attack import base_attack
from Attack import test_attack

URL = "https://example.com/"

"""
1. לזהות redirect ומילים נפוצות של דפי התחברות
2. לבקש מהמשתמש את הפרטי התחברות לאתר
3. להתחבר לאתר עם הפרטים שהוכנסו
4. לעשות redirect בחזרה לכתובת הראשונית
"""
# test123


class CSRF(base_attack.Attack):
    def __init__(self, url):
        super().__init__(url)

    def scan(self):
        # region SCAN

        cookies_dict = {
            "security": "low"
        }

        # cookies_dict = {
        #     # "username": "admin",
        #     # "password": "password",
        #     # "Login": "Login",
        #     "PHPSESSID": user_token,
        #     "security": "low"
        # }

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            # http://127.0.0.1:80/DVWA/login.php
            user_token = helper_dvwa.DVWA.get_user_token(self.url)


            # http://127.0.0.1:80/DVWA/vulnerabilities/csrf/
            csrf_url_page = input("Please enter a website url to check CSRF: ")
            csrf_page_res = sess.get(csrf_url_page)
            print(csrf_page_res.text)
        # endregion

        print(f"Scanning from function: '{CSRF.scan.__name__}'\nClass: {self.__class__.__name__}\nUrl:'{self.url}'\n")
        self.test()

    def test(self):
        t1 = base_attack.Attack(self.url)
        print(type(t1))
        t1.scan()

        t2 = test_attack.TestAttack(self.url)
        print(type(t2))
        t2.scan()


def main():
    csrf_obj = CSRF(URL)
    csrf_obj.scan()


if __name__ == "__main__":
    main()
