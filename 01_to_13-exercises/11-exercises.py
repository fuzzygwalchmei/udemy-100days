#! /bin/python3

# Blackjack Capstone project

from random import randint, choice

card_values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def score_hand(hand):
    aces = hand.count('A')
    score = sum([card_values.get(x) for x in hand])
    if aces>0 and score<11:
        score+=10
    return score

def create_deck():
    deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    return deck

def deal_card(deck):
    card = choice(deck)
    deck.remove(card)
    return card

def dealer_choice(computer_cards):
    return True if score_hand(computer_cards) < 17 else False

def print_all(player, computer):
        print("")
        print(f"Your Cards: \t{[card for card in player]}")
        print(f"Computers Cards:\t{[card for card in computer]}")
        print(f"Your current score is: {score_hand(player)}")
        print(f"Computers score is: {score_hand(computer)}")

def setup_game(deck):
        player_cards = []
        computer_cards = []
        player_cards.append(deal_card(deck))
        computer_cards.append(deal_card(deck))
        player_cards.append(deal_card(deck))
        return player_cards, computer_cards

def debug_print(player, computer, deck):
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    print(f"Deck: {deck}")



def main():
    game_deck = create_deck()
    play_choice = input("Do you want to Blackjack? (y/n): ").lower()
    player, computer = setup_game(game_deck)
    while play_choice =="y":
        print_all(player, computer)
        add_card = input("Do you want another card?").lower()
        while add_card == "y":
            player.append(deal_card(game_deck))
            print_all(player, computer)
            if score_hand(player)>21:
                break
            add_card = input("Do you want another card?").lower()
            clear()

        while dealer_choice(computer):
            computer.append(deal_card(game_deck))
        clear()
        if score_hand(player)>21:
            print("Sorry, you busted!")
        elif score_hand(computer)>21:
            print("The computer busted!, You Win!")
        elif score_hand(player) > score_hand(computer):
            print("You won!")
        elif score_hand(player) == score_hand(computer):
            print("You pushed, there is no winner today")
        else:
            print("Sorry, you lost")
        print_all(player, computer)
        play_choice = input("Would you like to play again? (y/n): ").lower()
    
    


if __name__ == "__main__":
    main()
