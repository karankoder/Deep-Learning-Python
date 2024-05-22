import random
import string

def generate_random_password(length):
    """Generate a random password string with the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
password_length = 10

random_password = generate_random_password(password_length)

print("Random Password:", random_password)
