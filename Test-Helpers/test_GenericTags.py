import requests
from Helpers import helper_generic_tags as helper

# WORKING

DOMAIN = "owasp.org"
URL = f"https://{DOMAIN}"
response = requests.get(URL)

tags = helper.GetGenericTags.get_tags(response.text, "input", None)
all_links = helper.GetGenericTags.get_tags(response.text, 'a', {'href': True})

print(tags, "\n"+"_"*80)
print([link["href"] for link in all_links if DOMAIN in link['href']])
