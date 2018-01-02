cities=["Dakar", "Algiers", "New York", "London", "Paris"]

print("\nThis is the ORIGINAL list: ")
print(cities)

# Temp sorting code
print("\nList SORTING TEMPORARILY: ")
print(sorted(cities))


print("\nPrinting list in REVERSE ORDER TEMPORARILY")
print(sorted(cities,reverse=True))

print ("\nFinding the LENGHT of the list is:")
print(len(cities))

# Code for permanent sort
print("\n")
print(cities)
cities.reverse()
print("\nPrinting list in REVERSE ORDER PERMANENTLY")
print(cities)

# Permnament Alphabetical sort
cities.sort()
print("\nThis is how you SORT the list PERMANENTLY")
print(cities)
