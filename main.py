currentState = 'dungeon_01'
states = ["dungeon_01", "door_01", "torch_01", "corridor_01", "dungeon_02", "chest_02", "door_02", "torch_02", "corridor_02", 
					"grue", "dungeon_03", "chest_03", "torch_03", "corridor_03"]
statechange = true

while true: #main loop, starts functions
	if currentState == "dungeon_01":
		state_dungeon_01()

def state_dungeon_01(): #this is one of the states
	print("You are in a dank dungeon. There are stone walls all around. There is a wooden chest and a lit torch on the wall.\n\n" +
				"Press C to open the Chest, D to try the Door, and T to look at the Torch")
	playerinput = raw_input()
	if playerinput == "C":
		currentstate = "chest_01"
	elif playerinput == "D":
		currentstate = "door_01"
	elif playerinput == "T":
		currentstate = "torch_01"
