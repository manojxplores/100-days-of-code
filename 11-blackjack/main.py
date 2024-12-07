import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def compare_scores(user_score, comp_score):
    if user_score > 21:
        print("You went over 21. You lose!")
    elif comp_score > 21:
        print("Dealer went over 21. You Win!")
    elif user_score > comp_score:
        print("You win!")
    elif user_score < comp_score:
        print("You lose!")
    else:
        print("Its' a draw!")

def blackjack():
    user_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards)]
    game_over = False

    if calculate_score(user_cards) == 21:
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print("Blackjack! You win!")
        return
    elif calculate_score(dealer_cards) == 21:
        print(f"Dealer's hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
        print("Dealer has Blackjack! You lose!")
        return

    while not game_over:
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if draw_card == "y":
            user_cards.append(random.choice(cards))
            user_score = calculate_score(user_cards)
            if user_score > 21:
                compare_scores(calculate_score(user_cards), calculate_score(dealer_cards))
                return
        else:
            game_over = True

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))

    dealer_score = calculate_score(dealer_cards)
    user_score = calculate_score(user_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    compare_scores(user_score, dealer_score)

blackjack()