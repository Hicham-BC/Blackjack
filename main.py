from random import sample,choice

def blackjack():
    if computer_score == 21:
        final_hand()
        print("Blackjack, Computer Wins")
        return False
    elif user_score == 21:
        final_hand()
        print("Blackjack, You Win")
        return False
    return True

def compare_score():
    if blackjack():
        final_hand()
        if computer_score > 21:
            print("Computer went over 21, You win")
        elif user_score > computer_score:
            print("You Win")
        elif user_score == computer_score:
            print("Draw")
        else:
            print("Computer wins")
    
    return False

def ace(cards, score):
    card = choice(cards)
    if card == 11 and (score + card) > 21:
        return 1
    return card


def remove_cards(cards, hand):
    for card in hand:
        cards.remove(card)


def final_hand():
    print(f"\tyour final cards: {user_hand} >> your final score: {user_score}")
    print(f"\tcomputer's final cards: {computer_hand} >> its final score: {computer_score}")   


user_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = sample(user_cards, k=2)
computer_hand = sample(computer_cards, k=2)
remove_cards(user_cards, user_hand)
remove_cards(computer_cards, computer_hand)

user_score = sum(user_hand)
computer_score = sum(computer_hand)

should_continue = blackjack()

while should_continue:
    print(f"\tyour cards: {user_hand} >> current score:{sum(user_hand)}")
    print(f"\tcomputer's first card is: {computer_hand[0]}")
    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        user_card = ace(user_cards, user_score)
        user_hand.append(user_card)
        user_cards.remove(user_hand[-1])
        user_score = sum(user_hand)

        should_continue = blackjack()
        if user_score > 21:
            final_hand()
            print("You went over 21, Computer Wins")
            should_continue = False
    else:
        while computer_score < 17:
            computer_card = ace(computer_cards, computer_score)
            computer_hand.append(computer_card)
            computer_cards.remove(computer_hand[-1])
            computer_score = sum(computer_hand)
        
        should_continue = compare_score()

        