import requests
from bs4 import BeautifulSoup

CODE_OK = 200

def get_input_tags(links: list) -> None:
    """
    TODO: 
    work on this function later on...
    """
    input_labels = []

    for link in links:
        link_response = requests.get(link)

        if link_response.status_code == CODE_OK:
            soup = BeautifulSoup(link_response.text, 'html.parser')
            input_labels_url = soup.find_all('input')
            input_labels.append(input_labels_url)
        else:               
            print(f"Failed to retrieve the webpage. Status code: {link_response.status_code}")
    
    return input_labels

def get_one_page_input_labels(url: str):
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify)

        # Find all the input labels using BeautifulSoup's find_all method
        input_labels = soup.find_all('input')
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    return input_labels



# test function
def get_input_tags_from_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup.prettify)
            # Find all the input tags using BeautifulSoup's find_all method
            input_tags = soup.find_all('input', {'type': ['text', 'password', 'email', 'number', 'tel', 'url', 'search', 'id']})

            # Return the list of input tags
            return list(set(input_tags))

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
    