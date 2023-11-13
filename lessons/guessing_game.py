""""Program that loops untill correct number is guessed"""

from random import randint

secret: int = randint(1, 10)
guess: int = int(input("Guess a number between 1 and 10: "))
guess_count: int = 1
max_tries: int = 3
while (guess != secret) and (guess_count < max_tries):
    print("Wrong! ")
    # If guess is out of bounds
    if guess < 1 or guess > 10:
        print("That is not between 1 and 10!")
    # If guess is too low
    if guess < secret:
        print("Too low!")
    else: # guess must be greater than secret
        print("Too high!")
    # tell them how many tries they have left and guess again
    print(f" You have {max_tries - guess_count} tries left")
    guess = int(input("Guess again: "))
    guess_count += 1
   
# If i've reached this point, guess == secret
if guess == secret:
    print("You got it!")
else: 
    print("You lose :(")
