import requests
from datetime import datetime
from Helpers import helper_generic_tags


class DVWA:
    @staticmethod
    def get_user_token(login_page_url: str) -> str:
        with requests.Session() as sess:
            res = sess.get(login_page_url)
            cookies = helper_generic_tags.GetGenericTags.get_tags(res.text, "input", {"type": "hidden"})
            user_token = cookies[0]["value"]

        return user_token

    @staticmethod
    def get_login_cookies(login_page_url: str, level: int = 0):
        security_level = ["low", "medium", "high", "impossible"]

        login_cookies = {
            "PHPSESSID": DVWA.get_user_token(login_page_url),
            "security": security_level[level]
        }

        return login_cookies

    @staticmethod
    def extract_input_values(form) -> dict:
        print(f"type(form): {type(form)}") # Remove debug line

        dict_input_values = {}
        input_tags = form.find_all("input")

        for input_tag in input_tags:
            name = input_tag.get("name")
            value = input_tag.get("value")

            dict_input_values[name] = value

        return dict_input_values

    @staticmethod
    def get_payload_list(file_path: str) -> list:
        with open(file_path, "r") as file:
            sqli_payload_list = file.read().split("\n")
        return sqli_payload_list[:-1]

    @staticmethod
    def save_date_to_file(file_path: str):
        with open(file_path, "a") as file:
            file.write(f"## Date: {datetime.now().strftime('%d-%m-%Y')} ~ Time: {datetime.now().strftime('%H:%M:%S')} ##\n")
            file.write("-"*50 + "\n")

    @staticmethod
    def save_logs_to_file(file_path, result_tuple):
        with open(file_path, "a") as file:
            file.write(f"Scan Result: {result_tuple[0]}\nScan Description: {result_tuple[1]}\n")
            file.write("_" * 50 + "\n")

    # TODO: add a function that will use the brute force module created by elad to get the dvwa credentials (user name and pass)
    @staticmethod
    def get_credentials():
        pass
