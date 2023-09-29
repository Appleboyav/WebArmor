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
    headers = {'User-Agent:':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    
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
        headers = {'User-Agent:':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
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
    
def function(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    
    res = requests.get(url)

    if res.ok:
        html_page = BeautifulSoup(res.content, 'html.parser')
        html_inputs = html_page.find_all('input', {'type': ['text','password', 'textarea']})
        print(html_page.prettify)

        return list(set(html_inputs))
    else:
        return "not found"
    