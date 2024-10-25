# import os
# import time
# import random
#
# def cprint(message, *args):
#     prefix = "--> "
#     print(prefix + message, *args)
#
# def cinput(message):
#     prefix = "--> "
#     out = input(prefix + message)
#     return out
#
# def cls():
#     os.system('cls')
#
# def calculate_hand_value(hand):
#     value = 0
#     aces = 0
#     for card in hand:
#         if card == 11:
#             aces += 1
#         value += card
#     while value > 21 and aces:
#         value -= 10
#         aces -= 1
#     return value
#
# def play_blackjack():
#     cprint("BLACKJACK\n\n")
#     bg = cinput("Press Enter to begin...")
#     cls()
#
#     end = 0
#     turn = 1
#     cards = [2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
#     dcards = []
#     pcards = []
#
#     def givecards():
#         a = random.choice(cards)
#         while True:
#             try:
#                 cards.index(a)
#             except:
#                 a = random.choice(cards)
#             else:
#                 del cards[cards.index(a)]
#                 break
#         pcards.append(a)
#         cprint(f"You have drawn a card of value {a}. Your total is now {calculate_hand_value(pcards)}.")
#
#     def givedcards():
#         a = random.choice(cards)
#         while True:
#             try:
#                 cards.index(a)
#             except:
#                 a = random.choice(cards)
#             else:
#                 del cards[cards.index(a)]
#                 break
#         dcards.append(a)
#
#     turn = 1
#     stand = 0
#
#     while end == 0:
#         cls()
#         cprint("BEGIN TURN ", turn)
#         if(turn == 1):
#             cprint("Draw 1 starts now.")
#             dcards.append("?")
#             hiddencard = random.choice(cards)
#             del cards[cards.index(hiddencard)]
#
#             a = random.choice(cards)
#             dcards.append(a)
#             del cards[cards.index(a)]
#
#             a = random.choice(cards)
#             if(a == 11):
#                 b = 1
#                 pcards.append(b)
#                 del cards[cards.index(b)]
#             else:
#                 pcards.append(a)
#                 del cards[cards.index(a)]
#
#             a = random.choice(cards)
#             if(a == 11):
#                 b = 1
#                 pcards.append(b)
#                 del cards[cards.index(b)]
#             else:
#                 pcards.append(a)
#                 del cards[cards.index(a)]
#
#             if (calculate_hand_value(pcards) > 21):
#                 cls()
#                 cprint(f"You have busted.")
#                 cprint(f"Your total was {calculate_hand_value(pcards)}, {calculate_hand_value(pcards) - 21} past 21.")
#                 del dcards[0]
#                 cprint(f"The dealer's hidden card was {hiddencard}, giving them a total of {hiddencard + calculate_hand_value(dcards)}.")
#                 
#         else:
#             cprint(f"Draw {turn} starts now.")
#         print("DEALER cards: ", *dcards)
#         print("PLAYER cards: ", *pcards)
#         decision = cinput("\n Hit or stand? (Hit/H or Stand/S)\n")
#         if(decision == "Hit" or decision == "H"):
#             givecards()
#         else:
#             cprint("You have chosen to STAND.")
#             stand = 1
#
#         if(calculate_hand_value(pcards) > 21):
#             cls()
#             cprint(f"You have busted.")
#             cprint(f"Your total was {calculate_hand_value(pcards)}, {calculate_hand_value(pcards) - 21} past 21.")
#             del dcards[0]
#             cprint(f"The dealer's hidden card was {hiddencard}, giving them a total of {hiddencard +  calculate_hand_value(dcards)}.")
#             
#         elif(calculate_hand_value(pcards) == 21):
#             for i in range(10):
#                 print("BLACKJACK!")
#             cls()
#             cprint(f"You win with a blackjack!")
#             del dcards[0]
#             cprint(f"The dealer's hidden card was {hiddencard}, giving them a total of {hiddencard +  calculate_hand_value(dcards)}.")
#             
#
#         if(stand == 1):
#             cls()
#             cprint("Revealing dealer's hidden card...")
#             del dcards[0]
#             dcards.insert(0, hiddencard)
#             cprint(f"\n The dealer's hidden card was revealed to be a {hiddencard}!")
#             while(calculate_hand_value(dcards) < 17):
#                 cls()
#                 cprint("SHOWDOWN MODE.")
#                 givedcards()
#                 cprint("Dealer cards: ", *dcards)
#                 time.sleep(2)
#             if(calculate_hand_value(dcards) > 21):
#                 cls()
#                 cprint("You win! (Dealer busted)")
#                 cprint(f"Sum of your cards: {calculate_hand_value(pcards)}")
#                 cprint(f"Sum of dealer cards: {calculate_hand_value(dcards)}")
#             elif(calculate_hand_value(dcards) == 21):
#                 cls()
#                 cprint("Dealer wins with a blackjack!")
#                 cprint(f"Sum of your cards: {calculate_hand_value(pcards)}")
#                 cprint(f"Sum of dealer cards: {calculate_hand_value(dcards)}")
#             else:
#                 cls()
#                 cprint("Counting card values:")
#                 time.sleep(1)
#                 print("Player: ", *pcards)
#                 print("Dealer: ", *dcards)
#                 time.sleep(2)
#                 if(calculate_hand_value(pcards) > calculate_hand_value(dcards)):
#                     cls()
#                     print("You win!")
#                 elif(calculate_hand_value(pcards) == calculate_hand_value(dcards)):
#                     cls()
#                     print("Game tied!")
#                 else:
#                     cls()
#                     print("Dealer wins!")
#                 cprint(f"Sum of your cards: {calculate_hand_value(pcards)}")
#                 cprint(f"Sum of dealer cards: {calculate_hand_value(dcards)}\n\n")
#                 cprint("Thank you for playing with us.")
#
#             
#         turn += 1
#
# play_blackjack()

import os
import time
import random

# blackjack made with nothing but pure semi-panicked procastination over a project more important
# i have no clue how it works. code from a sober me vs a stressed me is code from two completely different beings
# the game might not register the game ended sometimes lmao
# also the thing where aces = 11 unless it would result in the game ending in which case aces = 1 doesn't work very well
# RHARR WHAT THE FUCK IS ABSTRACTION

# TODO: make it not suck

def cprint(message, *args):
    prefix = "--> "
    print(prefix + message, *args)

def cinput(message):
    prefix = "--> "
    return input(prefix + message)

def cls():
    os.system('cls')

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card == 11:
            aces += 1
        value += card
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def play_blackjack():
    cprint("BLACKJACK\n\n")
    cinput("Press Enter to begin...")
    cls()

    game_ended = 0
    cards = [2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    dcards = []
    pcards = []

    def givecards():
        a = random.choice(cards)
        while True:
            try:
                cards.index(a)
            except:
                a = random.choice(cards)
            else:
                del cards[cards.index(a)]
                break
        pcards.append(a)
        cprint(f"You have drawn a card of value {a}. Your total is now {calculate_hand_value(pcards)}.")

    def givedcards():
        a = random.choice(cards)
        while True:
            try:
                cards.index(a)
            except:
                a = random.choice(cards)
            else:
                del cards[cards.index(a)]
                break
        dcards.append(a)

    turn = 1
    stand = 0
    hiddencard = None

    while game_ended == 0:
        cls()
        cprint("BEGIN TURN ", turn)
        if (turn == 1):
            cprint("Draw 1 starts now.")
            dcards.append("?")
            hiddencard = random.choice(cards)
            del cards[cards.index(hiddencard)]

            a = random.choice(cards)
            dcards.append(a)
            del cards[cards.index(a)]

            a = random.choice(cards)
            pcards.append(1 if a == 11 else a)
            del cards[cards.index(1 if a == 11 else a)]

            a = random.choice(cards)
            pcards.append(1 if a == 11 else a)
            del cards[cards.index(1 if a == 11 else a)]

            if (calculate_hand_value(pcards) > 21):
                cls()
                cprint("You have busted.")
                cprint(f"Your total was {calculate_hand_value(pcards)}, {calculate_hand_value(pcards) - 21} past 21.")
                del dcards[0]
                cprint(
                    f"The dealer's hidden card was {hiddencard}, giving them a total of {hiddencard + calculate_hand_value(dcards)}.")
                
        else:
            cprint(f"Draw {turn} starts now.")

        print("DEALER cards: ", *dcards)
        print("PLAYER cards: ", *pcards)
        decision = cinput("\n Hit or stand? (Hit/H or Stand/S)\n")

        if (decision in ["Hit", "H"]):
            givecards()
        else:
            cprint("You have chosen to STAND.")
            stand = 1

        if (calculate_hand_value(pcards) > 21):
            cls()
            cprint("You have busted.")
            cprint(f"Your total was {calculate_hand_value(pcards)}, {calculate_hand_value(pcards) - 21} past 21.")
            del dcards[0]
            cprint(
                f"The dealer's hidden card was {hiddencard}, giving them a total of {hiddencard + calculate_hand_value(dcards)}.")
            
        elif (calculate_hand_value(pcards) == 21):
            cls()
            cprint("BLACKJACK! You win!")
            del dcards[0]
            cprint(
                f"The dealer's hidden card was {hiddencard}, giving them a total of {hiddencard + calculate_hand_value(dcards)}.")
            

        if (stand == 1):
            cls()
            cprint("Revealing dealer's hidden card...")
            del dcards[0]
            dcards.insert(0, hiddencard)
            cprint(f"\n The dealer's hidden card was revealed to be a {hiddencard}!")
            while (calculate_hand_value(dcards) < 17):
                cls()
                cprint("SHOWDOWN MODE.")
                givedcards()
                cprint("Dealer cards: ", *dcards)
                time.sleep(2)

            if (calculate_hand_value(dcards) > 21):
                cls()
                cprint("You win! (Dealer busted)")
            elif (calculate_hand_value(dcards) == 21):
                cls()
                cprint("Dealer wins with a blackjack!")
            else:
                cls()
                cprint("Counting card values:")
                time.sleep(1)
                print("Player: ", *pcards)
                print("Dealer: ", *dcards)
                time.sleep(2)
                if (calculate_hand_value(pcards) > calculate_hand_value(dcards)):
                    cls()
                    cprint("You win!")
                elif (calculate_hand_value(pcards) == calculate_hand_value(dcards)):
                    cls()
                    cprint("Game tied!")
                else:
                    cls()
                    cprint("Dealer wins!")
                cprint(f"Sum of your cards: {calculate_hand_value(pcards)}")
                cprint(f"Sum of dealer cards: {calculate_hand_value(dcards)}")

            cprint("Thank you for playing with us.")
            break
        turn += 1

if __name__ == "__main__":
    play_blackjack()
