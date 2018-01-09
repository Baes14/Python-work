# # Exercise 7-1 Rental car
# car = input("What type of car would you like ? ")
# print("Let me see if I can find you a "+car.title())

# # Exercise 7-2 REstaurant seating
# group = input("Good evening! How many people are in your dinner group ? ")
# group=int(group)
# if group > 8:
# 	print ("Please wait a moment while we prepare a table")
# else:
# 	print ("Your table is ready!")

# # Exercise 7-2 Restaurant seating
# number = input("Give me a number :")
# number=int(number)
# if number % 10 == 0 :
# 	print("This number is a multiple of 10")
# else:
# 	print("This number is NOT a multiple of 10")

# # Exercise 7-4 Pizza Toppings
# active = True
# print("Type 'quit' to exit Program")
# while active:
# 	toppings = input("Please enter your toppings: ")
# 	if toppings == 'quit':
# 		active = False
# 	else:
# 		print("We will add "+toppings+" to your pizza")

# # Exercise 7-5 Movie tickets
# print("Type 'quit' to exit Program")

# while True :
# 	age = input("How old are you ?")
# 	if age == 'quit':
# 		break
# 	age = int(age)
# 	if age < 3 :
# 		print ("Your ticket is FREE")

# 	elif age >= 3 and age <= 12 :
# 		print ("Your ticket costs 10$")

# 	elif age >12 :
# 		print ("Your ticket costs 15$")

# # Excercise 7-8 Deli and 7-9 No Pastrami
# sandwich_orders = [
# 'pastrami', 'philly cheese steak', 'pastrami', 'meatball', 'Club', 
# 'Tuna Fish','Ham & cheese', 'pastrami',
# 	]

# print("\n The Deli has run out of pastrami\n")
# while 'pastrami' in sandwich_orders:
# 	sandwich_orders.remove('pastrami')

# finished_sandwiches = []

# while sandwich_orders :
# 	current_sandwich = sandwich_orders.pop()
# 	print("I made your "+current_sandwich+" sandwich")
# 	finished_sandwiches.append(current_sandwich) 

# print("\nHere are all the sandwiches that've been made :")
# for sandwich in finished_sandwiches:
# 	print("\t\t\t\t\t\t + "+sandwich)

# Exercise 7-10 Dream vacation

responses = []
polling_active = True

while polling_active :
	response = input("If you could visit one place in the world,"+
	 "where would you go ? ")
	responses.append(response)
	repeat = input("Next Person? (yes/no)")
	if repeat == 'no':
		polling_active = False
print("\n --------------------"+"\n Polling results"+"\n --------------------")
for result in responses:
	print(" \t\t\t + "+result)



