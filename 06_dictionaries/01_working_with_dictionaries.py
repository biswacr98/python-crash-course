# Working with Dictionaries
# --------------------------

# - A dictionary in Python is a collection of key-value pairs.
# - Each key is connected to a value, and you can use a key to access the value associated with that key.
# - A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.
# - In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces.

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color']) # green
print(alien_0['points']) # 5

# - A key-value pair is a set of values associated with each other.
# - When you provide a key, Python returns the value associated with that key.
# - Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.

# Accessing Values in a Dictionary
# ---------------------------------

alien_0 = {'color': 'green'}

print(alien_0['color']) # green

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']

print(f"You just earned {new_points} points!") # You just earned 5 points!

# Adding New Key-Value Pairs
# --------------------------

# - Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
# - To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# - Dictionaries retain the order in which they were defined.
# - When you print a dictionary or loop through its elements, you will see the elements in the same order in which they were added to the dictionary.

# Starting with an Empty Dictionary
# ---------------------------------

# - It’s sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it.

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0) # {'color': 'green', 'points': 5}

# Modifying Values in a Dictionary
# --------------------------------

# - To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.") # The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") # The alien is now yellow.

#------

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Output:
# Original position: 0
# New position: 2

# Removing Key-Value Pairs
# ------------------------

# - When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair.
# - All del needs is the name of the dictionary and the key that you want to remove.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0) # {'color': 'green'}

# - Be aware that the deleted key-value pair is removed permanently.

# A Dictionary of Similar Objects
# -------------------------------

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.") # Sarah's favorite language is C.

# Using get() to Access Values
# ----------------------------

# - Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # KeyError: 'points'

# - For dictionaries, specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.
# - The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist.

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) # No point value assigned.

# - If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value.
