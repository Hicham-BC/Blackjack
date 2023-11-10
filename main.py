from random import sample
from functions import *
from art import logo


while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    clear_screen()

    user_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(logo)
    # dealing the user and the computer 2 cards each.
    user_hand = sample(user_cards, k=2)
    computer_hand = sample(computer_cards, k=2)
    remove_cards(user_cards, user_hand)
    remove_cards(computer_cards, computer_hand)

    # Calculate the total score for the player and the computer based on their current hands.
    user_score = sum(user_hand)
    computer_score = sum(computer_hand)

    # Check if the game is over by determining if there's a Blackjack winner
    game_over = blackjack(user_hand, user_score, computer_hand, computer_score)

    while not game_over:
        print(f"\tYour cards: {user_hand} >> Current score:{sum(user_hand)}")
        print(f"\tDealer's first card is: {computer_hand[0]}")

        # Prompt the player to decide whether to draw another card
        if input("Type 'yes' to get another card, type 'no' to pass: ") == "yes":
            # Draw a card for the player, considering the possibility of an Ace
            user_card = ace(user_cards, user_score)
            # Add the drawn card to the player's hand
            user_hand.append(user_card)
            # remove the value of Ace in the user's cards
            user_cards.remove(user_hand[-1]) if (user_card != 1) else user_cards.remove(11)
            # Recalculate the total score for the player's hand
            user_score = sum(user_hand)

            game_over = blackjack(user_hand, user_score, computer_hand, computer_score)
            # Check if the player's total score exceeds 21, resulting in a bust
            if user_score > 21:
                final_hand(user_hand, user_score, computer_hand, computer_score)
                print("You went over 21, Dealer Wins")
                # Set the game_over flag to True, indicating the end of the round
                game_over = True
        
        # Computer's turn: Draw cards if necessary.
        else:
            # Continue drawing cards for the computer while its total score is below 17.
            while computer_score < 17:
                # Draw a card for the computer, considering the possibility of an Ace
                computer_card = ace(computer_cards, computer_score)
                # Add the drawn card to the computer's hand
                computer_hand.append(computer_card)
                # remove the value of Ace in the computer's cards
                computer_cards.remove(computer_hand[-1]) if (computer_card != 1) else computer_cards.remove(11)
                # Recalculate the total score for the computer's hand
                computer_score = sum(computer_hand)
            
            # Determine the winner.
            game_over = compare_score(user_hand, user_score, computer_hand, computer_score)