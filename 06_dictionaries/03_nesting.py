# Nesting
# --------

# - Store multiple dictionaries in a list or a list of items as a value in a dictionary.
# - This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

# A List of Dictionaries
# ----------------------

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Output:
# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Output:
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...
# Total number of aliens: 30

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the first 3 aliens to yellow, medium-speed aliens worth 10 points each.
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Output:
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the first 3 aliens to yellow, medium-speed aliens worth 10 points each. Use an elif block to change the color of the second alien to red and give it a speed of fast worth 15 points each.

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# A List in a Dictionary
# -----------------------

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python ', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Output:
# Jen's favorite languages are:
#     Python
#     Rust

# Sarah's favorite languages are:
#     C

# Edward's favorite languages are:
#     Ruby
#     Go

# Phil's favorite languages are:
#     Python
#     Haskell

# - Should not nest lists and dictionaries too deeply.

# A Dictionary in a Dictionary
# ----------------------------

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',

    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
