global currentstate
currentstate = "dungeon_01"
global keyDict
global newState
newState = ""
keyDict = {}

def state_dungeon_01(): #this is one of the states
    print("You are in a dank dungeon. There are stone walls all around. There is a wooden chest and a lit torch on the wall.\n\n" +
                "Press C to open the Chest, D to try the Door, and T to look at the Torch\n")
    playerinput = raw_input()
    playerinput = playerinput.lower()
    if playerinput == "c":
        currentstate = "chest_01"
    elif playerinput == "d":
        currentstate = "door_01"
    elif playerinput == "t":
        currentstate = "torch_01"
    return currentstate

def state_dungeon_02():
    print("You are in a dank dungeon. There are stone walls all around. There is a wooden chest " +
          "and a lit torch on the wall. You have a unlit torch in your hand.\n\n" +
                "Press C to open the Chest, D to try the Door, and T to look at the Torch\n")
    playerinput = raw_input()
    playerinput = playerinput.lower()
    if playerinput == "c":
        currentstate = "chest_02"
    elif playerinput == "d":
        currentstate = "door_02"
    elif playerinput == "t":
        currentstate = "torch_02"
    return currentstate

def state_dungeon_03():
    print("The room burnes slightly brighter with the added light of your torch.\n\n" +
          "Press C to open the Chest, D to try the Door, and T to look at the Torch\n")
    playerinput = raw_input()
    playerinput = playerinput.lower()
    if playerinput == "c":
        currentstate = "chest_03"
    elif playerinput == "d":
        currentstate = "door_03"
    elif playerinput == "t":
        currentstate = "torch_03"
    return currentstate

def state_chest_01():
    print("The chest is almost empty, but there is a unlit torch inside.\n\n" +
          "Press R to Return, T to Take the torch\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_01"
    elif playerinput == "t":
        currentstate = "dungeon_02"
    return currentstate

def state_chest_02():
    print("The chest is empty, were you expecting something?\n\n" +
          "Press R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_02"
    return currentstate

def state_chest_03():
    print("Well points for persistance, so here's a bonus point!\n\n" +
          "Press R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_03"
    return currentstate

def state_door_01():
    print("This is a old dungeon door. It appears to be unlocked. \n\n" +
          "Press C to continue, R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_01"
    elif playerinput == "c":
        currentstate = "corridor_01"
    return currentstate

def state_door_02():
    print("This is a old dungeon door. It appears to be unlocked. \n\n" +
          "Press C to continue, R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_02"
    elif playerinput == "c":
        currentstate = "corridor_02"
    return currentstate

def state_door_03():
    print("This is a old dungeon door. It appears to be unlocked. \n\n" +
          "Press C to continue, R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_03"
    elif playerinput == "c":
        currentstate = "corridor_03"
    return currentstate

def state_torch_01():
    print("This is a torch, it burnes with a orange light, illuminating the room.\n\n" +
          "Press R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_01"
    return currentstate

def state_torch_02():
    print("Well, are you just going to stand there, or light the torch?\n\n" +
          "Press R to Return, L to Light your torch\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_02"
    elif playerinput == "l":
        currentstate = "dungeon_03"
    return currentstate

def state_corridor_01():
    print("A long corridor stretches before you, darkness concealing the end. " +
       "You are likely to be eaten by a grue.\n\n" +
          "Press C to continue, R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_01"
    elif playerinput == "c":
        currentstate = "grue"
    return currentstate

def state_corridor_02():
    print("A long corridor stretches before you, darkness concealing the end." +
       "You are still likely to be eaten by a grue.\n\n" +
          "Press C to continue, R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_02"
    elif playerinput == "c":
        currentstate = "grue"
    return currentstate

def state_corridor_03():
    print("A long corridor stretches before you, there is a door at the end. \n\n" +
          "Press C to continue, R to Return\n")
    playerinput = raw_input()
    if playerinput == "r":
        currentstate = "dungeon_03"
    elif playerinput == "c":
        currentstate = "EOL"
    return currentstate

def EOL():
    print("You beat level one!")

def state_grue():
    print("You were eaten by a grue! Tip: Grue's like the dark, so bring a light!\n\n" +
          "Try again? R for Retry\n")
    playerinput = raw_input()
    playerinput = playerinput.lower()
    if playerinput == "r":
        currentstate = "dungeon_01"
    return currentstate

def one_room(situation, gotos, keyOne, gotoOne):
    print(situation + "\n\n" + gotos)
    playerinput = raw_input()
    playerinput = playerinput.lower()
    if playerinput == keyOne:
        return gotoOne
    else:
        return("kpe")
    

while True:
    if currentstate == "dungeon_01":
        newState = one_room()
    if newState != "kpe":
        currentstate = newState