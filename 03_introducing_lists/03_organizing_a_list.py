# Organizing a List
#-------------------
# - If you want to preserve the original order of your list or you'll want to change the original order, you can organize the list.

# Sorting a List Permanently with the sort() Method
# --------------------------------------------------
# - The sort() method changes the order of the list permanently.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']

# - You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

# Sorting a List Temporarily with the sorted() Function
# ------------------------------------------------------
# - To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
# - The sorted() function lets you display your list in a particular order but doesn't affect the actual order of the list.

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the sorted list:")
print(sorted(cars)) # ['audi', 'bmw', 'subaru', 'toyota']

print("\nHere is the original list again:")
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']

# - The sorted() function can also accept the reverse=True argument if you want to display a list in reverse alphabetical order.

# Printing a List in Reverse Order
# ---------------------------------
# - To reverse the original order of a list, you can use the reverse() method.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars) # ['subaru', 'toyota', 'audi', 'bmw']

# - The reverse() doesn't sort the list in reverse alphabetical order; it simply reverses the order of the list.
# - The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.

# Finding the Length of a List
# -----------------------------
# - You can quickly find the length of a list by using the len() function.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # 4

# - Python counts the items in a list starting with one, so you shouldn't run into any off-by-one errors when determining the length of a list.
