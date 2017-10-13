global currentstate
currentstate = "dungeon_01"
global keyDict
global newState
newState = ""
returnkey = "Press R to Return"
chestPoint = False

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
      "a chest in the corner, and a closed wood and iron door leading out. You have a unlit torch in your hand",
      "Press C to look at the Chest, T to look at the Torch, and D to look at the Door", 
      'c', 't', 'd', "chest_02", "torch_02", "door_02")
      
    if currentstate == "chest_02":
      newState = one_room("Nope, nothing here.", returnkey, 'r', "dungeon_02")
         
    if currentstate == "door_02":
      newState = two_room("An old dungeon door. It appears to be unlocked.",
      returnkey + ", C to Continue", 'r', 'c', "dungeon_02", "corridor_02")
      
    if currentstate == "torch_02":
      newState = two_room("Well, are you just going to stand there, or light the torch?", 
      returnkey + ", L to Light your torch.", 'r', 'l', 'dungeon_02', 'dungeon_03')
      
    if currentstate == "corridor_02":
      newState = two_room("A dark corridor stretches before you. If it has a end, " +
      "darkness conceals it. You are likely to be eaten by a Grue.", 
      returnkey + ", C to Continue", 'r', 'c', "dungeon_02", "Grue")
      
    if currentstate == "dungeon_03":
      newState = three_room("The dungeon burns slightly brighter with the light of your torch.",
      "D to try the Door, C to look in the Chest, T to inspect the Torch", 
      'd', 'c', 't', 'door_03', "chest_03", "torch_03")
      
    if currentstate == "chest_03":
      newState = one_room("Well, aren't you persistent! Here's a bonus point for you!", returnkey,
      'r', "dungeon_03")
      chestPoint = True
      
    if currentstate == "torch_03":
      newState = one_room("Yep, still burning, but it might not burn forever, and the the Grues will come out",
      returnkey, 'r', "dungeon_03")
      
    if currentstate == "door_03":
      newState = two_room("An old dungeon door. It appears to be unlocked.",
      returnkey + ", C to Continue", 'r', 'c', "dungeon_03", "corridor_03")
      
    if currentstate == "corridor_03":
      newState = two_room("At the end of the corridor, there is a door, set in stone.", returnkey + 
      ", C to Continue", 'r', 'c', "dungeon_03", " ")
      
    if newState != "kpe":
      currentstate = newState
    else:
      print("Key not recognized \n\n")
