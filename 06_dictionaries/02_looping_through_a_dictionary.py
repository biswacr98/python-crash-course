# Looping Through a Dictionary
# ----------------------------

# Looping Through All Key-Value Pairs
# ------------------------------------

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Output:
# Key: username
# Value: efermi

# Key: first
# Value: enrico

# Key: last
# Value: fermi

# - The method items() returns a sequence of key-value pairs.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Output:
# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Rust.
# Phil's favorite language is Python.

# Looping Through All the Keys in a Dictionary
# --------------------------------------------

# - The method keys() is useful when you don't need to work with all of the values in a dictionary.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name in favorite_languages.keys():
    print(name.title())

# Output:
# Jen
# Sarah
# Edward
# Phil

# - Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote:

for name in favorite_languages:
    print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Output:
# Hi Jen.
# Hi Sarah.
# 	Sarah, I see you love C!
# Hi Edward.
# Hi Phil.
# 	Phil, I see you love Python!

# - You can also use the keys() method to find out if a particular person was polled.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Output:
# Erin, please take our poll!

# - The keys() method isn't just for looping: It actually returns a list of all the keys, and the line if 'erin' not in favorite_languages.keys(): checks whether 'erin' is one of the keys in the dictionary.

# Looping Through a Dictionary's Keys in Order
# --------------------------------------------

# - Sorted Order

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Output:
# Edward, thank you for taking the poll.
# Jen, thank you for taking the poll.
# Phil, thank you for taking the poll.
# Sarah, thank you for taking the poll.

# Looping Through All Values in a Dictionary
# ------------------------------------------

# - The values() method returns a list of values without any keys.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Output:
# The following languages have been mentioned:
# Python
# C
# Rust
# Python

# - This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list.

# - To see each language chosen without repetition, we can use a set. A set is similar to a list except that each item in the set must be unique.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Output:
# The following languages have been mentioned:
# Python
# C
# Rust

# - Build a set directly using braces and separating the elements with commas.

languages = {'python', 'ruby', 'python', 'c'}
print(languages) # {'python', 'ruby', 'c'}

# - When you see braces but no key-value pairs, you're looking at a set.
