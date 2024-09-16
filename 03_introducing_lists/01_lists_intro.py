# Lists
# -------
# - A list is a collection of items in a particular order.
# - Put anything you want in a list, and items in your list don't have to be related in any particular way.
# - You can put numbers, letters, strings, and even other lists in your lists.
# - In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # ['trek', 'cannondale', 'redline', 'specialized']

# Accessing Elements in a List
# -----------------------------
# - Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.
# - To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # trek

# - When we ask for a single item from a list, Python returns just that element without square brackets.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title()) # Trek (title() method uses Title Case, where each word begins with a capital letter)

# Index Positions Start at 0, Not 1
# -----------------------------------
# - Python considers the first item in a list to be at position 0, not position 1.
# - The second item in a list has an index of 1.
# - Using this counting system, you can get any element you want from a list by subtracting one from its position in the list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1]) # cannondale
print(bicycles[3]) # specialized

# - Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # specialized

# - The index = -2 returns the second item from the end of the list, the index = -3 returns the third item from the end, and so forth.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-2]) # redline
print(bicycles[-3]) # cannondale

# Using Individual Values from a List
# -------------------------------------
# - You can use individual values from a list just as you would any other variable.
# - For example, you can use f-strings to create a message based on a value from a list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message) # My first bicycle was a Trek.
