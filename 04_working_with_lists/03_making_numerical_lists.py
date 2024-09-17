# Making Numerical Lists
# -----------------------
# - Lists are ideal for storing sets of numbers, and Python provides a number of tools to help you work efficiently with lists of numbers.

# Using the range() Function
# ---------------------------
# - Python's range() function makes it easy to generate a series of numbers.

for value in range(1,5):
    print(value)
# 1
# 2
# 3
# 4

# - In this example, range() prints only the numbers 1 through 4. The output does not include 5 because range() stops one number before the stop value you specify.
# - This is a result of the off-by-one behavior you'll see often in programming languages.
# - The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.

# - To print the numbers from 1 to 5, you would use range(1,6).

for value in range(1,6):
    print(value)
# 1
# 2
# 3
# 4
# 5

# - You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example, range(6) would return the numbers 0-5.

for value in range(6):
    print(value)

# 0
# 1
# 2
# 3
# 4
# 5

# Using range() to Make a List of Numbers
# ----------------------------------------
# - If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.
# - When you wrap list() around a call to the range() function, the output will be a list of numbers.

numbers = list(range(1,6))
print(numbers)
# [1, 2, 3, 4, 5]

# - You can also use the range() function to tell Python to skip numbers in a given range.
# - If you pass a third argument to range(), Python uses that value as a step size when generating numbers.

even_numbers = list(range(2,11,2))
print(even_numbers)
# [2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# - A concise way

squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Simple Statistics with a List of Numbers
# -----------------------------------------
# - A few Python functions are specific to lists of numbers.
# - For example, you can easily find the minimum, maximum, and sum of a list of numbers.

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45

# List Comprehensions
# -------------------
# - A list comprehension allows you to generate this same list in just one line of code.
# - A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.

squares = [value ** 2 for value in range(1,11)]
print(squares)
