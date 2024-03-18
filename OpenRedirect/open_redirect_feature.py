import requests
from Helpers import helper_dvwa

BASE_URL = "http://127.0.0.1:80/DVWA"
COOKIES_JSON = {
    "PHPSESSID": helper_dvwa.DVWA.get_user_token(f"{BASE_URL}/login.php"),
    "security": "low"
}


def check_open_redirect(url):
    # TODO: elad check if the code works
    # Pass the login page: "http://127.0.0.1:80/DVWA/index.php"
    with requests.Session() as sess:
        sess.cookies.update(COOKIES_JSON)
        index_page_response = sess.get(f"{BASE_URL}/index.php")
        payload = {'redirect_param': ''}
        response = sess.get(url, params=payload, allow_redirects=False)
        print(response.status_code)

        if response.status_code == 302 and 'Location' in response.headers:
            print(f'open redirect detected. Redirect location: {response.headers["Location"]}')
        else:
            print('No open redirect vulnerability detected.')


# http://localhost/DVWA/vulnerabilities/open_redirect/
# https://owasp.org/www-project-juice-shop/
check_open_redirect('http://localhost/DVWA/vulnerabilities/open_redirect/')