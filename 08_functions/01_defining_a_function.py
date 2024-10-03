# Defining a Function
# -------------------

# - Functions are named blocks of code designed to do one specific job.
# - When you want to perform a particular task that you've defined in a function, you call the function responsible for it.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Output:
# Hello!

# - The def keyword is the function definition, which tells Python the name of the function, and what kind of information the function needs to do its job. The parentheses hold that information.
# - Any indented lines that follow def greet_user(): make up the body of the function.
# - The text in triple quotes is a comment called a docstring, which describes what the function does. Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.

# - When you want to use this function, you call it. A function call tells Python to execute the code in the function. To call a function, you write the name of the function followed by any necessary information in parentheses.

# - Passing Information to a Function
# -----------------------------------

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# Output:
# Hello, Jesse!

# - Arguments and Parameters
# --------------------------

# - A parameter is a piece of information the function needs to do its job.
# - An argument is a piece of information that is passed from a function call to a function.
