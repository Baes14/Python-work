guests=["Michael Jordan", "Leopold Sedar Sengor", "Marcus Aurelius", "Elon Musk"]
greeting="Welcome to my humble home Mr. "
print (greeting+guests[0]+"!")
print (greeting+guests[1]+"!")
print (greeting+guests[2]+"!")
print (greeting+guests[3]+"!")

excused_guest=" won't be able to make it unfortunately !"

print ("\nMr."+guests.pop()+excused_guest)
guests.append("Barrack Obama")

print ("\n"+greeting+guests[0]+"!")
print (greeting+guests[1]+"!")
print (greeting+guests[2]+"!")
print (greeting+guests[3]+"!\n")

print("We found a bigger dinner table, how delightful !\n")

guests.insert(0,"Emmanuel Macron")
guests.insert(2,"Dave Chapelle")
guests.append("Jimmy Fallon")

print (greeting+guests[0]+"!")
print (greeting+guests[1]+"!")
print (greeting+guests[2]+"!")
print (greeting+guests[3]+"!")
print (greeting+guests[4]+"!")
print (greeting+guests[5]+"!")
print (greeting+guests[6]+"!")

print ("What a pitty! Our table has now shrunk and we can only keep two guest !\n")

print ("Apologies Mr. "+guests.pop()+", we will have to do this some other time, tada!")
print ("Apologies Mr. "+guests.pop()+", we will have to do this some other time, tada!")
print ("Apologies Mr. "+guests.pop()+", we will have to do this some other time, tada!")
print ("Apologies Mr. "+guests.pop()+", we will have to do this some other time, tada!")
print ("Apologies Mr. "+guests.pop()+", we will have to do this some other time, tada!\n")

greeting="Your invitation is still valid and you are welcome to my humble home Mr. "
print (greeting+guests[0]+"!")
print (greeting+guests[1]+"!\n")