from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def get_all_input_tags(url):
    # Create a new instance of the Firefox driver (you can use other drivers like Chrome, Safari, etc.)
    driver = webdriver.Chrome()
    
    # Navigate to the given URL
    driver.get(url)
    sleep(5)
    
    # Find all input tags on the page
    input_tags = driver.find_elements(By.NAME, 'body')

    # Print the attributes of each input tag
    for input_tag in input_tags:
        print("Input Tag Attributes:")
        print("Type:", input_tag.get_attribute('type'))
        print("Name:", input_tag.get_attribute('name'))
        print("ID:", input_tag.get_attribute('id'))
        print("Value:", input_tag.get_attribute('value'))
        print("")

    print(input_tags)
    # Close the browser window
    driver.quit()

# Replace 'your_url_here' with the actual URL you want to inspect
url_to_scrape = 'https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content'
get_all_input_tags(url_to_scrape)
