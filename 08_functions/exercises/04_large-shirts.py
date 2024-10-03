# Exercise 4:

# Modify the make_shirt() function so that shirts are large by default with a message that reads "I love Python." Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='l', message='I love Python.'):
    print(f"\nThe size of the shirt is {size.upper()} and the message printed on it is: {message.title()}.")

make_shirt()
make_shirt('m')
make_shirt('s', 'hello, python!')
