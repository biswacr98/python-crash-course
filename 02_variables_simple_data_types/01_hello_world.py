# Running a python file
# - .py indicates it's a Python file.
# - VS Code runs the file through the Python interpreter.
# - The Python interpreter reads through the program and determines what each word means.
#    - print is a function that displays a message on the screen.
#    - "Hello Python world!" is a string, which is a series of characters.

# Syntax Highlighting
# - Python code is color-coded to make it easier to read.

# Variables
# - Every variable is connected to a value, which is the information associated with that variable.
# - Python Interpreter first associates the variable with the value.


message = "Hello Python world!" # This is a variable.
print(message)

message = "Hello Python Crash Course world!" # Change the value of the variable in your program at any time.
print(message)

# Naming and Using Variables
# - Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. message_1 > 1_message.
# - Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. greeting_message > greeting message.
# - Avoid using Python keywords and function names as variable names.
# - Variable names should be short and descriptive.
#       - name > n
#       - student_name > s_n
#       - name_length > length_of_persons_name
# - Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.
# - Python is case-sensitive. This means that the variable name message is different from Message.
# - Avoid starting variable names with a capital letter. Class names should be capitalized.

# Name Errors Using Variables

# message = "Hello Python Crash Course reader!"
# print(mesage) # NameError: name 'mesage' is not defined

# - Python Interpreter provides a traceback, which is a record of where the interpreter ran into trouble when trying to execute your code.
# - NameError: name 'mesage' is not defined. Did you mean: 'message'?
# - The error message tells you that Python doesn't recognize the name mesage. It suggests that you might have meant message instead.
# - A name error usually means we either forgot to set a variable's value before using it, or we made a typo in the variable's name.
