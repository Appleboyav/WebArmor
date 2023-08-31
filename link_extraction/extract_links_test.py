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

    # print("_"*20)

    html_page = BeautifulSoup(response.content, 'html.parser')
    # print(html_page.prettify())

    all_links = html_page.find_all('a', {'href': True})
    print(type(all_links))
    # print(all_links) #debug

    return all_links

def extract_links(url:str, domain_name:str, all_links:set) -> dict:
    panda_links = {'link':[], 'category':[]}

    for link in all_links:
        # print(link) #debug
        href = link['href']

        if href:
            if domain_name in href:
                # print(href)
                # print(f"url: {url} _____ href: {href}")
                panda_links["link"].append(href)
                panda_links["category"].append("Internal")

            if href[0] == "#":
                panda_links["link"].append(f"{url}{href}")
                panda_links["category"].append("Internal")

            if href.split(':')[0] in ['https','http'] and not domain_name in href:
                panda_links["link"].append(href)
                panda_links["category"].append("External")
    return panda_links

def input_url_and_fetch_domain() -> tuple:
    url =  input("Please enter a URL to check: ")
    domain = url.split('/')[2]
    return url, domain

def main():
    url, domain = input_url_and_fetch_domain()
    all_links = get_all_links_from_url(url, domain)
    all_panda_links = extract_links(url, domain, all_links)


if __name__ == '__main__':
    main()