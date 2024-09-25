# Exercise 5:

# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

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
