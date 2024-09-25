# Exercise 2:

# Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    'john': 7,
    'jane': 3,
    'jim': 8,
    'jill': 10,
    'jack': 5
}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")

# Output:
# John's favorite number is 7.
# Jane's favorite number is 3.
# Jim's favorite number is 8.
# Jill's favorite number is 10.
# Jack's favorite number is 5.
