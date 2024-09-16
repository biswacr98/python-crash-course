# Modifying, Adding, and Removing Elements in a List
# -----------------------------------------------------
# - Most lists you create will be dynamic, meaning you'll build a list and then add and remove elements from it as your program runs its course.

# Modifying Elements in a List
# -----------------------------
# - To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# - Change the value of any item in the list, not just the first item.

# Adding Elements to a List
# ---------------------------
# - Python provides several ways to add new data to a list.

# Appending Elements to the End of a List
# ----------------------------------------
# - Add a new element to a list using append the item to the list.
# - When you use the append() method, the new element is added to the end of the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

# - Start with an empty list and then add items to the list using a series of append() calls.

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# - To put your users in control, start by defining an empty list that will hold the users' values. Then append each new value provided to the list.

# Inserting Elements into a List
# --------------------------------
# - You can add a new element at any position in your list by using the insert() method.
# - You do this by specifying the index of the new element and the value of the new item.

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']

# - The insert() method opens a space at position 0 and stores the value.
# - This operation shifts every other value in the list one position to the right.

# Removing Elements from a List
# ------------------------------
# - Remove an item according to its position in the list or according to its value.

# Removing an Item Using the del Statement
# -----------------------------------------
# - If you know the position of the item you want to remove from a list, you can use the del statement.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles) # ['yamaha', 'suzuki']

# - You can remove an item from any position in a list using the del statement if you know its index.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

del motorcycles[1]
print(motorcycles) # ['honda', 'suzuki']

# Removing an Item Using the pop() Method
# ----------------------------------------
# - The pop() method removes the last item in a list, but it lets you work with that item after removing it.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha']
print(popped_motorcycle) # suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.") # The last motorcycle I owned was a Suzuki.

# Popping Items from any Position in a List
# ------------------------------------------
# - You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in the parentheses.

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.") # The first motorcycle I owned was a Honda.

# - When you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

# Removing an Item by Value
# --------------------------
# - If you only know the value of the item you want to remove, you can use the remove() method.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# - Use the remove() method to work with a value that's being removed from a list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
print(f"\nA {too_expensive.title()} is too expensive for me.") # A Ducati is too expensive for me.

# - The remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to determine if all occurrences of the value have been removed.
