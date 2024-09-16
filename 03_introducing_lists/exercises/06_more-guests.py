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

