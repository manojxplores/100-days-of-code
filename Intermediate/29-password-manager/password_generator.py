import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

NR_LETTERS = 4
NR_SYMBOLS = 4
NR_NUMBERS = 4


def create_password():
    password_list = []
    for i in range(NR_LETTERS):
        password_list.append(random.choice(letters))
    for j in range(NR_SYMBOLS):
        password_list.append(random.choice(symbols))
    for k in range(NR_NUMBERS):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = "".join(password_list)
    return password


