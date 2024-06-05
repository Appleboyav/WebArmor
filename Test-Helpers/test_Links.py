from Helpers import helper_links as helper


ls = helper.GetLink.get_internal_links()
print("ls is: ", ls)
print("ls TYPE is: ", type(ls))

# ls2 = helper.GetLink.__validate_url("https://owasp.org/")
#
# print("ls is: ", ls2)
# print("ls TYPE is: ", type(ls2))
