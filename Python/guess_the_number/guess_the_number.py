import random
import os

def game():
    os.system("clear")

    print("-----------------------------------------------------")

    print("Welcome to GUESS THE NUMBER game")

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
     
    
    
    count = 0
    

    guess = random.randint(start, end)

    answer = None

    while answer != guess: 
        answer = int(input("Enter your guess: "))

        if answer > guess:
            print("you guess high")

        elif answer < guess:
            print("you guess low")

        else:
            print("correct")

        count = count + 1
    
    os.system("clear")

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





game()

