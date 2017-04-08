import random
import string


def make_email():

    providers = ["@gmail.com", "@yahoo.com", "@aol.com", "@hotmail.com", "@live.com"]
    characters = list(string.ascii_lowercase)
    characters += string.digits
    #characters.append("_")
    email = []

    for i in range(0, 25):
        email.append(random.choice(characters))

    email.append(random.choice(providers))

    return email


def make_password():
    characters = list(string.ascii_lowercase)
    characters.append(string.digits)
    characters.append("_")
    pass_word = []

    for i in range(0, 6):
        pass_word.append(random.choice(characters))

    return pass_word

print("".join(make_email()))
print("".join(make_password()))
