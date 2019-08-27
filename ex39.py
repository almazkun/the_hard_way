# Abbr to contry
countries = {
    "Russia": "RU",
    "Germany": "DE",
    "Uzbekistan": "UZ",
    "Zimbabwe": "ZW",
    "Turkey": "TR",
}


# Some Citis of Countries
cities = {
    "UZ": "Zaravshan",
    "TR": "Antalya",
    "DE": "Minhen",
}


# Adding some cities
cities["ZW"] = "Gveru"
cities["RU"] = "Moskow"


# Print some cities
print("-_- " * 10)
print("There is a city {} in ZW".format(cities["ZW"]))
print("There is a city {} in RU".format(cities["RU"]))


# Print some countries
print("-_- " * 10)
print("Abbraviation for Turkey: {}".format(countries["Turkey"]))
print("Abbraviation for Germany: {}".format(countries["Germany"]))


# Print cities in counties
print("-_- " * 10)
print("There is a city {} in Turkey".format(cities[countries["Turkey"]]))
print("There is a city {} in RU".format(cities[countries["Russia"]]))


# List all abbreviations
print("-_- " * 10)
for country, abbr in countries.items():
    print("{} for {}".format(country, abbr))


# List of all cities
print("-_- " * 10)
for abbr, city in cities.items():
    print("In {} is {}.".format(abbr, city))


# Now both 
print("-_- " * 10)
for country, abbr in countries.items():
    print("Country {} has an abbr {} and city {}.".format(country, abbr, cities[abbr]))


print("-_- " * 10)
# Safe method to get an abbr
#country - countries.get("US", None)


if not country:
    print("US is absent today.")


# Printing  city with argument by default
city = cities.get("US", "do not exist")
print("In US is a city {}.".format(city))




