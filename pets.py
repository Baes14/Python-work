rex = {'dog':'mark'}
jack = {'parrot':'johnny'}
felix = {'cat':'marco'}
bugs= {'rabbit':'elmer'}

pets = [rex, jack, felix, bugs]

for pet in pets:
	print("\n")
	for kind,owner in pet.items():
		print("There's a "+kind+" that belongs to "+owner.title())

favorite_places = {
	'jessica':'paris',
	'Moussa':'rome',
	'Caroline':'berlin',
	'Salima':'istanbul',
}
print("\n")
for name,place in favorite_places.items():
	print (name.title()+" favorite place is "+place.title())