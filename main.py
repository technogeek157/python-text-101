global currentstate
currentstate = "dungeon_01"
global keyDict
global newState
newState = ""
returnkey = "Press R to Return"

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

while True:
    if currentstate == "dungeon_01":
      newState = three_room("You are in a dark dungeon, there is a torch on the wall, " +
      "a chest in the corner, and a closed wood and iron door leading out.",
      "Hit C to look at the Chest, T to look at the Torch, and D to try the Door",
      'c', 't', 'd', "chest_01", "torch_01", "door_01")
      
    if currentstate == "chest_01":
      newState = two_room("Mostly empty, but a unlit torch lies in the bottom.",
      returnkey + ", T to Take the torch", 'r', 't', "dungeon_01", "dungeon_02")
      
    if currentstate == "torch_01":
      newState = one_room("A lit torch.", returnkey, 'r', "dungeon_01")
      
    if currentstate == "door_01":
      newState = two_room("An old dungeon door. It appears to be unlocked.",
      returnkey + ", C to Continue", 'r', 'c', "dungeon_01", "corridor_01")
      
    if currentstate == "corridor_01":
      newState = two_room("A dark corridor stretches before you. If it has a end, " +
      "darkness conceals it. You are likely to be eaten by a Grue.", 
      returnkey + ", C to Continue", 'r', 'c', "dungeon_01", "Grue")
      
    if currentstate == "Grue":
      newState = one_room("You have been eaten by a Grue! Try again?",
      "Press R to Retry", 'r', "dungeon_01")
      
    if currentstate == "dungeon_02":
      newState = three_room("You are in a dark dungeon, there is a torch on the wall, " +
      "a chest in the corner, and a closed wood and iron door leading out. You have a unlit torch in your hand", "Press C to look at the Chest, T to look at the Torch, and D to look at the Door", 'c', 't', 'd', "chest_02", "torch_02", "door_02")
      
    if newState != "kpe":
      currentstate = newState
    else:
      print("Key not recognized \n\n")
