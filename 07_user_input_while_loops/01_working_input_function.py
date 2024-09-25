# How the input() function works
# ------------------------------

# - The input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it stores it in a variable to make it convenient for you to work with.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Output:
# Tell me something, and I will repeat it back to you: Hello everyone!
# Hello everyone!

# - The input() function takes one argument: the prompt that we want to display to the user so they know what kind of information to enter.

# Writing Clear Prompts
# ----------------------

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Output:
# Please enter your name: Alice
# Hello, Alice!

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Output:
# If you tell us who you are, we can personalize the messages you see.
# What is your first name? Alice
# Hello, Alice!

# Using int() to Accept Numerical Input
# --------------------------------------

# - When you use the input() function, Python interprets everything the user enters as a string.

age = input("How old are you? ")
print(age)

# Output:
# How old are you? 21
# 21

age = input("How old are you? ")
print(age)
#print(age >= 18) # TypeError: '>=' not supported between instances of 'str' and 'int'

age = input("How old are you? ")
age = int(age)
print(age)
print(age >= 18)

# Output:
# How old are you? 21
# 21
# True

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Output:
# How tall are you, in inches? 71
# You're tall enough to ride!

# The Modulo Operator
# -------------------

# - A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder.

print(4 % 3) # 1
print(5 % 3) # 2
print(6 % 3) # 0
print(7 % 3) # 1

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")

else:
    print(f"\nThe number {number} is odd.")

# Output:
# Enter a number, and I'll tell you if it's even or odd: 10
# The number 10 is even.
