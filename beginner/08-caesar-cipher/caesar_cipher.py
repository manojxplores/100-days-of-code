alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(text, shift, direction):
    if direction == "decode":
        shift *= - 1

    cipher_text = ""
    for char in text:
        if char not in alphabet:
            cipher_text += char
        else:
            char_index = alphabet.index(char)
            new_index = char_index + shift
            new_index %= 26
            cipher_text += alphabet[new_index]

    print(f"Here's the {direction}d result: {cipher_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    if input("Type 'yes' if you want to go again. Otherwise type 'no'") == "no":
        print("Goodbye!")
        should_continue = False

