import requests
from bs4 import BeautifulSoup

# ! not working

# Set the URL of the login page
login_url = "http://127.0.0.1:80/DVWA/login.php"  # Replace with the actual URL

# Set the login credentials
payload = {
    "username": "admin",
    "password": "password",
    "Login": "Login",  # This value may need to match the actual name of the submit button
    "user_token": "982b2f073c40f2b48c707fea0a00d5a6"
}

# Create a session
session = requests.Session()

# Send a POST request to the login page to authenticate
response = session.post(login_url, data=payload)

# Check if the login was successful
if "CSRF token is incorrect" not in response.text:
    print("Login successful!")
else:
    print("Login failed.")

# Now you can use the 'session' object to make subsequent requests while keeping the session alive
# For example, you can make requests to other pages within the authenticated session

# Example: Get the content of another page after login
other_page_url = "http://127.0.0.1:80/DVWA/index.php"  # Replace with the actual URL
other_page_response = session.get(other_page_url)

# Parse the HTML content of the response if needed
soup = BeautifulSoup(other_page_response.text, "html.parser")
# Perform actions on the parsed HTML content as needed
print(soup.prettify)
# Close the session when done
session.close()
