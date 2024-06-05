from pyfiglet import Figlet


def print_ascii_art(text):
    # Create a Figlet object
    figlet = Figlet()

    # Generate ASCII art from the text
    ascii_art = figlet.renderText(text)

    # Print the ASCII art
    print(ascii_art)
