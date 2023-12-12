import requests
from bs4 import BeautifulSoup

# ! not working

# Target URL
url = "http://127.0.0.1:80/DVWA/login.php"

# Login credentials
payload = {
    "username": "admin",
    "password": "password",
    "Login": "Login",
}

# Create a session to persist the login session
session = requests.Session()

# Make a POST request to the login page with the credentials
response = session.post(url, data=payload)

# Check if login was successful
if "Login failed" in response.text:
    print("Login failed. Please check your credentials.")
else:
    print("Login successful!")

# Now, you can continue to make requests using the open session
# For example, you can make a GET request to the SQLi vulnerability page
sqli_url = "http://127.0.0.1:80/DVWA/vulnerabilities/sqli/"
response = session.get(sqli_url)

# Do whatever you want with the open connection
print(response.text)

# Don't forget to close the session when you're done
session.close()
