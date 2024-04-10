from enum import Enum
import pyfiglet_ascii_art
import validators

from SQLi.ErrorBased import error_based_sqli
from CSRF import csrf_scan
from BruteForce import brute_force_feature
from XSS import xss


class Attack_Choice(Enum):
    SQL_INJECTION = 1
    CSRF = 2
    XSS = 3
    BRUTE_FORCE = 4


def welcome_screen() -> None:
    pyfiglet_ascii_art.print_ascii_art("WebArmor")
    print("Welcome to our website scanner!")


def menu() -> None:
    print("You can scan this attacks on you website")
    for item in Attack_Choice:
        print(f"\t{item.value}.\t{item.name}")


def get_user_choice() -> int:
    lowest_value: int = (min(Attack_Choice, key=lambda x: x.value)).value
    highest_value: int = (max(Attack_Choice, key=lambda x: x.value)).value

    while True:
        try:
            user_input: int = int(input("Please choose one of the options above: "))

            if lowest_value <= user_input <= highest_value:
                return user_input
            else:
                print(f"Invalid choice. Please enter a value between {lowest_value} and {highest_value}")

        except ValueError:
            print("Invalid input, please enter a valid integer.")


def validate_url() -> str:
    while True:
        url_to_scan: str = input("Please enter the url to scan:\n")

        if validators.url(url_to_scan):
            return url_to_scan
        else:
            print("Invalid URL. Please try again.")


def main():
    welcome_screen()
    menu()
    user_choice: int = get_user_choice()
    print(user_choice)

    # http://127.0.0.1/DVWA/vulnerabilities/sqli/  -> sqli
    # http://127.0.0.1/DVWA/vulnerabilities/csrf/  -> csrf
    # http://127.0.0.1/DVWA/                       -> xss
    # http://127.0.0.1/DVWA/vulnerabilities/brute/ -> brute
    url_to_scan: str = validate_url()

    # Create a list of attack objects and based on the user choice use that object and run it's scan function
    attacks_obj_list = [error_based_sqli.SQLi, csrf_scan.CSRF, xss.XSS, brute_force_feature.BruteForce]
    attack_choice = attacks_obj_list[user_choice-1](url_to_scan)  # Create a function to get url from user.

    # Run scan attack
    attack_res = attack_choice.scan()
    print(attack_res)


if __name__ == "__main__":
    main()
