# importing all the required libraries

import pyfiglet
import random
import os
import time
from colorama import Fore, Back, Style, init

# initilising the colorama

init()

# defining the game function

def game():

    text = "GUESS THE NUMBER"

    terminal_width = os.get_terminal_size().columns

    ascii_art = pyfiglet.figlet_format(text)

    lines = ascii_art.splitlines()

    os.system("clear")

    for line in lines:
        centered_line = line.center(terminal_width)
        print(centered_line)

    print("\n\n\n\n\n")
    input(Fore.YELLOW + "Press <ENTER> to continue".center(terminal_width) + Style.RESET_ALL)

    os.system("clear")

    # game logic starts here

    start = int(input("Enter the first number of the guessing range: "))
    end = int(input("Enter the last number of the guessing range: "))
      
    count = 0

    guess = random.randint(start, end)

    answer = None

    while answer != guess: 
        answer = int(input("Enter your guess: "))

        if answer > guess:
            print("your guess is high")

        elif answer < guess:
            print("your guess is low")

        count = count + 1
    
    os.system("clear")

    print("Your guess is correct: ",answer)

    print(f"No. of attempts: {count}")

    if count == 1:
        print ("Congratulations your score: 10/10!")
    elif count == 2:
        print ("Your score: 9/10")
    elif count == 3:
        print ("Your score: 8/10")    
    elif count == 4:
        print ("Your score: 7/10")    
    elif count == 5:
        print ("Your score: 6/10")
    elif count == 6:
        print ("Your score: 5/10")
    elif count == 7:
        print ("Your score: 4/10")
    elif count == 8:
        print ("Your score: 3/10")
    elif count == 9:
        print ("Your score: 2/10")
    elif count > 9:
        print("Your score: 1/10")



# this is the execution of the main program

if __name__ == "__main__":
    game()

