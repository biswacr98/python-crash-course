# Exercise 1:
# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs car == 'SUBARU'? I predict False.")
print(car == 'SUBARU')

print("\nIs car == 'mercedes'? I predict False.")
print(car == 'subaru')

print("\nIs car == 'SuBaRu'? I predict True.")
print(car.lower() == 'subaru')
