import requests
from bs4 import BeautifulSoup

def get_all_noscript(url):

    try:
        # Ensure the URL ends with a slash
        url = url.rstrip('/') + '/'
        # Send a GET request to the index page
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all non-script elements in the HTML
            noscript_elements = soup.find_all("noscript")
            return noscript_elements
        
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to get content. Status code: {response.status_code}")
            return
    #Explain what the Error:
    except requests.RequestException as e:
        print(f"Error: {e}")
        return
    


def find_encrypted_secret_word(non_script_elements, enrypted_secret_word):
    for element in non_script_elements:
        # Check if the encrypted secret word exists in the text content of one of the element
        if enrypted_secret_word in element.get_text():
            return True
    return False
