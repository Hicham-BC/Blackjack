from random import choice
import os

def blackjack(player_hand, player_score, dealer_hand, dealer_score):
    """
    Check if there is a Blackjack winner.

    Returns:
    - True if the dealer or the player has a Blackjack (a hand value of 21),
      and displays the final hands along with the winner.
    - False if there is no Blackjack winner.
    """
    if dealer_score == 21:
        final_hand(player_hand, player_score, dealer_hand, dealer_score)
        print("Blackjack, Dealer Wins")
        return True
    elif player_score == 21:
        final_hand(player_hand, player_score, dealer_hand, dealer_score)
        print("Blackjack, You Win")
        return True
    return False

def compare_score(player_hand, player_score, dealer_hand, dealer_score):
    """
    Compare the final scores of the dealer and the player and determine the winner.

    Returns:
    - True to indicate the end of the game.
    """
    if not blackjack(player_hand, player_score, dealer_hand, dealer_score):
        final_hand(player_hand, player_score, dealer_hand, dealer_score)
        if dealer_score > 21:
            print("Dealer went over 21, You win")
        elif player_score > dealer_score:
            print("You Win")
        elif dealer_score == player_score:
            print("Draw")
        else:
            print("Dealer Wins")
    
    return True

def ace(cards, score):
    """
    Simulate drawing a card, considering the possibility of an Ace.

    Args:
    - cards (list): The available cards to draw from.
    - score (int): The current score of the hand.

    Returns:
    - The value of the drawn card, taking into account the possibility of an Ace
      being worth 1 or 11 based on the current hand score.
    """
    card = choice(cards)
    if card == 11 and (score + card) > 21:
        return 1
    return card

def remove_cards(cards, hand):
    """
    Remove a list of cards from the available cards.

    Args:
    - cards (list): The available cards to draw from.
    - hand (list): The list of cards to be removed from the available cards.
    """
    for card in hand:
        cards.remove(card)

def final_hand(player_hand, player_score, dealer_hand, dealer_score):
    """
    Display the final hands and scores of the player and the dealer.
    """
    print(f"\tYour final cards: {player_hand} >> Your final score: {player_score}")
    print(f"\tDealer's final cards: {dealer_hand} >> His final score: {dealer_score}")

def clear_screen():
    """
    Clears the terminal screen.

    Uses the appropriate command based on the operating system to clear the screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')