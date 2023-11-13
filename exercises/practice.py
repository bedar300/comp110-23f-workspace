
def odd_and_even(list: list[int]) -> list[int]:
    """Create a new list with odd numbers that have even indexes from previous list."""""
    new_list = []
    for i in range(len(list)):
        if list[i] % 2 != 0 and i % 2 == 0:
            new_list.append(list[i])
    return new_list

def value_exists(dict: dict[str, int], x: int) -> bool:
    """Return True if x is a value in the dictionary."""
    for key in dict:
        if dict[key] == x:
            return True  
    return False  # If we get here, x is not in the dictionary
        
def short_words(list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters long."""
    new_list = []
    for word in list:
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} is too long!")
    return new_list

my_list_1: list[int] = [1, 2, 7, 5, 8, 13, 11, 20]
my_list_2: list[str] = ["sun", "cloud", "sky"]
my_dict_1: dict[str, int] = {"a": 2, "b": 4, "c": 7, "d": 1}
test_val: int = 7

print(odd_and_even(my_list_1))
print(value_exists(my_dict_1, test_val))
print(short_words(my_list_2))

