import requests
from Helpers import helper_dvwa
from Helpers import helper_generic_tags
from Attack import base_attack
from Attack import test_attack

URL = "https://exampasdasdle.com/"

"""
1. לזהות redirect ומילים נפוצות של דפי התחברות
2. לבקש מהמשתמש את הפרטי התחברות לאתר
3. להתחבר לאתר עם הפרטים שהוכנסו
4. לעשות redirect בחזרה לכתובת הראשונית
"""


class CSRF(base_attack.Attack):
    def __init__(self, url):
        super().__init__(url)

    def scan(self):
        # # sess = requests.Session()
        #
        # # http://127.0.0.1:80/DVWA/login.php
        # login_page_url = input("Enter login page url (to bypass it): ")
        # user_token = helper_dvwa.DVWA.get_user_token(login_page_url)
        #
        # cookies_json = {
        #     # "username": "admin",
        #     # "password": "password",
        #     # "Login": "Login",
        #     "PHPSESSID": user_token,
        #     "security": "low"
        # }
        # print(cookies_json)
        #
        # with requests.Session() as sess:
        #     sess.cookies.update(cookies_json)
        #
        #     # http://127.0.0.1:80/DVWA/vulnerabilities/csrf/
        #     # http://127.0.0.1:80/DVWA/vulnerabilities/sqli/
        #     csrf_url_page = input("Please enter a website url to check CSRF: ")
        #     csrf_page_res = sess.get(csrf_url_page)
        #     print(csrf_page_res.text)

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
