# Exercise - 4:

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

# Example Output:
# Enter a pizza topping: mushrooms
# I'll add mushrooms to your pizza.
# Enter a pizza topping: green peppers
# I'll add green peppers to your pizza.
# Enter a pizza topping: quit

pizza_topping = input("Enter a pizza topping: ")

while pizza_topping != 'quit':
    print(f"I'll add {pizza_topping} to your pizza.")
    pizza_topping = input("Enter a pizza topping: ")


