import pyfiglet
import random
import os

def game():
    os.system("clear")

    

    print("="*80)

    print(pyfiglet.figlet_format("GUESS THE NUMBER GAME"))

    print("="*80)



    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
     
    
    
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





if __name__ == "__main__":
    game()

