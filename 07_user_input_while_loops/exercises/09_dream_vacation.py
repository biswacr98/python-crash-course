# Exercise 9:

# Write a program that polls users about their dream vacation. Write a prompt similar to "If you could visit one place in the world, where would you go?" Include a block of code that prints the results of the poll.

prompt = "\nIf you could visit one place in the world, where would you go? "
prompt += "\nEnter 'quit' to end the program. "

dream_vacations = []

while True:
    dream_vacation = input(prompt)

    if dream_vacation == 'quit':
        break
    else:
        dream_vacations.append(dream_vacation)

print("\n--- Dream Vacations ---")
for dream_vacation in dream_vacations:
    print(dream_vacation.title())

