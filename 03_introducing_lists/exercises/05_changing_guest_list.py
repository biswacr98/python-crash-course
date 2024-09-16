# Exercise 5:
# You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
# Start with your program from Exercise 4. Add a print() call at the end of your program stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

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
