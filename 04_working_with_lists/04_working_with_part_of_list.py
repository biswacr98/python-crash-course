# Working With Part of a List
# ---------------------------
# - Work with a specific group of items in a list, Python allows you to work with a slice.

# Slicing a List
# --------------
# - To make a slice, you specify the index of the first and last elements you want to work with.
# - As with the range() function, Python stops one item before the second index you specify.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']

# - Generate any subset of a list.
# - If you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4.

print(players[1:4]) # ['martina', 'michael', 'florence']

# - If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) # ['charles', 'martina', 'michael', 'florence']

# - A similar syntax works if you want a slice that includes the end of a list.
# - If you want all items from the third item through the last item, you can start with index 2 and omit the second index.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) # ['michael', 'florence', 'eli']

# - This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list.

# - If you want to output the last three players on the roster, you can use the slice players[-3:].

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli']

# - You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

# Looping Through a Slice
# -----------------------
# - You can use a slice in a for loop if you want to loop through a subset of the elements in a list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Here are the first three players on my team:
# Charles
# Martina
# Michael

# - When you're  working with data, you can use slices to process your data in chunks of a specific size.
# - When you're building a web application, you can use slices to display information in a series of pages with an appropriate amount of information on each page.

# Copying a List
# --------------
# - You'll want to start with an existing list and make an entirely new list based on the first one.
# - To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).
# - This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# - To prove we actually have two separate lists, we'll add a new food to each list and show that each list keeps track of the appropriate person's favorite foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']

# - Copy a list withoout using a slice.

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# - This code doesn't copy the list my_foods to the list friend_foods; it makes friend_foods simply an alias for my_foods.

# - This syntax actually tells Python to connect the new variable friend_foods to the list that my_foods is connected to, so now both variables point to the same list.

# - This output shows that both lists are the same.
