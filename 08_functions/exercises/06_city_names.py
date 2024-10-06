# Exercise 6:

# Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('london', 'england'))
print(city_country('new york', 'usa'))

# Output:
# Santiago, Chile
# Paris, France
# London, England
# New York, Usa
