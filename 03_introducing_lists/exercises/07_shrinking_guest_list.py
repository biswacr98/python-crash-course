# Exercise 7:
# You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
# Start with your program from Exercise 6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# Exercise 6:
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 4 or Exercise 5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"Hello {guests[0]}, would you like to join me for dinner?")
print(f"Hello {guests[1]}, would you like to join me for dinner?")
print(f"Hello {guests[2]}, would you like to join me for dinner?")
print(f"Hello {guests[3]}, would you like to join me for dinner?")
print(f"Hello {guests[4]}, would you like to join me for dinner?")

print(f"{guests[4]} can't make it to dinner.")

guests[4] = "Frank"
print(f"Hello {guests[0]}, would you like to join me for dinner?")
print(f"Hello {guests[1]}, would you like to join me for dinner?")
print(f"Hello {guests[2]}, would you like to join me for dinner?")
print(f"Hello {guests[3]}, would you like to join me for dinner?")
print(f"Hello {guests[4]}, would you like to join me for dinner?")

print("I found a bigger dinner table!")

guests.insert(0, "Grace")
guests.insert(3, "Helen")
guests.append("Ivy")

print(f"Hello {guests[0]}, would you like to join me for dinner?")
print(f"Hello {guests[1]}, would you like to join me for dinner?")
print(f"Hello {guests[2]}, would you like to join me for dinner?")
print(f"Hello {guests[3]}, would you like to join me for dinner?")
print(f"Hello {guests[4]}, would you like to join me for dinner?")
print(f"Hello {guests[5]}, would you like to join me for dinner?")
print(f"Hello {guests[6]}, would you like to join me for dinner?")
print(f"Hello {guests[7]}, would you like to join me for dinner?")

print("\nI can only invite two people for dinner.")

print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner.")

print(f"{guests[0]}, you're still invited to dinner.")
print(f"{guests[1]}, you're still invited to dinner.")

del guests[1]
del guests[0]
print(guests)
