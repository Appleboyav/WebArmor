import requests

r = requests.get('https://ilearn.cyber.org.il/')
print(r.content)


# df = pd.DataFrame(all_panda_links)
# print(df)
# print(all_panda_links["Link"])