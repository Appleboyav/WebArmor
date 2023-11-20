import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_all_links_from_url(url:str, domain_name:str) -> set:
    response = requests.get(url)

    if response.ok:
        print('This URL is working properly!')
        print(response)
    else:
        print('This page either does not exist or is out.')
        print(response)
        # return None #debug

    html_page = BeautifulSoup(response.content, 'html.parser')

    all_links = html_page.find_all('a', {'href': True})

    return all_links

def extract_links(url:str, domain_name:str, all_links:set) -> dict:
    panda_links = {'Link':[], 'Category':[]}

    for link in all_links:
        href = link['href']

        if href:
            if domain_name in href:
                panda_links["Link"].append(href)
                panda_links["Category"].append("Internal")

            if href[0] == "#":
                panda_links["Link"].append(f"{url}{href}")
                panda_links["Category"].append("Internal")


            # if href.split(':')[0] in ['https','http'] and not domain_name in href:
            #     panda_links["Link"].append(href)
            #     panda_links["Category"].append("External")

    return panda_links

def input_url_and_fetch_domain() -> tuple:
    url =  input("Please enter a VALID URL to check: ")
    domain = url.split('/')[2]

    return url, domain

def main():
    url, domain = input_url_and_fetch_domain()
    all_links = get_all_links_from_url(url, domain)
    all_panda_links = extract_links(url, domain, all_links)
    
    df = pd.DataFrame(all_panda_links)
    # print(df)
    print(all_panda_links["Link"])

if __name__ == '__main__':
    main()