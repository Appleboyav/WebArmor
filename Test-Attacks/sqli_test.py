# import SQLi.ErrorBased.error_based_sqli as SQLI
from SQLi.ErrorBased.error_based_sqli import SQLi

URL = "https://example.com/"


def main():
    input_url_to_check = input("Please enter a website url you want to check for Error Based SQL Injection: ")

    sqli_atk = SQLi(input_url_to_check)
    sqli_atk.scan()


if __name__ == "__main__":
    main()
