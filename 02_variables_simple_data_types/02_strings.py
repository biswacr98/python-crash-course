# Strings
# ---------
# - A string is a series of characters.
# - Anything inside quotes is considered a string in Python. You can use single or double quotes around your strings.

message = "This is a string."
message = 'This is also a string.'

# - Use quotes or apostrophes within your strings
paragraph_1 = 'I told my friend, "Python is my favorite language!"'
paragraph_2 = "The language 'Python' is named after Monty Python, not the snake."
paragraph_3 = "One of Python's strengths is its diverse and supportive community."

print(paragraph_1) # I told my friend, "Python is my favorite language!"
print(paragraph_2) # The language 'Python' is named after Monty Python, not the snake.
print(paragraph_3) # One of Python's strengths is its diverse and supportive community.

# Changing Case in a String with Methods
# ---------------------------------------

name = "ada lovelace"
print(name.title()) # Ada Lovelace (title() method uses Title Case, where each word begins with a capital letter)

# - A method is an action that Python can perform on a piece of data.
# - The dot (.) after name in name.title() tells Python to make the title() method act on the variable name.
# - Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses.

name = "Ada Lovelace"
print(name.upper()) # ADA LOVELACE (upper() method uses all uppercase letters)
print(name.lower()) # ada lovelace (lower() method uses all lowercase letters)

# Using Variables in Strings
# ---------------------------
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f-string is a formatted string literal. The f is for format, which tells Python to replace the variable name with its value.
print(full_name) # ada lovelace

# - Use f-strings to compose complete messages using the information associated with a variable.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") # Hello, Ada Lovelace!

# - You can also use f-strings to compose messages, and then assign those messages to a variable.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message) # Hello, Ada Lovelace!

# Adding Whitespace to Strings with Tabs or Newlines
# --------------------------------------------------
# - Whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols.
# - Use whitespace to organize your output so it's easier for users to read.

# - To add a tab to your text, use the character combination \t.
print("Python") # Python
print("\tPython") #     Python

# - To add a newline in a string, use the character combination \n.
print("Languages:\nPython\nC\nJavaScript") # Languages:
                                            # Python
                                            # C
                                            # JavaScript

# - You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab.

print("Languages:\n\tPython\n\tC\n\tJavaScript") # Languages:
                                                    #     Python
                                                    #     C
                                                    #     JavaScript

# Stripping Whitespace
# ---------------------

# - Extra whitespace can be confusing in your programs.
# - Python detects extra whitespace and considers it significant unless you tell it otherwise.
# - Python can look for extra whitespace on the right and left sides of a string.

# - To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
favorite_language = 'python '
print(favorite_language) # python<space>
print(favorite_language.rstrip()) # python
print(favorite_language) # python<space> (rstrip() method doesn't change the value of the variable permanently)
# - To remove the whitespace from the variable permanently, you have to associate the stripped value with the variable name.
favorite_language = favorite_language.rstrip()
print(favorite_language) # python

# - To ensure that no whitespace exists at the left end of a string, use the lstrip() method.
favorite_language = ' python'
print(favorite_language) # <space>python
print(favorite_language.lstrip()) # python

# - To ensure that no whitespace exists at either end of a string, use the strip() method.
favorite_language = ' python '
print(favorite_language) # <space>python<space>
print(favorite_language.strip()) # python

# - The methods rstrip(), lstrip(), and strip() are particularly useful when receiving input from people.

# Removing Prefixes
# ------------------
# - Consider a URL with common prefixes such as http://, https://.
# - We want to remove these prefixes from the URL so we can focus on the main part of the address.
# - Python 3.9 introduced the removeprefix() method to remove prefixes from strings.
# - This method is useful when working with URLs, file paths, and other strings that have a common prefix.
# - Like the rstrip(), lstrip(), and strip() methods, removeprefix() doesn't change the value of the variable permanently. It leaves the original string unchanged.
# - To remove the prefix from the variable permanently, you have to associate the stripped value with the variable name.

google_url = "https://www.google.com"
print(google_url) # https://www.google.com
google_url_prefixed = google_url.removeprefix("https://") # www.google.com
print(google_url_prefixed)

# Avoiding Syntax Errors with Strings
# -------------------------------------
# - Syntax errors occur when Python doesn't recognize a section of your program as valid Python code.
# - For example, if you use an apostrophe within single quotes, Python will get confused because it won't know where the string should end.
# - Python interprets everything between the first single quote and the apostrophe as a string. It then tries to interpret the rest of the text as Python code, which leads to a syntax error.

message = "One of Python's strengths is its diverse and supportive community."
print(message) # One of Python's strengths is its diverse and supportive community.

# - If you use double quotes to define the string, Python will be able to interpret the apostrophe correctly.

# - If you use single quotes to define the string, Python will get confused because it will think the string ends after Python.
# message = 'One of Python's strengths is its diverse and supportive community.'
# print(message) # SyntaxError: unterminated string literal

message = 'One of Python\'s strengths is its diverse and supportive community.'
# Use the backslash (\) to escape the apostrophe. This tells Python to ignore the apostrophe and continue reading the string.
print(message) # One of Python's strengths is its diverse and supportive community.
