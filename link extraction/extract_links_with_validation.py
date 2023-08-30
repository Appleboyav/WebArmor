import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

def validate_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This raises an exception for HTTP errors (4xx, 5xx)
        return True
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError):
        return False

def get_all_links_from_url(url: str, domain_name: str) -> set:
    response = requests.get(url)

    if response.ok:
        print('This URL is working properly!')
        print(response)
    else:
        print('This page either does not exist or is out.')
        print(response)

    html_page = BeautifulSoup(response.content, 'html.parser')

    all_links = html_page.find_all('a', {'href': True})

    return all_links

def extract_links(url: str, domain_name: str, all_links: set) -> dict:
    panda_links = {'Link': [], 'Category': []}

    for link in all_links:
        href = link['href']

        if href:
            if domain_name in href:
                panda_links["Link"].append(href)
                panda_links["Category"].append("Internal")

            if href[0] == "#":
                panda_links["Link"].append(f"{url}{href}")
                panda_links["Category"].append("Internal")

            # Addiotion of external links to the dict

            # if href.split(':')[0] in ['https', 'http'] and not domain_name in href:
            #     panda_links["Link"].append(href)
            #     panda_links["Category"].append("External")

    return panda_links

def input_url_and_fetch_domain() -> tuple:
    while True:
        url = input("Please enter a VALID URL to check: ")
        parsed_url = urlparse(url)
        
        if parsed_url.netloc and validate_url(url):
            domain = parsed_url.netloc
            return url, domain
        else:
            print("Invalid URL. Please enter a valid URL.")


def get_internal_links() -> list:
    url, domain = input_url_and_fetch_domain()
    all_links = get_all_links_from_url(url, domain)
    all_panda_links = extract_links(url, domain, all_links)

    # df = pd.DataFrame(all_panda_links)
    # print(df)
    # print(all_panda_links["Link"])

    # return a set of the links
    return sorted(set(all_panda_links["Link"]))


# def main():
#     extracted_links = get_internal_links()
#     print(extracted_links)

# if __name__ == '__main__':
#     main()

#TODO: make the code cleaner (delete) with less things i dont need, add git to this folder and also add noga as an owner "NogaBanana"
