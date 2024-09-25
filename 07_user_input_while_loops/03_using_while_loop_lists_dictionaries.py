# Using while loop with Lists and Dictionaries
#  -------------------------------------------

# - A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop.
# - Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

# Moving Items from One List to Another
# -------------------------------------

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Output:
# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

# The following users have been confirmed:
# Candace
# Brian
# Alice

# Removing All Instances of Specific Values from a List
# -----------------------------------------------------

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Output:
# ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ['dog', 'dog', 'goldfish', 'rabbit']

# Filling a Dictionary with User Input
# -------------------------------------

responses = {}

# Set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# Output:
# What is your name? Alice
# Which mountain would you like to climb someday? Denali
# Would you like to let another person respond? (yes/ no) yes

# What is your name? Bob
# Which mountain would you like to climb someday? Everest
# Would you like to let another person respond? (yes/ no) no

# --- Poll Results ---
# Alice would like to climb Denali.
# Bob would like to climb Everest.
