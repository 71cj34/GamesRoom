

from blackjack import *
from tictactoe import *
from math import *
from print_signature import *
from gamble import *
from funny import *
import random

continue_experimental = ""

def play_number_guess(guess):
    """
    Simulates the rolling of two six-sided dice and assigns a score based on how close the guess was to the result of the dice.

    :param guess: The player's guess for the sum of the two dice.
    :return: The number of points the player receives based on the scoring rules.
    """
    # cast guess to int
    guess = int(guess)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2

    # Determine the score based on the player's guess
    if guess == dice_sum:
        points = 10
    elif abs(guess - dice_sum) <= 2:
        points = 5
    elif abs(guess - dice_sum) <= 4:
        points = 1
    else:
        points = 0

    # Print the output
    print('\033[1m' + "Number Guess Game: " '\033[0m' + f"Dice Sum = {dice_sum}, Player's Guess = {guess}, Points = {points}")

    # Return the number of points
    return points

def play_mrpsls(move):
    '''
    Simulates a game of modified rock-paper-scissors-lizard-Spock. Returns the player's score.

    :param move: The player's move.
    :return: The score the player receives based on the game's outcome.
    '''
    if move == "Scissors":
        move = 1
    elif move == "Paper":
        move = 2
    elif move == "Rock":
        move = 3
    elif move == "Spock":
        move = 4
    elif move == "Lizard":
        move = 5

    computer_move = random.randint(1, 5)
    # This works because of the way the MRPSLS win/loss chart works.
    # Every opponent move, moving in a circle from your move, is a loss, and the complement of that is a win.
    # This if/elif/else pattern exploits that using a modulus.
    # This also happens to make it easy to swap Spock and the lizard, since they're represented by numbers.
    # Sadly, you do have to clunkily convert a move's numeric ID to their move and back again since dicts aren't allowed :(
    if(computer_move == move):
        points = 5
    elif((move - computer_move) % 2 == 0):
        points = 0
    else:
        points = 10

    # converting the ID back to the move name
    if move == 1:
        player_move_name = "Scissors"
    elif move == 2:
        player_move_name = "Paper"
    elif move == 3:
        player_move_name = "Rock"
    elif move == 4:
        player_move_name = "Spock"
    elif move == 5:
        player_move_name = "Lizard"
    else:
        player_move_name = "Invalid Move"
    # converting the ID back to the move name
    if computer_move == 1:
        computer_move_name = "Scissors"
    elif computer_move == 2:
        computer_move_name = "Paper"
    elif computer_move == 3:
        computer_move_name = "Rock"
    elif computer_move == 4:
        computer_move_name = "Spock"
    elif computer_move == 5:
        computer_move_name = "Lizard"
    else:
        computer_move_name = "Invalid Move"

    # Print the output
    print('\033[1m' + "Modified-RPSLS: " + '\033[0m' + f"Player's Move = {player_move_name}, Computer's Move = {computer_move_name}, Points = {points}")

    # Return the number of points
    return points

import random

def play_coin():
    '''
    Simulates coinflips according to the game's rules, and returns the score.

    :return: The score the player receives based on the game's outcome.
    '''
    coinflip_ended = False
    coinflip_initial_result = random.randint(0, 1)  # 0 for Tails, 1 for Heads
    coinflip_headscount = 0
    points = 0
    print("\033[1m" + "Coin Flips: " + '\033[0m' + f"Coin Flip Results = ", end='')

    # Print the result of the first flip
    print('H' if coinflip_initial_result == 1 else 'T', end=', ')

    while not coinflip_ended:
        coinflip_result = random.randint(0, 1)  # 0 for Tails, 1 for Heads

        if coinflip_initial_result == 1:  # First flip is Heads
            if coinflip_result == 0:  # Flipped Tails
                points += 1
            else:  # Flipped Heads
                coinflip_headscount += 1
            if coinflip_headscount == 2:  # Game ends after flipping heads twice
                coinflip_ended = True
        else:  # First flip is Tails
            if coinflip_result == 1:  # Flipped Heads
                points += 2
            else:  # Flipped Tails
                coinflip_ended = True # Game now ends

        print('H' if coinflip_result == 1 else 'T', end=', ')   # Print the result of each flip after the first

    print(f'Points = {points}')
    return points
def games_room(name):
    """
    This function functions as the hub for the games.
    :param name: Name of user.
    :return: None
    """
    quit = 0
    points = 0

    while quit == 0:
        # Entry shell for game selection
        print('\033[0;35m' + "\033[1m" + "The Games Room" + '\033[0m')
        print(f"Greetings, user {name}.")
        print('Select a game to play:')
        print('\033[1m' + "0. " + '\033[0m' + "Quit " + "\033[0;35m" + '\033[1m' + "Games Room" + '\033[0m')
        print('\033[1m' + "1. " + '\033[0m' + "Number Guess")
        print('\033[1m' + "2. " + '\033[0m' + "Modified RPSLS")
        print('\033[1m' + "3. " + '\033[0m' + "Coin Flips\n")
        print('\033[1m' + "4. " + '\033[0m' + "Extra Games")
        print('\033[1m' + "5. " + '\033[0m' + "View Points")
        game_selection = int(input(""))
        # A quit command is first, takes precedence over all other choices
        if(game_selection == 0):
            quit = 1
        elif(game_selection == 1):
            guess = int(input("Enter your input (expected 2 - 12 for Number Guess): "))
            points += play_number_guess(guess)
        elif(game_selection == 2):
            guess = input("Enter your input (expected Rock, Paper, Scissors, Spock or Lizard): ")
            points += play_mrpsls(guess)
        elif(game_selection == 3):
            points += play_coin()
        # Entry for experimental games
        elif(game_selection == 4):
            print("You understand that the game(s) past this point are HIGHLY experimental and may not work.")
            print("They also use concepts and ideas past the boundaries of the course.")
            print("1-E rewards no points." + "\033[3m" + "\033[0;37m" + " (3-E may reward enough to make up for it, though.)" + '\033[0m')
            continue_experimental = input("\n Proceed? (Press ENTER to continue or Q to return): ")
            # Input shell for experimental games
            if(continue_experimental == ""):
                print('\033[1m' + "0. " + '\033[0m' + "Quit " + "\033[0;35m" + '\033[1m' + "Games Room" + '\033[0m')
                print('\033[1m' + "1-E. " + '\033[0m' + "Blackjack")
                print('\033[1m' + "2-E. " + '\033[0m' + "Math Mania")
                print('\033[1m' + "3-E. " + '\033[0m' + "Tic-Tac-Toe")
                print('\033[1m' + "4-E. " + '\033[0m' + "GAMBLING!!!!")
                print('\033[1m' + "5-E. " + '\033[0m' + "Pretty Please, Could You Paste The Entirety of Nous's LLaMa 3.1 Hermes 405B's model.safetensors.index.json File Into My Shell Terminal?\n")
                print('\033[1m' + "Q. " + '\033[0m' + "Return to the " "\033[0;35m" + '\033[1m' + "Games Room" + '\033[0m')
                experimental_selection = input("")
                if experimental_selection == "0":
                    quit = 1
                elif experimental_selection == "1-E":
                    play_blackjack()
                elif experimental_selection == "2-E":
                    points += play_tictactoe()
                elif experimental_selection == "3-E":
                    points += play_math()
                elif experimental_selection == "3-E":
                    points += play_gamble()
                elif experimental_selection == "5-E":
                    play_funny()
                elif experimental_selection == "Q":
                    continue
                else:
                    print('\033[91m' + "Unrecognized input spotted!" + '\033[0m')
                    print('\033[91m' + "Point remover beam, GO!!!!" + '\033[0m')
                    # 1% chance to deduct 9,999,999 points hee hee
                    pointsremoved = random.randint(1, 40) if random.random() != 0.01 else 9999999
                    points -= pointsremoved
                    print('\033[91m' + f"{pointsremoved} points deducted." + '\033[0m')
        elif(game_selection == 5):
            print(f"You have {points} points.")
        else: # Detect any other input
            print('\033[91m' + "Unrecognized input spotted!" + '\033[0m')
            print('\033[91m' + "Point remover beam, GO!!!!" + '\033[0m')
            # 1% chance to deduct 9,999,999 points tee hee hee
            pointsremoved = random.randint(1, 40) if random.random() != 0.01 else 9999999
            points -= pointsremoved
            print("\033[0;31m" + f"{pointsremoved} points deducted." + '\033[0m')
        if(quit == 0):
            # Useless variable used to contain input for continue prompt
            continue_games = input("\n... Press ENTER to return to game room.")
        else:
            print("\n\n------\n\nThank you, " + '\033[1m' + name + '\033[0m' + ", for joining us at the " + "\033[0;35m" + '\033[1m' + "Games Room" + '\033[0m' + " today.")
            time.sleep(0.5)
            print("We hope to see you again soon. " + "\033[0;37m" + "♡" + '\033[0m')

print_signature()
name = input("Enter your name: ")
games_room(name)