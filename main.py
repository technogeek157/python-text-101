import random
global currentstate
currentstate = "dungeon_01"
global keyDict
global newState
newState = ""
returnkey = "Press R to Return"
chestPoint = False
global playerHealth, playerItem
playerHealth = 10
playerItem = 'torch'

def one_room(situation, gotos, keyOne, gotoOne):
		print("\n\n" + situation + "\n\n" + gotos)
		playerinput = raw_input()
		playerinput = playerinput.lower()
		if playerinput == keyOne:
				return gotoOne
		else:
				return("kpe")
		
def two_room(situation, gotos, keyOne, keyTwo, gotoOne, gotoTwo):
		print("\n\n" + situation + "\n\n" + gotos)
		playerinput = raw_input()
		playerinput = playerinput.lower()
		if playerinput == keyOne:
				return gotoOne
		elif playerinput == keyTwo:
			return gotoTwo
		else:
			return("kpe")

def three_room(situation, gotos, keyOne, keyTwo, keyThree, gotoOne, gotoTwo, gotoThree):
		print("\n\n" + situation + "\n\n" + gotos)
		playerinput = raw_input()
		playerinput = playerinput.lower()
		if playerinput == keyOne:
				return gotoOne
		elif playerinput == keyTwo:
			return gotoTwo
		elif playerinput == keyThree:
			return gotoThree
		else:
			return("kpe")
			
def gremlin(description, p, level):
	attackPower = 2
	fighting = False
	enemyHealth = 5 * level
	print ("You have come across a gremlin. " + description + " It has " + 
	str(enemyHealth) + " health." + "\n\n")
	print ("Press R to Retreat, A to Attack, you have a " + playerItem + "\n\n")
 
	while True:
	 if enemyHealth == 0:
	 	print "You killed the monster!"
	 	break
	 
	 playerinput = raw_input("Your turn.")
	 playerinput = playerinput.lower()
	 
	 if playerinput == 'r':
	 	if random.randint(1, 2) == 1:
	 		print "\nRetreated!"
			break
		else:
			print "\nFailed to retreat"
	 elif playerinput == 'a':
			if random.randint(1, 2) == 1:
				print "\nYou hit the monster!"
				enemyHealth = enemyHealth - 1
			else:
				print "\nYou missed."
	 print "\nYou have " + str(playerHealth) + " health. \nThe monster has " + str(enemyHealth) + " health.\n"
	 
	 desicion = random.randint(1,2)
	return p 
	
while True:
		if currentstate == "dungeon_01":
			newState = gremlin("It is dirty", 'p', 1)
		
		if newState != "kpe":
			currentstate = newState
		else:
			print("Key not recognized \n\n")
