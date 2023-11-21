from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_full_html(url):
    # Set up the Chrome driver with a custom user-agent
    options = Options()
    driver = webdriver.Chrome(options=options)

    try:
        # Open the URL in the browser
        driver.get(url)

        # Wait for the page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Get the HTML content after JavaScript execution
        full_html = driver.page_source

    finally:
        # Close the browser to free up resources
        driver.quit()

    return full_html

def extract_inputs(full_html):
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(full_html, 'html.parser')
    # print(soup.prettify)
    # Extract the input tags
    # html_inputs = soup.find_all('input', {'type': ['text', 'password', 'textarea']})
    html_inputs = soup.find_all('input')

    return list(set(html_inputs))

def main():
    # url = "https://alf.nu/alert1?world=alert&level=alert0"  # Replace with the URL of the website you want to scrape
    url = "https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content"  
    full_html = get_full_html(url)
    html_inputs = extract_inputs(full_html)

    # Print or do something with the extracted input tags
    print(html_inputs)

if __name__ == "__main__":
    main()
