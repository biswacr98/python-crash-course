# Exercise 7:

# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will welcome people to your application on login. Loop through the list and print a greeting to each user, and a special greeting to the admin.
# - If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# - Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

usernames = ['admin', 'eric', 'john', 'jane', 'joe']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# Output:
# Hello admin, would you like to see a status report?
# Hello eric, thank you for logging in again.
# Hello john, thank you for logging in again.
# Hello jane, thank you for logging in again.
# Hello joe, thank you for logging in again.
