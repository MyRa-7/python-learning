from sys import exit

room_type = 0
moves = 0
key = money = food = coat = 0
orc = dragon = 1
flee = 0
solved = 0

def space_bar():
	print "\n\n"

def choice(room_type):

	print "There are %d ways out, which one do you pick?" % room_type
	door_choice = raw_input("> ")

	if not door_choice.isdigit():
		print "Enter a number."
		choice(room_type)
	elif int(door_choice) > room_type or int(door_choice) < 1 :
		print "Invalid choice."
		choice(room_type)
	else: 
		return int(door_choice)

def room_aa():

	room_type = 2
	global key, money, food, coat, moves
	moves += 1

	space_bar()
	print "This is your home. This is where you want to be."
	
	if not key:
		print "I see you don't have the door key yet, first find it and return."
	else:
		print "I see you have the key, well done."

	if not money and not food:
		print "See, it's easy to just stay here, but you need your money and food. Go get some more."
	else:
		print "You're well stocked up. Be at peace."

	if not coat:
		print "There are very few people who can always escape unscathed without facing battles. ",
		print "So, I suggest that you anyway get the Mithril Coat."
	else:
		print "Your battle scars speak of your glory."

	if key and money and food and coat:
		print "Excellent job. You won! This home is yours. You got here in %d moves" % moves
		exit(0)
	else:
		print "Earn this home. Continue your quest."
		door_choice = choice(room_type)

		if door_choice == 1 :
			room_ba()
		else :
			room_ab()


# room_aa(1, 1, 1, 0)

def room_ab():

	room_type = 3
	global coat, moves
	moves += 1

	space_bar()
	if not coat: 
		print "Frodo had to get this from Bilbo, and Bilbo had to steal it from the dwarves."
		print "(or did they give it to him? I'll never rememeber)."
		print "But now that you're here, take the Mithril Coat."

		coat = 1

		print "You will now be protected from dragons and swords alike."
		print "Never be fooled and give this away for any amount of gold or money to anyone, unless you love them truly."
		print "But if you do love them this much, well done."
	else:
		print "You already have the coat. There's nothing more for you here."

	door_choice = choice(room_type)

	if door_choice == 1 :
		room_aa()
	elif door_choice == 2 :
		room_bb()
	else :
		room_ac()


# room_ab(0, 0, 0, 1)

def room_ba():

	room_type = 3
	global money, coat, orc, flee, moves
	moves += 1
	space_bar()

	print "There is an orc in front of you."

	if orc:
		print "And it's alive!"
		print "It's coming at you with a sword, what do you do? Fight or Flee? "
		orc_choice = raw_input("> ")

		if orc_choice == "Fight" or orc_choice == "fight":
			print "You chose to fight."

			if not coat:
				print "Bad choice, you don't have your Mithril Coat. First find that."
				
				if not money:
					print "I'm teleporting you to Square 1, literally."
					room_bc()
				else:
					print "Hey wait. I see you have money. You can bribe the orc."
					print "More like, you have to bribe the orc. So you do."
					money = 0
					print "The orc lets you pass for now."
			else:
				print "With the protection of your Mithril Coat, you have defeated the orc."
				orc = 0
		elif orc_choice == "Flee" or orc_choice == "flee":
			print "You choose to flee. Okay, but you probably can't do this forever."
		else:
			print "You must choose only between the two. I am restarting this round for you."
			room_ba()
		
	else:
		print "It's dead though. You may proceed as you wish."

	door_choice = choice(room_type)

	if door_choice == 1:
		room_ca()
	elif door_choice == 2:
		room_bb()
	else:
		room_aa()


# room_ba(0, 1, 0, 1)
# room_ba(0, 1, 0, 1)

def room_ca():

	room_type = 2
	global key, flee, orc, dragon, moves
	moves += 1
	space_bar()

	print "This is where you can get your key."

	if not orc and not dragon:
		print "And with your bravery, you've earned your key."
		key = 1
		print "Good job. Proceed."
	else:
		print "You may not see it now because the key knows that you've not proved yourself."
		print "Yet. However, proceed and return later."

	door_choice = choice(room_type)

	if door_choice == 1:
		room_cb()
	else:
		room_ba()



# room_ca(0, 0, 0, 0)
# orc = dragon = 0
# room_ca(0, 0, 0, 0)

def room_cb():

	room_type = 3
	global food, coat, flee, moves
	moves += 1
	space_bar()

	print "There is a dragon in front of you."

	global dragon

	if dragon:
		print "And it's alive!"
		print "It's spewing smoke, its nostrils are flaring and its eyes are red."
		print "What do you do? Fight or Flee? "
		dragon_choice = raw_input("> ")

		if dragon_choice == "Fight" or dragon_choice == "fight":
			print "You chose to fight."

			if not coat:
				print "Bad choice, you don't have your Mithril Coat. First find that."
				
				if not food:
					print "I'm teleporting you to Square 1, literally."
					room_bc()
				else:
					print "Hey wait. I see you have food. You can appease the dragon."
					print "More like, you have to appease the dragon. So you do."
					food = 0
					print "The dragon lets you pass for now."
			else:
				print "With the protection of your Mithril Coat, you have defeated the dragon."
				dragon = 0
		elif dragon_choice == "Flee" or dragon_choice == "flee":
			print "You choose to flee. Okay, but you probably can't do this forever."
		else:
			print "You must choose only between the two. I am restarting this round for you."
			room_cb()
		
	else:
		print "It's dead though. You may proceed as you wish."

	door_choice = choice(room_type)

	if door_choice == 1:
		room_cc()
	elif door_choice == 2:
		room_bb()
	else:
		room_ca()

# room_cb()
# key = 1 ; food = 1; coat = 1
# room_cb()

def room_bb():

	room_type = 4
	global solved, moves
	moves += 1
	space_bar()

	print "This is the midpoint of your journey, maybe not really, only literally. "
	print "Solve this riddle to proceed. You have infinite tries."

	if not solved:
		print "\nThe crux of mathematical logic is the truth of statements."
		print "If I say \"There are 10 ways to represent the truth of a statement.\""
		print "Am I lying or saying the truth? And why?"
		print "I will look for two keywords in your answer."
		print "One of them is True/False."
		print "Other rhymes with something from the 'flower pot' family."

		while not solved:
			riddle_ans = raw_input("> ")

			if ("True" in riddle_ans or "true" in riddle_ans) and ("base" in riddle_ans or "Base" in riddle_ans):
				solved = 1
			else:
				print "Try again."
	else:
		"\nOh wait."

	print "Yay! You've cleared it. Good job."

	door_choice = choice(room_type)

	if door_choice == 1:
		room_cb()
	elif door_choice == 2:
		room_bc()
	elif door_choice == 3:
		room_ab()
	else:
		room_ba()


# room_bb()

def room_cc():

	room_type = 2
	global money, moves
	moves += 1
	space_bar()

	print "This is where you get your money."
	print "Ironically, for free."
	print "Just come here, take the money you want."
	print "How many ever times you want."
	print "Only catch : You only get a fixed amount everytime. And I decide it."

	print "Here, take your money."
	money = 1

	print "So long!"

	door_choice = choice(room_type)

	if door_choice == 1:
		room_bc()
	else:
		room_cb()

def room_ac():

	room_type = 2
	global food, moves
	moves += 1
	space_bar()

	print "This is where you get food."
	print "You can have how much ever you want while you're here."
	print "But once you ask for a parcel, I make it."

	print "Here, take your food." 
	food = 1

	print "So long!"

	door_choice = choice(room_type)

	if door_choice == 1:
		room_ab()
	else:
		room_bc()

def room_bc():

	room_type = 3
	global moves
	space_bar()

	print "Welcome."
	
	if not moves:
		print """
		I am the chief here. I'll be walking you through your game.
		In this game, you'll be moving through a small labyrinth of interconnected rooms.
		You're free to choose your path.
		You may meet obstacles and power ups. 
		I'll be there at each step, needn't worry.
		Have fun!
		"""
	else:
		print "Hope you're having fun."

	door_choice = choice(room_type)

	if door_choice == 1:
		room_ac()
	elif door_choice == 2:
		room_bb()
	else:
		room_cc()

room_bc()

