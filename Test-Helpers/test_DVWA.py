from Helpers import helper_dvwa


# print(get_login_cookies("http://localhost/DVWA/login.php"))
# print(get_login_cookies("http://localhost/DVWA/login.php", 1))

my_dict1 = helper_dvwa.get_login_cookies("http://localhost/DVWA/login.php")
my_dict2 = helper_dvwa.get_login_cookies("http://localhost/DVWA/login.php", 1)
dup_my_dict1 = my_dict1

# print(type(my_dict1))
# print(type(my_dict2))

print("my_dict1: ", id(my_dict1))
print("dup_my_dict1: ", id(dup_my_dict1))
print("my_dict2: ", id(my_dict2))
