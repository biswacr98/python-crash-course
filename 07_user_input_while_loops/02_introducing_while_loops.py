# Introducing While Loops
# ------------------------

# The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.

# The while loop in action
# ------------------------

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# Letting the user choose when to quit
# -------------------------------------

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)

# Output:
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. How are you doing?
# How are you doing?

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit
# quit

# Use a if statement to prevent printing 'quit' after the user enters it.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Output:
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. How are you doing?
# How are you doing?

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit

# Using a flag
# -------------

# - For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program.
# - We can write our programs so they run while the flag is set to True and stop when any of several events sets the value of the flag to False.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Output:
# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. How are you doing?
# How are you doing?

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit

# Using break to Exit a Loop
# ---------------------------

# - To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.
# - The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren't, so the program only executes code that you want it to, when you want it to.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Output:
# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) New York
# I'd love to go to New York!

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) Paris
# I'd love to go to Paris!

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) quit

# - You can use the break statement in any of Python's loops. For example, you could use break to quit a for loop that is working through a list or a dictionary.

# Using continue in a Loop
# -------------------------

# - Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Output:
# 1
# 3
# 5
# 7
# 9

# Avoiding Infinite Loops
# ------------------------

# - Every while loop needs a way to stop running so it won't continue to run forever.

x = 1
while x <= 5:
    print(x)
    x += 1

# This loop runs forever because there is no way for the loop to stop running.
# x = 1
# while x <= 5:
#     print(x)

# - If your program gets stuck in an infinite loop, press Ctrl + C or just close the terminal.
