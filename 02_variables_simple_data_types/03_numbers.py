# Numbers
# -------
# - Keep Score in Games
# - Represent Data in Visualizations
# - Store Information in Web Applications
# - Python manages numbers in a variety of ways, including integers and floats.

# Integers
# ---------
# - Integers are whole numbers.
# - You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.

print(2 + 3) # 5
print(3 - 2) # 1
print(2 * 3) # 6
print(3 / 2) # 1.5
# - Python uses two multiplication symbols to represent exponents:

print(3 ** 2) # 9
print(3 ** 3) # 27
print(10 ** 6) # 1000000

# - Python supports the order of operations too, so you can use multiple operations in one expression.
# - You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify.

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

# - Spaces around the +, -, *, and / operators are optional, but the use of spaces can make your code easier to read.

# Floats
# -------
# - Python calls any number with a decimal point a float.

print(0.1 + 0.1) # 0.2
print(0.2 + 0.2) # 0.4
print(2 * 0.1) # 0.2
print(2 * 0.2) # 0.4

# - Be aware that you can sometimes get an arbitrary number of decimal places in your answer.

print(0.2 + 0.1) # 0.30000000000000004
print(3 * 0.1) # 0.30000000000000004

# - Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally.

# Integers and Floats
# --------------------
# - When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float.

print(4 / 2) # 2.0

# - If you mix an integer and a float in any other operation, you'll get a float as well.

print(1 + 2.0) # 3.0
print(2 * 3.0) # 6.0
print(3.0 ** 2) # 9.0

# - Python defaults to a float in any operation that uses a float, even if the output is a whole number.

# Underscores in Numbers
# -----------------------
# - When you're writing long numbers, you can group digits using underscores to make large numbers more readable.

universe_age = 14_000_000_000
print(universe_age) # 14000000000

# - Python completely ignores the underscores when storing these values, so you can use them to help you read the code.

# Multiple Assignment
# --------------------
# - You can assign values to more than one variable using just a single line.

x, y, z = 0, 0, 0

# - This technique is useful when you need to initialize a set of variables.

# Constants
# ----------
# - A constant is like a variable whose value stays the same throughout the life of a program.
# - Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed.

MAX_CONNECTIONS = 5000

# - Comments
# ----------
# - Comment allows you to write notes in English within your programs.
# - In Python, the # symbol indicates a comment.

# Say hello to everyone.
print("Hello Python people!")

# - Comments are ignored by the Python interpreter.
# - Write clear, concise comments that explain what your code does.

# Zen of Python
# --------------

import this
# - The Zen of Python is a collection of 19 software principles that influence the design of the Python programming language.

print(this)


# The Zen of Python, by Tim Peters
# -  Beautiful is better than ugly.
# -  Explicit is better than implicit.
# -  Simple is better than complex.
# -  Complex is better than complicated.
# -  Flat is better than nested.
# -  Sparse is better than dense.
# -  Readability counts.
# -  Special cases aren't special enough to break the rules.
# -  Although practicality beats purity.
# -  Errors should never pass silently.
# -  Unless explicitly silenced.
# -  In the face of ambiguity, refuse the temptation to guess.
# -  There should be one-- and preferably only one --obvious way to do it.
# -  Although that way may not be obvious at first unless you're Dutch.
# -  Now is better than never.
# -  Although never is often better than *right* now.
# -  If the implementation is hard to explain, it's a bad idea.
# -  If the implementation is easy to explain, it may be a good idea.
# -  Namespaces are one honking great idea -- let's do more of those!
