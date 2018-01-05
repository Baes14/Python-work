# # Exercise 6.1 Person
# my_friend = {
# 	'first_name':'barack',
# 	'last_name':'obama',
# 	'city':'washington d.c',
# 	'height':"6'4\"",
# 	}
# print(my_friend['first_name'].title()+" "+my_friend['last_name'].title()+"\n\n")

# # Exercise 6.2 Favorite Numbers
# favorite_numbers = {
# 	'ralph':3,
# 	'becky':6,
# 	'rob':7,
# 	'monica':9,
# 	'sarah':5,
# }

# for friend,fav_num in favorite_numbers.items():
# 	print(friend.title()+"'s favorite number is "+str(fav_num))

# # Exercise 6.3 Glossary

# glossary = {
# 	'indentation':'white space left at the begining of the line before'+ 
# 	' the first character. Indentations are typically used to provide '+
# 	'more readibility to text',
# 	'looping':'looping is a programing term defining the function of applying '+
# 	'certain lines of code to a set of values contained in a list, dictionnary etc...',
# 	'method':'a method is a function incorporated within python that can be applied to '+
# 	'several objects. Just like functions they can take other parameters and return a value',
# }

# for word,definition in glossary.items():
# 	print("\n"+word.title()+" : "+definition.capitalize())

# # Exercise 6.5 Rivers
# rivers={
# 	'nile':'egypt',
# 	'missisipi':'the united states',
# 	'seine':'france',
# }

# for river,country in rivers.items():
# 	print("\nThe "+river.title()+" river runs through "+country.title())

# print("\n")
# for river in rivers:
# 	print(river.title())

# print("\n")
# for country in rivers.values():
# 	print(country.title())

# Exercise 6.7 People
# friend_0 = {
# 	'first_name':'barack',
# 	'last_name':'obama',
# 	'city':'washington d.c',
# 	'height':"6'4\"",
# 	}

# friend_1 = {
# 	'first_name':'LeBron',
# 	'last_name':'james',
# 	'city':'cleveland',
# 	'height':"6'8\"",
# 	}

# friend_2 = {
# 	'first_name':'Marcus',
# 	'last_name':'Aurelius',
# 	'city':'Rome',
# 	'height':"5'11\"",
# 	}

# people = [friend_0, friend_1, friend_2]

# for friend in people:
# 	print("\n")
# 	for friend_info,value in friend.items():
# 		print(friend_info.title()+" : "+value.title())

# Exercise 6.10 Favorite Numbers
# favorite_numbers = {
# 	'ralph':[3,11,22],
# 	'becky':[6,4,1],
# 	'rob':[7],
# 	'monica':[9,2,8],
# 	'sarah':[5],
# }

# for friend,fav_num in favorite_numbers.items():
# 	if(len(fav_num)>1):
# 		print("\n"+friend.title()+"'s favorite numbers are :")
# 		for num in fav_num:
# 			print("\t --> "+str(num))
# 	else:
# 		print("\n"+friend.title()+" favorite number is :\t"+str(fav_num))

# Exercise 6.11 Cities
cities = {
	'algiers':{
	'country':'algeria',
	'population':'4,000,000',
	'fact':'City was built by the Romans in the 18th century'
	},
	'new york':{
	'country':'the united states',
	'population':'15,000,000',
	'fact':'Manhattan island was sold for 25$ by the native american'
	},
	'paris':{
	'country':'France',
	'population':'8,000,000',
	'fact':'Paris has about 50 Million visitors each year on cultural trips'
	},
}

for city,description in cities.items():
	print("\n"+city.title()+" :")
	for info,value in description.items():
		print("\t- "+info.title()+" : "+value.title())
