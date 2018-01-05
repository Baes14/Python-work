#From the top
cubes=[cube**3 for cube in range(1,11)]
print(cubes)
print("\nThe first three items from the list are :")
for cube in cubes[0:3]:
	print("\t--> "+str(cube))

# From the middle
middle=int(len(cubes)/2)
print("\nThree items from the middle of the list are :")
for cube in cubes[middle:middle+3]:
	print("\t--> "+str(cube))

# Last 3 items
print("\nThe last 3 items from the list  are:")
for cube in cubes[-3:]:
	print("\t--> "+str(cube))