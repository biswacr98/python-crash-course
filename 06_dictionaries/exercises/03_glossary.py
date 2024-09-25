# Exercise 3:

# A python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
# - Think of five programming terms you've learned about in the previous chapters. Use these terms as the keys in your glossary, and store their meanings as values.
# - Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'A collection in which each item must be unique.',
    'variable': 'A placeholder for a value.'
}

print(f"List: {glossary['list']}")
print(f"Tuple: {glossary['tuple']}")
print(f"Dictionary: {glossary['dictionary']}")
print(f"Set: {glossary['set']}")
print(f"Variable: {glossary['variable']}")

# Output:
# List: A collection of items in a particular order.
# Tuple: An immutable list.
# Dictionary: A collection of key-value pairs.
# Set: A collection in which each item must be unique.
# Variable: A placeholder for a value
