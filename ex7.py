from sys import exit

def gold_room():
	print "This room is full of gold. How much doo you take?"
	
	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much = init(next)
	else:
		dead ("Type a number")
	if how_much < 50:
		print "You can go on!"
		exit(0)
	else:
		dead("You greedy Motherfucker!")
		
	
def bear_room():
	print"There is a bear with a lot of honey"
	print"The bear blocks you way through!"
	print"How are going to get through?"
	bear_moved = False
	
	while True:
		next = raw_input(">")
		
		if next == "take honey":
			dead("The bear slaps you after realising you stole his honey")
		elif next == "taunt bear" and not bear_moved:
			print"The bear moved from the door"
			bear_moved = True
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print"What do you mean?"
			

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
 
	next = raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room() 
			
			
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room with two doors in front of you."
	print "Which one do you choose, left or right?"
	
	next = raw_input(">")
	
	if next == "left":
		bear_room()
	
	elif next == "right":
		cthulhu_room()
	else:
		dead("You die in the dark for not finding an exit.")
		


start()