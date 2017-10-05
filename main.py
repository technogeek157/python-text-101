global currentstate
currentstate = "dungeon_01"
global define

def state_dungeon_01(currentstate): #this is one of the states
	print("You are in a dank dungeon. There are stone walls all around. There is a wooden chest and a lit torch on the wall.\n\n" +
				"Press C to open the Chest, D to try the Door, and T to look at the Torch")
	playerinput = raw_input()
	playerinput = playerinput.lower()
	if playerinput == "c":
		currentstate = "chest_01"
	elif playerinput == "d":
		currentstate = "door_01"
	elif playerinput == "c":
		currentstate = "torch_01"
	return currentstate

def state_chest_01():
	print("The chest is almost empty, but there is a unlit torch inside.\n\n" +
	      "Press R to Return")
	playerinput = raw_input()
	if playerinput == "r":
		currentstate = "dungeon_01"
	return currentstate

while True: #main loop, starts functions
	if currentstate == "dungeon_01":
		currentstate = state_dungeon_01(currentstate)
	elif currentstate == "chest_01":
		currentstate = state_chest_01()
