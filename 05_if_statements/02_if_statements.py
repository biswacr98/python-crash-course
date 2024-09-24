# Simplest if statements
# -----------------------

age = 19
if age >= 18:
    print("You are old enough to vote!")

# Output: You are old enough to vote!

# - All indented lines after the if statement run if the test passes, and the entire block of code is skipped if the test does not pass.

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# Output:
# You are old enough to vote!
# Have you registered to vote yet?

# if-else statements
# ------------------

# - Often, you'll want to take one action when a conditional test passes and a different action in all other cases.

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# Output:
# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!


# if-elif-else chain
# ------------------

# - Often, you'll need to test more than two possible situations, and to evaluate these you can use Python's if-elif-else syntax.

age = 12
if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $25.")

else:
    print("Your admission cost is $40.")

# Output: Your admission cost is $25.

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

else:
    price = 40

print(f"Your admission cost is ${price}.")

# Output: Your admission cost is $25.

# Using multiple elif blocks
# --------------------------

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

else:
    price = 20

print(f"Your admission cost is ${price}.")

# Output: Your admission cost is $25.

# Omitting the else block
# -----------------------

# - Python does not require an else block at the end of an if-elif chain.
# - Sometimes an else block is useful; sometimes it is clearer to use an additional elif statement that catches specific conditions.

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

# Output: Your admission cost is $25.

# - The else block is a catchall statement. It matches any condition that was not matched by a specific if or elif test, and that can sometimes include invalid or malicious data.
# - If you have a specific final condition you are testing for, consider using a final elif block and omit the else block.


# Testing multiple conditions
# ---------------------------

# - The if-elif-else chain is powerful, but it's only appropriate to use when you just need one test to pass.
# - As soon as Python finds one test that passes, it skips the rest of the tests.
# - This behavior is beneficial because it's efficient and allows you to test for one specific condition.
# - However, sometimes you want to check all of the conditions of interest.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# Output:
# Adding mushrooms.
# Adding extra cheese.

# Finished making your pizza!

# - The code checks for each requested topping in the list of requested_toppings.

# - If you want to test for only one condition, use an if-elif-else chain.
# - If you need to test for more than one condition, use a series of independent if statements.
