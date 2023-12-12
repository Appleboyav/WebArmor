import requests

# ! not working


# Target URL
url = "http://127.0.0.1:80/DVWA/login.php"

# Login credentials
payload = {
    "username": "admin",
    "password": "password",
    "Login": "Login",
}

# Custom headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "PHPSESSID=1o4bq0as8krq2ckdatmaesbhhq; security=low",
    "Host": "localhost",
    "Origin": "http://localhost",
    "Referer": "http://localhost/DVWA/login.php",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    "sec-ch-ua-mobile": "?0",
}

# Create a session to persist the login session
session = requests.Session()

# Make a POST request to the login page with the credentials and custom headers
response = session.post(url, data=payload, headers=headers)

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

