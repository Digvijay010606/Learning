import random
import os


def guess_the_number():
    # generate a random number between 1 and 100

    number_to_guess = random.randint(1,100)
    attempts = 0
    max_attempts = 10
    score = 100 # starting score

    os.system("clear")

    print("Welcome to the Guess the Number Game!\n")
    print("-"*40)
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.\n")
    print("-"*40)


    while attempts < max_attempts:
        try:
            # take input from the user
            guess = int(input("Enter your guess: "))

            attempts += 1


            # provide feedback
            if guess < number_to_guess:
                print("Too low!, Try again.")
                score -= 10 # decrease score for each incorrect guess
            elif guess > number_to_guess:
                print("Too high! Try again.")
                score -= 10 # decrease score for each incorrect guess
            else:
                print("-"*40)
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                print(f"Your score is: {score}")
                print("-"*40)
                break
        except ValueError:
            print("Please enter a valid integer.")
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was: {number_to_guess}")
        print(f"Your score is: {score}")


if __name__ == "__main__":
    guess_the_number()
