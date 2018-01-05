favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

candidates = ['phil', 'kathy','john','mary','sarah']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

for candidate in candidates:
	if candidate in favorite_languages:
		print("\nThank you "+candidate.title()+" for taking the poll.")
	else:
		print("\n** "+candidate.title()+" would you please take the poll !")