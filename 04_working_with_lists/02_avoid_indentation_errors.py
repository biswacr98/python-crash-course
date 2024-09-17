# Avoiding Indentation Errors
# ----------------------------
# - Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.
# - In longer Python programs, you'll notice blocks of code indented at a few different levels. These indentation levels help you gain a general sense of the overall program's organization.
# - For Indentation Errors there are two common patterns:
#       - Indent lines that don't need to be indented.
#       - Forget to indent lines that need to be indented.

# Forgetting to Indent
# ---------------------

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician)

# Indentation Error: expected an indented block after 'for' statement
# - Resolve this kind of indentation error by indenting the line or lines immediately after the for statement.

# Forgetting to Indent Additional Lines
# --------------------------------------
# - Sometimes your loop will run without any errors, but it won't produce the expected result.
# - This can happen when you forget to indent additional lines that are supposed to be inside the loop.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# - This is a logical error. The syntzx is valid in Python but the code does not produce the desired output because a problem occurs in its logic.


# Indenting Unnecessarily
# ------------------------
# - If you accidentally indent a line that doesn't need to be indented, Python informs you about the unexpected indent.

message = "Hello Python world!"
    #print(message) # IndentationError: unexpected indent


# Indenting Unnecessarily After the Loop
# ---------------------------------------
# - If you accidentally indent code that should run after a loop is finished, that code will be repeated once for each item in the list.
# - Sometimes this prompts Python to report an error, but often your program will still run without generating any errors.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!") # This line is indented unnecessarily

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.

# Thank you, everyone. That was a great magic show!
# David, that was a great trick!
# I can't wait to see your next trick, David.

# Thank you, everyone. That was a great magic show!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# Thank you, everyone. That was a great magic show!

# - If an action is repeated many times when it should be executed only once, check to see if a block of code is unnecessarily indented.

# Forgetting the Colon
# ---------------------
# - The colon at the end of a for statement tells Python to interpret the next line or lines as the start of a loop.

magicians = ['alice', 'david', 'carolina']
#for magician in magicians # SyntaxError: expected ':'
    #print(magician)

# - If you accidentally omit the colon, you'll get a syntax error because Python doesn't know what you're trying to do.
