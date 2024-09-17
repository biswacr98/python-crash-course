# Looping through an Entire List
# -------------------------------
# - When you want to do the same operation with every item in a list, you can use Python's for loop.

magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(magician)

# - For each magician in the list of magicians, we are printing the magician's name.

# A closer look at Looping
# ------------------------
# - Looping is important because it is one of the most common ways a computer automates repetitive tasks.

# - In this example, we are telling Python to retrieve the first value from the list magicians and associate it with the variable magician.
# - Python prints the current value of magician and then moves to the next value in the list.

# - Python repeats the entire loop once for each magician in the list.

# Doing More Work within a for Loop
# -----------------------------------

magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# - Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.

magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing Something After a for Loop
# ----------------------------------
# - We'd want to summarize a block of output or move on to other work that our program must accomplish.

magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# - The last print statement is not indented, so it is not part of the loop.


