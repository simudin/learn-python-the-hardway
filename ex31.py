print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "THe bear eats your face off!. Good Job!"
	elif bear == "2":
		print "The bears eat your legs off. Good job!"
	else:
		print "Well, doing %s is better. The bear runs away." % bear

elif door == "2":
	print "You stare into endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yello jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "You body surve=ives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of mucks. Good job!"

else:
	print "YOu stumble around and fall on a knife and die. Good job!"