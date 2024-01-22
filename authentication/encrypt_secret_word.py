import hashlib


# This function get word from the user, encrypt the word by hash 256, and print the result to user.
def encrypt(secret_word):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # secret word encoded as bytes
    sha256_hash.update(secret_word.encode('utf-8'))
    # Get the word after encryption
    encrypted_word = sha256_hash.hexdigest()
    # Return the encryption word
    return encrypted_word
