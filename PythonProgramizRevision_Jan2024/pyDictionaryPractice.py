# creating a dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}

# printing the dictionary
print(country_capitals)  # {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'}

# access the value of keys
print(country_capitals["Germany"])  # Output: Berlin
print(country_capitals["England"])  # Output: London

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"
print(country_capitals)  # {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London', 'Italy': 'Rome'}

# delete item having "Germany" key
del country_capitals["Germany"]
print(country_capitals)  # {'Canada': 'Ottawa', 'England': 'London', 'Italy': 'Rome'}

# clear the dictionary
# country_capitals.clear()
print(country_capitals)  # {}

# change the value of "Italy" key to "Rome"
country_capitals["Canada"] = "Toronto"
print(country_capitals) # {'Canada': 'Toronto', 'England': 'London', 'Italy': 'Rome'}

for country in country_capitals:
    print(country)

print()
for capital in country_capitals.values():
    print(capital)

print()
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

