from Helpers import helper_generic_tags
import validators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GetLabels:
    @staticmethod
    def __is_url_valid(url: str) -> bool:
        return validators.url(url)
    
    @staticmethod
    def __get_full_html(url: str) -> str:
        # Validate the URL
        if not GetLabels.__is_url_valid(url):
            raise ValueError("Invalid URL")

        driver_options = Options()
        driver_options.add_argument("headless")  # Headless = work in the background
        driver = webdriver.Chrome(options=driver_options)

        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            full_html = driver.page_source

        except Exception as e:
            print(f"An error occurred while fetching the HTML: {e}")
            full_html = ""

        finally:
            driver.quit()

        return full_html
    
    @staticmethod
    def __extract_labels(full_html: str, label_type="input") -> list(set()):  # input is the default label type
        html_labels = helper_generic_tags.GetGenericTags.get_tags(full_html, label_type, None)

        return list(set(html_labels))

    '''
    Ask Noga what to do with the fact that we are going to make the project as a website, because if we do, we need to make sure we send
    the user a response incase the url he entered is invalid.
    what/how should  we make it work with the website???
    '''
    @staticmethod
    def get_labels():
        """
        This function will return a list(set()) of HTML input tags.
        Params:
            - None
            Function will handle user input.
        Return:
            - A list(set()) of HTML input tags.
        """

        while True:
            input_url = input("Enter a website url: ")

            try:
                # Check if the URL is valid
                if not GetLabels.__is_url_valid(input_url):
                    print("Invalid URL. Please enter a valid URL: ")
                    continue

                full_html = GetLabels.__get_full_html(input_url)
                if not full_html:
                    print("Failed to retrieve HTML. Please try again.")
                    continue

                html_labels = GetLabels.__extract_labels(full_html)
                return html_labels

            except Exception as e:
                print(f"An error occurred: {e}")

    @staticmethod
    def get_labels_from_html(html):
        input_tags = GetLabels.__extract_labels(html)
        return input_tags
