from os import system
import random


play_new_game = True


def sum_of_cards(cards):
    return sum(cards)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def check_for_winner():
    print(f"\nYour final hand: {user_cards}, total score: {user_total}")
    print(f"Computer's cards: {computer_cards}, total score: {comp_total}")

    if user_total > 21:
        print("You went over, comp wins")
    elif user_total == 21:
        print("You blackjack, you wins")
    elif user_total == comp_total:
        print("It is a tie")
    elif comp_total == 21:
        print("Computer hits blackjack YOU LOSE !!")
    elif comp_total > 21:
        print("Computer went over, YOU WIN !!")
    elif user_total > comp_total:
        print("YOU WIN !!")
    else:
        print("YOU LOSE !!")


def print_decks():
    print(f"\nYour cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first hand card: {computer_cards[0]}")


while play_new_game:
    user_cards = []
    computer_cards = []
    user_total = 0
    comp_total = 0
    hold = True
    play = input("Do you want to play a game of black jack? Y or N: ").lower()

    if play == "y":
        system("clear")

        for _ in range(2):
            card = deal_card()
            user_cards.append(card)

        computer_cards.append(deal_card())

        user_total = sum_of_cards(user_cards)

        print_decks()

        while hold:
            take_another_card = input(
                "\nDo you want to get another card ? type y or n: "
            ).lower()

            if take_another_card == "y":
                card = deal_card()
                if (user_total + card) > 21 and card == 11:
                    card = 1
                user_cards.append(card)
                user_total = sum_of_cards(user_cards)

                print_decks()

                if user_total >= 21:
                    hold = False
            else:
                computer_cards.append(deal_card())
                comp_total = sum_of_cards(computer_cards)
                print_decks()
                hold = False

        check_for_winner()
    else:
        play_new_game = False
