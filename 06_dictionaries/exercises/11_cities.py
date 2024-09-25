# Exercise 11:

# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'new york': {
        'country': 'usa',
        'population': 8_623_000,
        'fact': 'New York City is the largest city in the United States.'
    },
    'london': {
        'country': 'england',
        'population': 8_982_000,
        'fact': 'London is the capital of England.'
    },
    'tokyo': {
        'country': 'japan',
        'population': 9_273_000,
        'fact': 'Tokyo is the capital of Japan.'
    }
}

for city, city_info in cities.items():
    print(f"{city.title()}:")
    for key, value in city_info.items():
        print(f"\t{key.title()}: {value}")
    print()

