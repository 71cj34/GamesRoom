import random
import time

class cl:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"

    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def play_gambling():
    points = 0
    print("GAMBLING IS AWESOME!!")
    print("(prepare your wallet!!)\n")
    print("Get ready...")
    time.sleep(1.5)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(2)
    print("0 and a half......\n")
    time.sleep(2.5)
    ROLL = 10000*(random.random())
    print("You rolled a " + cl.UNDERLINE + str(int(round(ROLL, 0))) + "/10000" + cl.END)
    if (ROLL <= 10):
        print(cl.RED + "Ouch. Just ouch." + cl.END)
        print("You lose " + cl.BOLD + "999,999,999" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "0.1% chance!" + cl.END)
        points -= 999999999
    elif (ROLL <= 100):
        print(cl.RED + "That's gotta hurt." + cl.END)
        print("You lose " + cl.BOLD + "50,000,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "0.9% chance!" + cl.END)
        points -= 50000000
    elif (ROLL <= 400):
        print(cl.RED + "Really not a good day for you." + cl.END)
        print("You lose " + cl.BOLD + "5,000,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "3% chance!" + cl.END)
        points -= 10000000
    elif (ROLL <= 1000):
        print(cl.LIGHT_RED + "Not a good day for you, huh?" + cl.END)
        print("You lose " + cl.BOLD + "300,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "6% chance!" + cl.END)
        points -= 300000
    elif (ROLL <= 2000):
        print(cl.LIGHT_RED + "That's not good." + cl.END)
        print("You lose " + cl.BOLD + "90,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "10% chance!" + cl.END)
        points -= 90000
    elif (ROLL <= 3500):
        print(cl.YELLOW + "It could be worse. (It could also be a lot better.)" + cl.END)
        print("You lose " + cl.BOLD + "50,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "15% chance!" + cl.END)
        points -= 50000
    elif (ROLL <= 5500):
        print(cl.DARK_GRAY + "Hey, that's not (technically) that bad! Roll it again, go on!" + cl.END)
        print("You lose " + cl.BOLD + "100" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "20% chance!" + cl.END)
        points -= 100
    elif (ROLL <= 7500):
        print(cl.DARK_GRAY + "See, you won something! Keep gambling. Never give up. Keep gambling." + cl.END)
        print("You win " + cl.BOLD + "30,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "20% chance!" + cl.END)
        points += 30000
    elif (ROLL <= 8500):
        print(cl.LIGHT_GREEN + "This roll is far better than average! Relish in it! Bathe in it! Gamble again!" + cl.END)
        print("You win " + cl.BOLD + "500,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "10% chance!" + cl.END)
        points += 500000
    elif (ROLL <= 9250):
        print(cl.GREEN + "Whoo boy! You're a millionaire now! Go on, double or nothing. Do it." + cl.END)
        print("You win " + cl.BOLD + "1,250,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "7.5% chance!" + cl.END)
        points += 1250000
    elif (ROLL <= 9750):
        print(cl.LIGHT_BLUE + "You're so lucky! So, so lucky. You can win again. Just one more." + cl.END)
        print("You win " + cl.BOLD + "2,000,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "5% chance!" + cl.END)
        points += 2000000
    elif (ROLL <= 9990):
        print(cl.BLUE + "4,000,000 is so much! So, so much, but... it could be more. Throw it on black this time. You can win even more." + cl.END)
        print("You win " + cl.BOLD + "6,000,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "2.4% chance!" + cl.END)
        points += 6000000
    else:
        print(cl.PURPLE + "100 MILLION POINT JACKPOT!" + cl.END)
        print("You gain " + cl.BOLD + "100,000,000" + cl.END + " points.")
        print(cl.ITALIC + cl.LIGHT_GRAY + "0.1% chance!" + cl.END)
        points += 10000000
    time.sleep(5)
    print("\n\n")
    print("Fun fact, the E(x) of this casino is -1,140,769.999.")
    print("This means playing x times, you are expected to lose an average of -1,140,770 points.\n")
    time.sleep(1.5)
    print(cl.ITALIC + cl.LIGHT_RED + "♤ The house always wins." + cl.END)
    return points

if __name__ == "__main__":
    play_gambling()