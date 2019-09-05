import string
import random

def func(words):
    upper_case = [random.choice(string.ascii_uppercase) for upper in range(words)]
    lower_case = [random.choice(string.ascii_lowercase) for lower in range(words)]
    digits = [random.choice(string.digits) for dig in range(words)]
    special_characters = [random.choice(string.punctuation) for spl in range(words)]
    pwd = "".join(upper_case + lower_case + digits + special_characters)
    print("Merged string: ",pwd)
    print("Length of merged string: ",len(pwd))
    generator = ''.join(random.choice(pwd) for i in range(words))
    return generator
    
words = int(input("Enter the length of the password to generate: "))
password = func(words)
print("Password:",password)
