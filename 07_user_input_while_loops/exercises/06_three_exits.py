# Exercise 6:

# Write different versions of exercises/ 05_movie_tickets.py that do each of the following at least once:
# - Use a conditional test in the while statement to stop the loop.
# - Use an active variable to control how long the loop runs.
# - Use a break statement to exit the loop when the user enters a 'quit' value.

# Conditional test in the while statement to stop the loop
person_age = input("Please enter your age: ")

while person_age != 'quit':
    person_age = int(person_age)
    if person_age < 3:
        print("Your ticket is free!")
    elif person_age >= 3 and person_age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
    person_age = input("Please enter your age: ")

# Active variable to control how long the loop runs

prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    person_age = input(prompt)

    if person_age == 'quit':
        active = False
    else:
        person_age = int(person_age)
        if person_age < 3:
            print("Your ticket is free!")
        elif person_age >= 3 and person_age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

# Break statement to exit the loop when the user enters a 'quit' value

prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' to end the program. "

while True:

    person_age = input(prompt)

    if person_age == 'quit':
        break
    else:
        person_age = int(person_age)
        if person_age < 3:
            print("Your ticket is free!")
        elif person_age >= 3 and person_age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
            
