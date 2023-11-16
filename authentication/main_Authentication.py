from encrypt_secret_word import encrypt
import html_content


#opening message:
print("Hello, if you are a website owner and you want us to check for you if there are any security holes on your website,Follow the next steps\n")

# Get URL website:
url =  input("Enter your URL website: ")

# Get secret word:
secret_word = input("Enter your secret word: ")

# Encrypt secret word:
encrypted_word = encrypt(secret_word)
# Print the encryptet word:
print("Encrypted word:", encrypted_word)
print("Put the Encrypted word in noscript tag in your root page(index page)")  
input("Press enter after putting the code on the site")

noscripts = html_content.get_all_noscript(url)

res = html_content.find_encrypted_secret_word(noscripts, encrypted_word)
if res:
    print("Succeeded!")
else:
    print("No Succeeded!")


