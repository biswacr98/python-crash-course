# Exercise 8:

# Think of at least five places in the world you'd like to visit.
# -  Store the locations in a list. Make sure the list is not in alphabetical order.
# -  Print your list in its original order. Don't worry about printing the list neatly, just print it as a raw Python list.
# -  Use sorted() to print your list in alphabetical order without modifying the actual list.
# -  Show that your list is still in its original order by printing it.
# -  Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# -  Show that your list is still in its original order by printing it again.
# -  Use reverse() to change the order of your list. Print the list to show that its order has changed.
# -  Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
# -  Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
# -  Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has changed.

places = ["Paris", "New York", "London", "Tokyo", "Sydney"]
print(places) # ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']

print(sorted(places)) # ['London', 'New York', 'Paris', 'Sydney', 'Tokyo']

print(places) # ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']

print(sorted(places, reverse=True)) # ['Tokyo', 'Sydney', 'Paris', 'New York', 'London']

print(places) # ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']

places.reverse() # ['Sydney', 'Tokyo', 'London', 'New York', 'Paris']
print(places)  # ['Sydney', 'Tokyo', 'London', 'New York', 'Paris']

places.reverse() # ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']
print(places) # ['Paris', 'New York', 'London', 'Tokyo', 'Sydney']

places.sort() # ['London', 'New York', 'Paris', 'Sydney', 'Tokyo']
print(places) # ['London', 'New York', 'Paris', 'Sydney', 'Tokyo']

places.sort(reverse=True) # ['Tokyo', 'Sydney', 'Paris', 'New York', 'London']
print(places) # ['Tokyo', 'Sydney', 'Paris', 'New York', 'London']
