pizzas=["4 season", "Spicy hot one", "Meat lovers", "Mexican", "Seafood"]
for pizza in pizzas:
	print("I love the "+pizza+" pizza !")
print("\nI'm a huge pizza fan!")

friend_pizzas=pizzas[:]
friend_pizzas.append('Pepperoni')

print("My favorite pizzas are :")
for pizza in pizzas:
	print("\t + "+pizza)

print("\nMy Friend's favorite pizzas are :")
for pizza in friend_pizzas:
	print("\t - "+pizza)