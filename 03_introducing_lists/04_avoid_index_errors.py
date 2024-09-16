# Avoiding Indexing Errors When Working with Lists
# ---------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) # IndexError: list index out of range

# The error message "IndexError: list index out of range" is Python's way of telling you that you tried to access an element from a list using an index that doesn't exist. In this case, the error occurred because the list motorcycles has only three elements, which means it has indexes 0, 1, and 2. When you request the item at index 3, Python can't find it, so it raises an IndexError.

# - Because of the off-by-one nature of indexing in lists, this error is typical.

# - An index error means Pythom can't find an item at the index you requested.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # suzuki

# - The index -1 always returns the last item in a list.
# - The only time this approach will cause an error is when the list you're trying to access is empty.

# motorcycles = []
# print(motorcycles[-1]) # IndexError: list index out of range
