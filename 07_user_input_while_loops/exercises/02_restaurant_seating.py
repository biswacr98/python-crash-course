# Exercise 2:

# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

people = int(input("How many people are in your dinner group? "))

if people > 8:
    print("I'm sorry, you'll have to wait for a table.")

else:
    print("Your table is ready.")
