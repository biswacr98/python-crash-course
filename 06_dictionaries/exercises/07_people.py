# Exercise 7:

# Start with the program you wrote for Exercise 1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

people = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'city': 'New York'
    },
    {
        'first_name': 'Jane',
        'last_name': 'Smith',
        'age': 25,
        'city': 'Los Angeles'
    },
    {
        'first_name': 'Michael',
        'last_name': 'Johnson',
        'age': 35,
        'city': 'Chicago'
    }
]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print()


