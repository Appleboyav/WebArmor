import requests
from bs4 import BeautifulSoup


res = requests.get("https://appleboyav.github.io/appleboyav21.github.io/PassAuth.html")
# res = requests.get("https://appleboyav.github.io/appleboyav21.github.io/")
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify)