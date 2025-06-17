import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\n")
num=random.randint(1,100)


game_over=False
print("I'm thinking of a number between 1 to 100\n")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="hard":
    attempts=5
else:
    attempts=10

    def guess_the_num():

        global game_over
        global attempts

        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        guess = int(input("Make a guess: "))

        if guess > num:
            print("Too high.")

        elif guess < num:
            print("Too low.")
        else:
            game_over = True
            return "You guessed the correct number! You win!"

        if attempts>0:
            return "Guess again."
        else:
            game_over = True
            return f"You lose. You are out of attempts. The answer was {num}"


    while game_over==False:
        print(guess_the_num())


