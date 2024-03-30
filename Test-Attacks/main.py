from CSRF import csrf_new
from SQLi.ErrorBased import error_based_sqli
import pyfiglet_ascii_art
from enum import Enum


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


def get_user_input() -> int:
    lowest_value = (min(Attack_Choice, key=lambda x: x.value)).value
    highest_value = (max(Attack_Choice, key=lambda x: x.value)).value

    while True:
        try:
            user_input = int(input("Please choose one of the options above: "))

            if lowest_value <= user_input <= highest_value:
                return user_input
            else:
                print(f"Invalid choice. Please enter a value between {lowest_value} and {highest_value}")

        except ValueError:
            print("Invalid input, please enter a valid integer.")


def main():
    welcome_screen()
    menu()
    user_choice = get_user_input()
    print(user_choice)


if __name__ == "__main__":
    main()
