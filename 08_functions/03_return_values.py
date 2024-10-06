# Return Values
# ---------------

# - A function doesn’t always have to display its output directly.
# - Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value.
# - The return statement takes a value from inside a function and sends it back to the line that called the function.

# - Returning a Simple Value
# ---------------------------

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Output:
# Jimi Hendrix

# - Making an Argument Optional
# ------------------------------

# - Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Output:
# Jimi Hendrix
# John Lee Hooker

# - Returning a Dictionary
# -------------------------

# - A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Output:
# {'first': 'jimi', 'last': 'hendrix'}

# - Extending the build_person() function to accept optional values like age.

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

# Output:
# {'first': 'jimi', 'last': 'hendrix', 'age': 27}

# - None is a special value whih=ch is used when a variable has no specific value assigned to it.
# - None is a placeholder value.
# - In conditional tests, None evaluates to False.

# - Using a Function with a while Loop
# -------------------------------------

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# Output:
# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: jimi
# Last name: hendrix

# Hello, Jimi Hendrix!

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: q

