import string
import random

def func(len):
    upper = [random.choice(string.ascii_uppercase) for upper in range(len)]
    lower = [random.choice(string.ascii_lowercase) for lower in range(len)]
    digits = [random.choice(string.digits) for dig in range(len)]
    special = [random.choice(string.punctuation) for spl in range(len)]
    merge = "".join(upper + lower + digits + special)
    generator = "".join(random.choice(merge) for i in range(len))
    return generator
    
len = int(input("Enter the length of the password to generate: "))
password = func(len)
print("Password:",password)
