from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import validators

class GetLabels:
    @staticmethod
    def is_valid_url(url: str) -> bool:
        return validators.url(url)
    
    @staticmethod
    def get_full_html(url: str) -> str:
        # Validate the URL
        if not GetLabels.is_valid_url(url):
            raise ValueError("Invalid URL")

        # Set up the Chrome driver
        driver_options = Options()
        driver_options.add_argument("headless")
        driver = webdriver.Chrome(options=driver_options)

        try:
            # Open the URL in the browser
            driver.get(url)

            # Wait for the page to fully load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Get the HTML content after JavaScript execution
            full_html = driver.page_source

        except Exception as e:
            print(f"An error occurred while fetching the HTML: {e}")
            full_html = ""

        finally:
            # Close the browser to free up resources
            driver.quit()

        return full_html
    
    @staticmethod
    def extract_labels(full_html: str, label_type="input") -> list(set()):
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(full_html, 'html.parser')
        # Extract the input tags
        html_labels = soup.find_all(label_type)

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
                if not GetLabels.is_valid_url(input_url):
                    print("Invalid URL. Please enter a valid URL.")
                    continue

                full_html = GetLabels.get_full_html(input_url)
                if not full_html:
                    print("Failed to retrieve HTML. Please try again.")
                    continue

                html_labels = GetLabels.extract_labels(full_html)
                return html_labels
                break  # Break out of the loop if everything is successful

            except Exception as e:
                print(f"An error occurred: {e}")

