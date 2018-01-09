# # Exercise 9-1 Restaurant
# class Restaurant() :
# 	def __init__ (self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
	
# 	def describe_restaurant(self):
# 		print("The "+self.restaurant_name.title()+" is lovely place, nice and quiet."+
# 			" Great "+self.cuisine_type.capitalize()+" food and friendly staff !")

# 	def open_restaurant(self):
# 		print(self.restaurant_name.title()+" is open\n")
	
# indian_restaurant = Restaurant('Taj Mahal','indian')

# print(indian_restaurant.restaurant_name.upper())
# print(indian_restaurant.cuisine_type.upper())

# # Exercise 9-2 Restaurant
# class Restaurant() :
# 	def __init__ (self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
	
# 	def describe_restaurant(self):
# 		print("The "+self.restaurant_name.title()+" is lovely, nice and quiet"+
# 			".\n" + " Great "+self.cuisine_type.capitalize() + " food and" + 
# 			"friendly staff !\n")

# 	def open_restaurant(self):
# 		print(self.restaurant_name.title()+" is open\n")
	
# indian_restaurant = Restaurant('Taj Mahal','indian')
# japanese_restaurant = Restaurant('Hoshi sushi', 'japanese')
# algerian_restaurant = Restaurant('Djenina', 'algerian')

# indian_restaurant.describe_restaurant()
# japanese_restaurant.describe_restaurant()
# algerian_restaurant.describe_restaurant()

# Exercise 9-3 Users
class Users():
	def __init__ (self, first_name, last_name, age, height):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.height = height

	def describe_user(self):
		print ("+ Last Name :\t " + self.last_name.title())
		print ("+ Age : \t" + self.age.title())
		print ("+ Height : \t" + self.height.title()+"\n")

	def greet_user(self):
		print("Hello "+self.first_name.title())

user_bob = Users('bob','dobalina', age='24', height="6'3")
user_max = Users('max','mad', age='36', height="5'11")
user_karen = Users('karen','mills', age='26', height="5'8")
user_stacey = Users('stacey','chapman', age='54', height="6'3")

user_bob.greet_user()
user_bob.describe_user()

user_max.greet_user()
user_max.describe_user()

user_karen.greet_user()
user_karen.describe_user()

user_stacey.greet_user()
user_stacey.describe_user()