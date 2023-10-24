"""EX 03: Structured Wordle!"""

__author__ = "730387751"


# Function for searching for characters in a string
def contains_char(secret_word: str, chr_of_guess: str) -> bool:
    """Checking to see if character is in secret word."""
    assert len(chr_of_guess) == 1
    idx = 0
    # If character is in word return true
    while idx < len(secret_word):
        if secret_word[idx] == chr_of_guess:
            return True
        idx += 1
    return False  # If we get here, we didn't find it


# Function for printing emoji boxes
def emojified(guess: str, secret_word: str) -> str:
    """Printing Guess results in emoji boxes."""
    assert len(guess) == len(secret_word)
    # Defining variables
    idx = 0
    result: str = ""
    White_Box: str = "\U00002B1C"
    Green_Box: str = "\U0001F7E9"
    Yellow_Box: str = "\U0001F7E8"
    # Loop for printing boxes
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:
            result += Green_Box
        elif contains_char(secret_word, guess[idx]):
            result += Yellow_Box
        else: 
            result += White_Box
        idx += 1
    return result


# Function for asking for guess and checking length
def input_guess(length_of_secret: int) -> str:
    """Asking for guess and making sure it is the right length."""
    guess = input(f"Enter a {length_of_secret} character word:")
    # If guess is wrong length ask again until correct
    while len(guess) != length_of_secret:
        guess = input(f"That wasn't {length_of_secret} chars! Try again: ")

    return guess  # If we get here guess is the right length


# Function for main game play
def main() -> None:
    """The entry poing of the program and # Your code will go here."""
    # Defining variables
    secret_word: str = "fires"
    length: int = len(secret_word)
    current_try: int = 1
    max_tries: int = 6
    # Loop for game play
    while current_try <= max_tries:
        print(f"=== Turn {current_try}/{max_tries} ===")
        guess: str = input_guess(length)
        print(emojified(guess, secret_word))
        # If correct guess win and exit game
        if guess == secret_word:
            print(f"You won in {current_try}/{max_tries} turns!")
            break  # Exit game when correct guess is achevied.
        current_try += 1
    # If no correct guess
    if current_try > max_tries:
        print(f"X/{max_tries} - Sorry, try again tomorrow!")


# Calling main function
if __name__ == "__main__":
    main()