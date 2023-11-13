"""Class 04 practice."""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words): 
        return("Index too high")
    return my_words[letter_idx]  # If we get here index is valid
    
my_words = input("Enter a word: ")
letter_idx = int(input("Enter an index: "))

print(mimic_letter(my_words, letter_idx))