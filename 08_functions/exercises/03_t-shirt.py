# Exercise 3:

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"\nThe size of the shirt is {size.upper()} and the message printed on it is: {message.title()}.")

make_shirt('m', 'hello, world!')
make_shirt(size='l', message='hello, python!')
