import requests
from Helpers import helper_dvwa
from Attack import base_attack

BASE_URL = "http://127.0.0.1:80/DVWA"
URL = 'http://localhost/DVWA/vulnerabilities/open_redirect/'
COOKIES_JSON = {
    "PHPSESSID": helper_dvwa.DVWA.get_user_token(f"{BASE_URL}/login.php"),
    "security": "low"
}

class OpenRedirect(base_attack.Attack):

    def __init__(self, url):
        super().__init__(url)

    def scan(self):
        with requests.Session() as sess:
            sess.cookies.update(COOKIES_JSON)
            index_page_response = sess.get(f"{BASE_URL}/index.php")
            payload = {'redirect_param': ''}
            response = sess.get(self.url, params=payload, allow_redirects=False)
            print(response.status_code)

            if response.status_code == 302 and 'Location' in response.headers:
                print(f'Open redirect detected. Redirect location: {response.headers["Location"]}')
            else:
                print('No open redirect vulnerability detected.')


def main():
    openRedirect = OpenRedirect(URL)
    OpenRedirect.scan(openRedirect)


if __name__ == "__main__":
    main()
