import requests
from urllib.parse import quote
from Helpers import helper_generic_tags


class SQLi:

    USER_PARAMETER_MARKDOWN = "*HERE*"

    @staticmethod
    def __get_user_token(login_page_url) -> str:
        with requests.Session() as sess:
            res = sess.get(login_page_url)
            cookies = helper_generic_tags.GetGenericTags.get_tags(res.content, "input", {"type": "hidden"})
            user_token = cookies[0]["value"]

            return user_token

    @staticmethod
    def __attack_success(control_response, sqli_response):
        if control_response.content != sqli_response.content:
            return True
        return False

    @staticmethod
    def main():
        control_query = ""
        sqli_query = ""

        # http://127.0.0.1:80/DVWA/login.php
        login_page_url = input("Enter login page url: ")
        user_token = SQLi.__get_user_token(login_page_url)

        cookies_dict = {
            "PHPSESSID": user_token,
            "security": "low"
        }

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            # Input the desire url to check
            input_url = input(f"Please enter the url you want to check.\nEnter Put {SQLi.USER_PARAMETER_MARKDOWN} where the parameter/s would be: ")

            # Get control response
            control_request = input_url.replace(SQLi.USER_PARAMETER_MARKDOWN, quote(control_query))
            control_response = sess.get(control_request)

            # Get sqli response
            sqli_request = input_url.replace(SQLi.USER_PARAMETER_MARKDOWN, quote(sqli_query))
            sqli_response = sess.get(sqli_request)

            success = SQLi.__attack_success(control_response, sqli_response)
            if success:
                print("SQL Injection attack has succeeded!")
            else:
                print("SQL Injection attack did not succeed...")


if __name__ == '__main__':
    SQLi.main()
