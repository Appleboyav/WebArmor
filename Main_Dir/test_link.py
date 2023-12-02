import helper_links as hl

ls = hl.GetLink.get_internal_links()

print("ls is: ",ls)
print("ls TYPE is: ",type(ls))

# ls2 = hl.GetLink.__validate_url("https://owasp.org/")

# print("ls is: ",ls2)
# print("ls TYPE is: ",type(ls2))
