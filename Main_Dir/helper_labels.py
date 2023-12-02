import helper_generic_tags
import validators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetLabels:
    @staticmethod
    def __is_valid_url(url: str) -> bool:
        return validators.url(url)
    
    @staticmethod
    def __get_full_html(url: str) -> str:
        # Validate the URL
        if not GetLabels.__is_valid_url(url):
            raise ValueError("Invalid URL")

        driver_options = Options()
        driver_options.add_argument("headless") #headless = work in the background 
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
    def __extract_labels(full_html: str, label_type="input") -> list(set()):
        html_labels = helper_generic_tags.GenericGetTags.get_tags(full_html, label_type, None)

        return list(set(html_labels))

    '''
    # ! Ask noga what to do with the fact that we are going to make the project as a website, because if we do, we need to make sure we send
    the user a response incase the url he entered is invalid.
    what/how should  we make it work with the website???
    '''
    @staticmethod
    def wrapper_get_lables_from_html():
        while True:
            input_url = input("Enter a website url: ")

            try:
                # Check if the URL is valid
                if not GetLabels.__is_valid_url(input_url):
                    print("Invalid URL. Please enter a valid URL.")
                    continue

                full_html = GetLabels.__get_full_html(input_url)
                if not full_html:
                    print("Failed to retrieve HTML. Please try again.")
                    continue

                html_labels = GetLabels.__extract_labels(full_html)
                return html_labels
                break  # Break out of the loop if everything is successful

            except Exception as e:
                print(f"An error occurred: {e}")
