import requests
from Helpers import helper_dvwa

BASE_URL = "http://127.0.0.1:80/DVWA"
SCRIPT = "<script>alert('XSS')</script>"
INJECT_DATA = {"name": SCRIPT, "submit": "Submit"}
COOKIES_JSON = {
    "PHPSESSID": helper_dvwa.get_user_token(f"{BASE_URL}/login.php"),
    "security": "low"
}


def main():
    with requests.Session() as sess:
        sess.cookies.update(COOKIES_JSON)

        url = input("Enter the URL you want to check for an XSS vulnerability:")
        print("Enter the structure of the form you want to check for an XSS vulnerability:  ")
        print("According to the structure of a dictionary, Example: {'name' : ori, 'submit' : 'Submit'}")
        string_form = input("")

        # Get the structure of the form as a dictionary -  change type from string to dictionary:
        dictionary_form = eval(string_form)

        # Get the first key in the dictionary
        first_key = list(dictionary_form.keys())[0]

        # Replace the value in the first place in the dictionary we got to the SCRIPT :
        dictionary_form[first_key] = SCRIPT

        # Inserting the data and in put the script in the name filed:
        res = sess.get(f"{BASE_URL}/index.php", params=dictionary_form)

        # Check i the script saved in the website:
        if SCRIPT in res.text:
            print("Your website is vulnerable to XSS Injection attack!")
        else:
            print("Your website is NOT vulnerable to XSS Injection attack.")


if __name__ == "__main__":
    main()
