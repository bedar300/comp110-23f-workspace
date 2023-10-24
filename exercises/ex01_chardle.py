"""EX01 - Chardle - A cute step toward Wordle!"""

__author__ = "730387751"

# Prompt for 5 character word
five_characterword: str = input("Enter a 5-character word:")
# Checking length of 5 character word
length_5 = len(five_characterword)
if length_5 != 5:
    False
    print("Error: Word must contain 5 characters")
    exit()
else:   
    instance_of_chr = 0
    # Prompt for one character word
    one_character: str = input("Enter a single character:")
    # Defining variables
    length_1 = len(one_character)
    
    if length_1 != 1:
        print("Error: Character must be a single character")
        exit()
    else:
        print("Searching for " + str(one_character) + " in " + str(five_characterword))
        # searching for letters at each index and adding to instance count
        if five_characterword[0] == one_character:
            print(str(one_character) + " found at index 0")
            instance_of_chr += 1

        if five_characterword[1] == one_character:
            print(str(one_character) + " found at index 1")
            instance_of_chr += 1

        if five_characterword[2] == one_character:
            print(str(one_character) + " found at index 2")
            instance_of_chr += 1

        if five_characterword[3] == one_character:
            print(str(one_character) + " found at index 3")
            instance_of_chr += 1

        if five_characterword[4] == one_character:
            print(str(one_character) + " found at index 4")
            instance_of_chr += 1
        # print instance count
        if instance_of_chr == 0:
            print("No instances of " + one_character + " found in " + five_characterword)

        if instance_of_chr == 1:
            print(str(instance_of_chr) + " instance of " + one_character + " found in " + five_characterword)

        if instance_of_chr >= 2:
            print(str(instance_of_chr) + " instances of " + one_character + " found in " + five_characterword) 