# # Exercise 8-1 Message
# def display_message():
# 	print("I'm reading Chapter 8 about Python Functions")
# display_message()

# # Exercise 8-2 Favorite Book
# def favorite_book(title):
# 	print("One of my favorite books is "+title.title())
# favorite_book('Meditations')

# # Excercise 8-3 T-Shirt
# def make_shirt(size, message):
# 	print("Your T-Shirt size "+size.capitalize()+" with the message '"+message+"' is ready!")
# make_shirt('XL', 'Kawa Bunga!!!')
# make_shirt(message='Beauty Queen', size='XS')

# # Excercise 8-4 Large Shirts
# def make_shirt(size='large', message='I love Python'):
# 	print("Your T-Shirt size "+size.upper()+" with the message '"+message+"' is ready!")
# make_shirt()
# make_shirt('medium')
# make_shirt('XXXL', 'Hoopa Gangman style')

# # Excercise 8-5 Cities
# def describe_city(city, country='Algeria'):
# 	print(city.capitalize()+" is in "+country.capitalize())
# describe_city('Casablanca')
# describe_city('Algiers')
# describe_city('New York', 'The USA')

# # Exercise 8-6 City Names
# def city_country(city, country):
# 	"""This Function separates city and country with a comma"""
# 	city_comma_country = "______________________________________\n"+city.title()+", "+country.title()+"\n______________________________________"
# 	return city_comma_country

# place = city_country('Las Vegas', 'arizona')
# print(place)

# place = city_country('paris', 'france')
# print(place)

# place = city_country('pekin', 'china')
# print(place)

# # Exercise 8-7 Album
# def make_album(artist, album, tracks=''):
# 	record ={'artist_name':artist, 'album_name':album, 'track':tracks}
# 	return record

# title = make_album('Dr Dre', 'The Chronic')
# print(title)

# title = make_album('Ed Sheeran', 'Shape of you','25')
# print(title)

# title = make_album('Jay Z', '4:44','14')
# print(title)

# # Exercise 8-8 User Albums
# def make_album(user, artist, album):
# 	record ={'artist_name':artist, 'album_name':album, 'user_name':user}
# 	return record

# print("Enter 'q' to quit or Ctrl+C")
# user_name = input("What's your name ? ")

# while user_name != 'q' :
# 	user_artist = input("Hi "+user_name.title()+", please enter the artist name :")
# 	user_album = input("Please enter "+user_artist.title()+"'s album name : ")
# 	user_record = make_album(user_name, user_artist, user_album)
# 	print(user_record)
# 	break

# # Exercise 8-9 Magicians
# magicians = ['Houdini', 'Cadabra', 'Kamel', 'Waldorf',]

# def show_magicians(magician_names):
# 	for magician in magician_names:
# 		print ("+ "+magician.title())

# show_magicians(magicians)

# # Exercise 8-10 Great Magicians
# magicians = ['Houdini', 'Cadabra', 'Kamel', 'Waldorf',]

# def show_magicians(magician_names):
# 	for magician in magician_names:
# 		print ("+ "+magician.title())

# def make_great(magician_names):
# 	i=0
# 	for magician in magician_names:
# 		magician_names[i]="The Great "+magician
# 		i+=1

# make_great(magicians)
# show_magicians(magicians)

# # Exercise 8-11 Unchanged Magicians
# magicians = ['Houdini', 'Cadabra', 'Kamel', 'Waldorf',]

# def show_magicians(magician_names):
# 	for magician in magician_names:
# 		print ("+ "+magician.title())

# def make_great(magician_names):
# 	i=0
# 	for magician in magician_names:
# 		magician_names[i]="The Great "+magician
# 		print("- "+magician_names[i])
# 		i+=1


# make_great(magicians[:])
# show_magicians(magicians)

# # Exercise 8-12 Sandwiches
# def make_sandwich(*elements):
# 	print ("\nYour sandwich will have the following :")
# 	for element in elements:
# 		print("\t\t\t +"+element.title())

# make_sandwich('cheese','chiken','tomato','olives')
# make_sandwich('Corn','fish')
# make_sandwich('Beef','Tuna','chick peas')

# Exercise 8-14 Cars
def make_car(brand, model, **optional):
	car = {}
	car['brand_name'] = brand
	car['model_name'] = model
	for key,value in optional.items():
		car[key] = value

	return car
car = make_car('Hyundai', 'Santa Fe', color='black', gps=True)
print (car)

