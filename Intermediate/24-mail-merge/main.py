
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    guest_list = []
    for name in names:
        guest_list.append(name.strip('\n'))

with open("./Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    for guest in guest_list:
        with open(f"./Output/ReadyToSend/letter_to_{guest}.txt", mode="w") as send_letter:
            send_letter.write(contents.replace("[name]", guest))
