"""Instantiating a class."""



# import the class
# from ,file_name>.<module_name> import <class_name>

from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True)  # Contructor

# access/set/update atrributes
# my_pizza.size = "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True

print("Size:")
print(my_pizza.size)

# Make sals_pizza size medium, 5 toppings, not gluten free
sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    """Comput the price of a pizza"""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings

    if input_pizza.gluten_free:
        cost += 1.00
    return cost

# Calling function
print(price(my_pizza))
print(price(sals_pizza))

# Calling methods
print(my_pizza.price())
print(sals_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_pizza_second_pizza: Pizza = my_pizza.add_toppings_new_order(2)
print(my_pizza_second_pizza.toppings)