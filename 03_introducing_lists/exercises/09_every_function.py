# Exercise 9:
# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter 03_introducing_lists at least once.

# I'll create a list of countries and use each function introduced in this chapter at least once.

countries = ["Australia", "Brazil", "Canada", "Denmark", "Egypt"]
print(countries) # ['Australia', 'Brazil', 'Canada', 'Denmark', 'Egypt']

print(sorted(countries)) # ['Australia', 'Brazil', 'Canada', 'Denmark', 'Egypt']
print(countries) # ['Australia', 'Brazil', 'Canada', 'Denmark', 'Egypt']

print(sorted(countries, reverse=True)) # ['Egypt', 'Denmark', 'Canada', 'Brazil', 'Australia']
print(countries) # ['Australia', 'Brazil', 'Canada', 'Denmark', 'Egypt']

countries.reverse()
print(countries) # ['Egypt', 'Denmark', 'Canada', 'Brazil', 'Australia']

countries.reverse()
print(countries) # ['Australia', 'Brazil', 'Canada', 'Denmark', 'Egypt']

countries.sort()
print(countries) # ['Australia', 'Brazil', 'Canada', 'Denmark', 'Egypt']

countries.sort(reverse=True)
print(countries) # ['Egypt', 'Denmark', 'Canada', 'Brazil', 'Australia']

print(len(countries)) # 5
