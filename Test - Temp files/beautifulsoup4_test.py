from bs4 import BeautifulSoup
import requests

url = "https://owasp.org/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content)

title = soup.find('title').text
print(title)

link = soup.find('a')
link_href = link['href']
link_text = link.text

for link in soup.find_all('a'):
    print(link['href'])
