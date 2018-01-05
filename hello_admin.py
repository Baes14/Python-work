# usernames=["karl", "admin", "operator", "maintenance", "sales"]
# if usernames:
# 	for username in usernames:
# 		if username=='admin':
# 			print("Hello admin, would like to see a status report?")
# 		else:
# 			print("Hello "+username+", thank you for logging in again.")
# else:
# 	print("There are no usernames in your list!")

current_users=["mark", "claude", "mike", "Irure", "excepteur"]
new_users=["Velit", "utanim", "Mark", "chris", "bob"]
for user in new_users:
	if user.lower() in current_users:
		print ("\nName already in use, please choose another :\n")
	else:
		print("username is available")