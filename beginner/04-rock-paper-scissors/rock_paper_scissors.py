import random

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors"))
comp_choice = random.randint(0, 2)
choice_list = [rock, paper, scissors]

print("You chose:")
print(choice_list[user_choice])
print(f"Computer chose:")
print(choice_list[comp_choice])

if user_choice == comp_choice:
    print("That's a draw!")
elif (
        (user_choice == 0 and comp_choice == 2) or
        (user_choice == 1 and comp_choice == 0) or
        (user_choice == 2 and comp_choice == 1)
):
    print("You win!")
else:
    print("You lose!")
