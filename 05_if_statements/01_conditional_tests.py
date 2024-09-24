cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Output:
# Audi
# BMW
# Subaru
# Toyota

# Conditional Tests
# ------------------

# - At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test.
# - Python uses the values True and False to decide whether the code in an if statement should be executed.
# - If a conditional test evaluates to True, Python executes the code following the if statement.
# - If the test evaluates to False, Python ignores the code following the if statement.

# Checking for Equality
# ----------------------

# - Most conditional tests compare the current value of a variable to a specific value of interest.
# - The simplest conditional test checks whether the value of a variable is equal to the value of interest.

car = 'bmw'
print(car == 'bmw') # True

# - The double equal sign or the equality operator returns True if the values on the left and right side of the operator match, and False if they don't match.

# - The assignment operator (=) is used to assign a value to a variable.

# Ignoring Case When Checking for Equality
# ------------------------------------------

# - Testing for equality is cas`e-sensitive in Python.
# - For example, two values with different capitalization are not considered equal.

car = 'Audi'
print(car == 'audi') # False

# - If you want to just test the equality of the values, you can convert the values to lowercase before doing the comparison.

car = 'Audi'
print(car.lower() == 'audi') # True

# Checking for Inequality
# ------------------------

# - When you want to determine whether two values are not equal, you can use an inequality operator (!=).

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

# Output:
# Hold the anchovies!

# Numerical Comparisons
# ----------------------

# - Test to see if two numbers are equal or not.

age = 18
print(age == 18) # True

# - You can also test to see if two numbers are not equal.

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# Output:
# That is not the correct answer. Please try again!

# - You can include various mathematical comparisons in your conditional statements. For example, you can check if a number is greater than, less than, greater than or equal to, or less than or equal to another number.

age = 19

print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# Checking Multiple Conditions
# -----------------------------

# Using and to Check Multiple Conditions
# ----------------------------------------

# - To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests.
# - If each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.

age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21) # False

age_1 = 22

print(age_0 >= 21 and age_1 >= 21) # True

# - To improve readability, we can use parentheses around the individual tests, but they are not required.

print((age_0 >= 21) and (age_1 >= 21)) # True

# Using or to Check Multiple Conditions
# ---------------------------------------

# - The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass.
# - An or expression fails only when both individual tests fail.

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21) # True

age_0 = 18

print(age_0 >= 21 or age_1 >= 21) # False


# Checking Whether a Value Is in a List
# ---------------------------------------

# - It's important to check whether a list contains a certain value before taking an action.
# - You can use the keyword in to check if a value is in a list.

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings) # True

print('pepperoni' in requested_toppings) # False

# Checking Whether a Value Is Not in a List
# -------------------------------------------
# - You can also check if a value is not in a list using the keyword not in.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Output:
# Marie, you can post a response if you wish.

# Boolean Expressions
# --------------------

# - A boolean expression is just another name for a conditional test.
# - A boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.

game_active = True
can_edit = False
