# Exercise 6:

# Use the code in favorite_languages dictionary.

# - Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.

# - Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'sarah', 'edward', 'phil', 'erin', 'jim']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")

# Output:
# Thank you for taking the poll, Jen!
# Thank you for taking the poll, Sarah!
# Thank you for taking the poll, Edward!
# Thank you for taking the poll, Phil!
# Erin, please take the poll!
# Jim, please take the poll!

