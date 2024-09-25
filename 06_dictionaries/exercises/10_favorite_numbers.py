# Exercise 10:

# Modify your program from Exercise 2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'alice': [1, 2, 3],
    'bob': [4, 5, 6],
    'charlie': [7, 8, 9],
    'david': [10, 11, 12],
    'eve': [13, 14, 15],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print()
