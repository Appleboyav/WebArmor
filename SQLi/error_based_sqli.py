from datetime import datetime
import requests
from Helpers import helper_generic_tags
from bs4 import BeautifulSoup as bs
from Helpers import helper_dvwa


class SQLi:
    @staticmethod
    def __extract_input_values(form) -> dict:
        dict_input_values = {}
        input_tags = form.find_all("input")

        for input_tag in input_tags:
            name = input_tag.get("name")
            value = input_tag.get("value")

            dict_input_values[name] = value

        return dict_input_values

    @staticmethod
    def __get_sqli_payload_list(payload_path="error_based_sqli_payloads.txt") -> list:
        with open(payload_path, "r") as file:
            sqli_payload_list = file.read().split("\n")
        return sqli_payload_list[:-1]

    @staticmethod
    def __check_sqli_success(html, sqli_payload) -> tuple:
        words_to_check = ["error", "Error", "You have an error in your SQL syntax", "error in your SQL syntax", "Uncaught mysqli_sql_exception"]

        soup = bs(html.content, "html.parser")
        full_text = soup.get_text()

        for word in words_to_check:
            if word in full_text:
                return (True, f"Your website is vulnerable to Error based SQL Injection attack!\nThis is the payload that was injected <{sqli_payload}>")
            return (False, f"We haven't found your website vulnerable to Error based SQL Injection attack...\nThis is the payload that we tried to inject <{sqli_payload}>")

    @staticmethod
    def main():
        LOG_FILE_PATH = "ErrorBased_SQLi_Logs.txt"
        with open(LOG_FILE_PATH, "a") as file:
            file.write(f"## Date: {datetime.now().strftime('%d-%m-%Y')} ~ Time: {datetime.now().strftime('%H:%M:%S')} ##\n")
            file.write("_"*50 + "\n")

        sqli_payload_list = SQLi.__get_sqli_payload_list()
        # print(f"sqli_payload_list -> {sqli_payload_list}")

        # http://127.0.0.1:80/DVWA/login.php
        login_page_url = input("Enter login page url (to bypass it): ")
        user_token = helper_dvwa.get_user_token(login_page_url)

        cookies_dict = {
            "PHPSESSID": user_token,
            "security": "low"
        }

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            input_url_to_check = input("Please enter a website url you want to check for Error Based SQL Injection: ")
            url_to_check_res = sess.get(input_url_to_check)

            forms = helper_generic_tags.GetGenericTags.get_tags(url_to_check_res.content, "form", None)
            print("*"*100)  # TODO: DEBUG remove

            for form in forms:
                print(f"1 - {form}")  # TODO: DEBUG remove
                for payload in sqli_payload_list:
                    print(f"2 - {payload}")  # TODO: DEBUG remove

                    if form["method"] == "GET":
                        get_input_tags_as_dict = SQLi.__extract_input_values(form)
                        print(f"3 - {get_input_tags_as_dict}")  # TODO: DEBUG remove

                        for key, value in get_input_tags_as_dict.items():
                            if value is None:
                                get_input_tags_as_dict[key] = payload
                        print(f"4 - {get_input_tags_as_dict}")  # TODO: DEBUG remove

                        response = sess.get(input_url_to_check, params=get_input_tags_as_dict)
                        print(f"5 - {response.text}")  # TODO: DEBUG remove

                    is_vulnerable = SQLi.__check_sqli_success(response, payload)
                    print(is_vulnerable[0], is_vulnerable[1])  # TODO: DEBUG remove
                    print("*" * 100)  # TODO: DEBUG remove

                    # Writing the results into a log file
                    with open(LOG_FILE_PATH, "a") as file:
                        file.write(f"Result (has succeed): {is_vulnerable[0]}\nDescription: {is_vulnerable[1]}\n")
                        file.write("_"*50 + "\n")


if __name__ == '__main__':
    SQLi.main()
