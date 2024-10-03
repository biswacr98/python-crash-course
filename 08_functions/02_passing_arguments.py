# Passing Arguments
# -----------------

# - Because a function definition can have multiple parameters, a function call may need multiple arguments.
# - You can use positional arguments, which need to be in the same order the parameters were written.
# - You can use keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.

# - Positional Arguments
# -----------------------

# - When you call a function, Python must match each argument in the function call with a parameter in the function definition.
# - The simplest way to do this is based on the order of the arguments provided.
# - Values matched up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Output:
# I have a hamster.
# My hamster's name is Harry.

# -- Multiple Function Calls
# ---------------------------

# - You can call a function as many times as needed.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Output:
# I have a hamster.
# My hamster's name is Harry.
#
# I have a dog.
# My dog's name is Willie.

# -- Order Matters in Positional Arguments
# -----------------------------------------

# - You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster') # The order of the arguments is wrong.

# Output:
# I have a harry.
# My harry's name is Hamster.

# - Keyword Arguments
# --------------------

# - A keyword argument is a name-value pair that you pass to a function.
# - Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# Output:
# I have a hamster.
# My hamster's name is Harry.

# - When you use keyword arguments, be sure to use the exact names of the parameters in the function's definition.

# -- Default Values
# ------------------

# - When writing a function, you can define a default value for each parameter.
# - If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter's default value.
# - So when you define a default value for a parameter, you can exclude the corresponding argument you'd usually write in the function call.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# Output:
# I have a dog.
# My dog's name is Willie.

# - Note that the order of the parameters in the function definition had to be changed. Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet's name.

# - When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.

# -- Equivalent Function Calls
# ----------------------------

# - Because positional arguments, keyword arguments, and default values can all be used together, often you'll have several equivalent ways to call a function.

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# -- Avoiding Argument Errors
# ---------------------------

# - Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet() # This will cause an error because the function call is missing the required arguments

# Output:
# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
