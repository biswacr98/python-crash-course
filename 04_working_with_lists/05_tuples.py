# Tuples
# -------
# - Lists work well for storing collection of items that can change throughout the life of a program.
# - However, sometimes you'll want to create a list of items that cannot change.
# - Python refers to the values that cannot change as immutable, and an immutable list is called a tuple.

# Defining a Tuple
# -----------------
# - A tuple looks just like a list except you use parentheses instead of square brackets.
# - Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list.

dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50

# - If we try to change one of the items in the tuple, we'll get an error.

# dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment

# - Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:

my_t = (3,)

# - It doesn't often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.

# Looping Through All Values in a Tuple
# ---------------------------------------
# - You can loop over all the values in a tuple using a for loop, just as you did with a list.

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 200
# 50

# Writing over a Tuple
# ---------------------
# - Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple.

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Original dimensions:
# 200
# 50

# Modified dimensions:
# 400
# 100

# - When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should not be changed throughout the life of a program.
