# Exercise 5:

# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# - Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# - Use a loop to print the name of each river included in the dictionary.
# - Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# Output:
# The Nile runs through Egypt.
# The Amazon runs through Brazil.
# The Yangtze runs through China.

# Nile
# Amazon
# Yangtze

# Egypt
# Brazil
# China
