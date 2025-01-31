import requests
from Helpers import helper_generic_tags
from urllib.parse import urlparse
# Fully working, no need to do any additional things.


class GetLink:
    @staticmethod
    def __validate_url(url: str) -> bool:
        try:
            response = requests.get(url)
            response.raise_for_status()  # This raises an exception for HTTP errors (4xx, 5xx)
            return True
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
            return False

    @staticmethod
    def __get_all_links_from_url(url: str) -> set:  # Basically a set
        response = requests.get(url)

        if response.ok:
            print(f'This URL is working properly!\nResponse: {response}')
        else:
            print(f'This page either does not exist or is out.\nResponse: {response}')
        
        all_links = helper_generic_tags.GetGenericTags.get_tags(response.content, 'a', {'href': True})

        return all_links

    @staticmethod
    def __extract_links(url: str, domain_name: str, all_links: set) -> list:
        list_links = []

        for link in all_links:
            href = link['href']

            if href:
                if domain_name in href:
                    list_links.append(href)

                if href[0] == "#":
                    list_links.append(f"{url}{href}")

        return list_links

    @staticmethod
    def __input_url_and_fetch_domain() -> tuple:
        while True:
            url = input("Please enter a VALID URL to check: ")
            parsed_url = urlparse(url)
            
            if parsed_url.netloc and GetLink.__validate_url(url):
                domain = parsed_url.netloc
                return (url, domain)
            else:
                print("Invalid URL. Please enter a valid URL.")

    @staticmethod
    def get_internal_links() -> sorted(set()):
        """
        This function will return a sorted(set()) of the website internal links.
        Params:
            - None
            Function will handle user input.
        Return:
            - A sorted(set()) of the website internal links.
        """

        url, domain = GetLink.__input_url_and_fetch_domain()
        all_links = GetLink.__get_all_links_from_url(url)
        all_list_links = GetLink.__extract_links(url, domain, all_links)

        return sorted(set(all_list_links))
