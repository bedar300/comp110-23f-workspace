"""EX 02: One Shot Wordle!"""

__author__ = "730387751"
# defining secret word and length variable
secret_word = 'python'
length = len(secret_word)
# asking for guess
guess = input(f"What is your {length} letter guess?")
# check length of guess and loop till it is correct amount of characters
while len(guess) != len(secret_word):
    guess = input(f"That was not {length} letters! Try again:")
# creating variables
character_idx = 0
White_Box: str = "\U00002B1C"
Green_Box: str = "\U0001F7E9"
Yellow_Box: str = "\U0001F7E8"
result_of_guess = ""
# loop through each character in guess
while character_idx < length: 
    chr_in_other_idx = [False] * length
    alt_idx = 0
    # character is in same index add green box
    if guess[character_idx] == secret_word[character_idx]:
        result_of_guess += Green_Box
        chr_in_other_idx[character_idx] = True

    # character is in other index add yellow box
    while chr_in_other_idx[character_idx] is not True and alt_idx < length:
        if guess[character_idx] == secret_word[alt_idx]:
            chr_in_other_idx[character_idx] = True
        alt_idx += 1
    # character is in other index add yellow box
    if chr_in_other_idx[character_idx] is True and guess[character_idx] != secret_word[character_idx]:
        result_of_guess += Yellow_Box 
    # character is not in secret word add white box     
    elif chr_in_other_idx[character_idx] is False:
        result_of_guess += White_Box
    character_idx += 1  
# Print result of guess
print(result_of_guess)
# Print if guess is correct or not
if result_of_guess == Green_Box * length:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")