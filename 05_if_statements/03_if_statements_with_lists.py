# Using if Statements with Lists
# -------------------------------

# - Watch for special values that need to be treated differently than other values in the list of values you're processing.
# - You can efficiently manage changing conditions, such as the availability of certain items in a restaurant throughout a shift.

# Checking for Special Items
# ---------------------------

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# Output:
# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.

# Finished making your pizza!

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# Output:
# Adding mushrooms.
# Sorry, we are out of green peppers right now.
# Adding extra cheese.

# Finished making your pizza!

# Checking That a List Is Not Empty
# ----------------------------------

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")

else:
    print("Are you sure you want a plain pizza?")

# Output: Are you sure you want a plain pizza?

# - When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.

# Using Multiple Lists
# ---------------------

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

# Output:
# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.

# Finished making your pizza!
