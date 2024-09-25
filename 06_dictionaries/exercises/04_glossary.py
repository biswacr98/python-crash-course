# Exercise 4:

# Now that you know how to loop through a dictionary, clean up the code from 03_glossary.py by replacing the series of print statements with a loop that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'A collection in which each item must be unique.',
    'variable': 'A placeholder for a value.'
}

for term, meaning in glossary.items():
    print(f"\n{term.title()}: {meaning}")

glossary['loop'] = 'A structure that allows you to repeat a block of code.'
glossary['function'] = 'A named block of code that performs a specific task.'
glossary['class'] = 'A blueprint for creating objects.'
glossary['module'] = 'A file containing Python code.'
glossary['package'] = 'A collection of modules.'

for term, meaning in glossary.items():
    print(f"\n{term.title()}: {meaning}")
