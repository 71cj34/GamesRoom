""" 
ENG 1P13. Computing 3 Lab, Pre-Lab Debrief Exercise 1.

Write a print_signature function that returns nothing but outputs the 
following to the shell, nicely formatted: 
    
    your name,  
    your student number and program,  
    COMPSCI 1MD3: Introduction to Programming, 
    Your professor’s name, and  
    the current term (e.g. Spring 2024) 
    
Save this function somewhere. You’ll be using it in your assignments 
from now on. 

McMaster, 2024"""

####    YOUR CODE HERE    ####
import time
import random

def print_signature():
    print("\033[38;5;246m\033[3m400565775\033[0m ")
    print("\033[38;5;246m\033[3mENGINEER 1P13: ENG 1\033[0m")
    print("\033[38;5;246m\033[3mFall-Winter 2024\033[0m \n")
    print("\033[1mJason Cheng\033[0m\n\n-------\n\n")
    time.sleep(1)
    print("Now loading...")

    def progress_bar(duration):
        """

        :param duration: How long the progress bar should last.
        :return: None
        """
        total_steps = 20
        step_time = duration / total_steps

        for i in range(total_steps + 1):
            # This basically makes it so the variance is more often shorter than longer
            time.sleep(random.random() ** 8)
            filled = '█' * i
            empty = '░' * (total_steps - i)
            # cool ahh fstring
            print(f'\r|{filled}{empty}| {i / total_steps * 100:.0f}.{0 if random.random() < 0.2 or i == total_steps else random.randint(0, 9)}%', end='')
            time.sleep(step_time)

    progress_bar(random.uniform(0.25, 0.6))

    print("\n\nLoading complete. Thank you for your patience.")
    print("Starting program...\n\n-------\n\n")
    time.sleep(0.5)