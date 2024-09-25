# Exercise 8:

# Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

pets = [
    {
        'name': 'dog',
        'kind': 'mammal',
        'owner': 'John'
    },
    {
        'name': 'cat',
        'kind': 'mammal',
        'owner': 'Jane'
    },
    {
        'name': 'rabbit',
        'kind': 'mammal',
        'owner': 'Michael'
    }
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()


