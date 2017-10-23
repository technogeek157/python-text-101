import random, time
global currentstate
global newState
newState = ""
returnkey = "Press R to Return"
chestPoint = False

global playerHealth, playerItem, pastState, itemDamage, enemyHealth, playerTreasure

def inventory():
        print("\n\nYou have " + str(playerTreasure) + " Gold, and a " + playerItem + ". It does " + str(itemDamage) + " damage.")
        time.sleep(2)
        return currentstate
                        

def clear():
        print "\n" * 1000

def status_report(h):
        print "You have " + str(playerHealth) + ' health.'
        print "The monster has " + str(h) + " health."

def one_room(situation, gotos, keyOne, gotoOne):
                clear()
                print("\n\n" + situation + "\n\n" + gotos)
                playerinput = raw_input()
                playerinput = playerinput.lower()
                if playerinput == keyOne:
                                return gotoOne
                                print gotoOne

                elif playerinput == 'i':
                        return inventory()
                else:
                                return("kpe")
                
def two_room(situation, gotos, keyOne, keyTwo, gotoOne, gotoTwo):
                clear()
                print("\n\n" + situation + "\n\n" + gotos)
                playerinput = raw_input()
                playerinput = playerinput.lower()
                if playerinput == keyOne:
                        return gotoOne
                            
                elif playerinput == keyTwo:
                        return gotoTwo

                elif playerinput == 'i':
                        return inventory()
                    
                else:
                        return("kpe")

def three_room(situation, gotos, keyOne, keyTwo, keyThree, gotoOne, gotoTwo, gotoThree):
                clear()
                print("\n\n" + situation + "\n\n" + gotos)
                playerinput = raw_input()
                playerinput = playerinput.lower()
                if playerinput == keyOne:
                                return gotoOne
                        
                elif playerinput == keyTwo:
                        return gotoTwo
                
                elif playerinput == keyThree:
                        return gotoThree

                elif playerinput == 'i':
                        return inventory()
                        
                else:
                        return("kpe")

def treasure_room(situation, gotos, keyOne, gotoOne, treasure):
                clear()
                global playerTreasure
                if playerTreasure == 0:
                        tNotification = "\n\nFrom now on, press I to view your inventory!"
                else:
                        tNotification = ''
                print("\n\n" + situation + "\n\nThe room contains " + str(treasure) + " treasure.\n\n" + gotos + tNotification)
                playerTreasure = playerTreasure + treasure
                playerinput = raw_input()
                playerinput = playerinput.lower()
                if playerinput == keyOne:
                                return gotoOne
                                print gotoOne
                else:
                                return("kpe")
                        
def gremlin(description, p, level):
        global playerHealth, currentstate
        clear()
        enemyHealth = 5 * level
        attackPower = 1 * level
        while True:
                if playerHealth <= 0: #player death
                        print "\nYou lost all of your health."
                        time.sleep(2)
                        return "dead"
                        
                elif enemyHealth <=0: #monster death
                        print "\nYou defeated the monster."
                        time.sleep(2)
                        return p

                        
                else:
                        clear()
                        print ("You have come across a gremlin. " + description + " It has " + str(enemyHealth) + " health." + "\n\n")
                        print ("Press R to Retreat, A to Attack, R to Retreat. You have a " + playerItem + ".")
                        print ("It does " + str(itemDamage) + " damage."  + "\n\n")
                        playerinput = raw_input()
                        playerinput = playerinput.lower()
                        clear()
                        
                        if playerinput == 'a':
                                clear()
                                if random.randint(1,2) == 1:
                                  print "You hit the monster!\n\n"
                                  time.sleep(1)
                                  print "You did " + str(itemDamage) + " damage.\n\n"
                                  time.sleep(1)
                                  enemyHealth = enemyHealth - itemDamage
                                  
                                else:
                                  print "You missed the monster.\n\n"
                                  time.sleep(1)
                                                        
                        if playerinput == 'r': #retreats
                                if random.randint(1,2) == 1:
                                  print "You were able to retreat!"
                                  time.sleep(2)
                                  return pastState
                                
                                else:
                                  print "Retreat failed."
                                  time.sleep(2)
                                  return currentstate
                                                          
                        if playerinput != 'a' and playerinput != 'r':
                          print "Key not recognized."
                          kpe = True
                          time.sleep(1)
                        else:
                                                        kpe = False

                if kpe != True:
                        if random.randint(1, 2) == 1:
                                print "The monster hit you!\n\n"
                                time.sleep(1)
                                print "It did " + str(attackPower) + " damage.\n\n"
                                playerHealth = playerHealth - attackPower
                                time.sleep(1)
                                status_report(enemyHealth)
                                time.sleep(2)

                        else:
                                print "The monster missed.\n\n"
                                time.sleep(1)
                                status_report(enemyHealth)
                                time.sleep(2)
def troll(description, p, level):
        global playerHealth, currentstate
        clear()
        enemyHealth = 10 * level
        attackPower = 3 * level
        while True:
                if playerHealth <= 0: #player death
                        print "\nYou lost all of your health."
                        time.sleep(2)
                        return "dead"
                        
                elif enemyHealth <=0: #monster death
                        print "\nYou defeated the monster."
                        time.sleep(2)
                        return p

                        
                else:
                        clear()
                        print ("You have come across a troll. " + description + " It has " + str(enemyHealth) + " health." + "\n\n")
                        print ("Press R to Retreat, A to Attack, R to Retreat. You have a " + playerItem + ".")
                        print ("It does " + str(itemDamage) + " damage."  + "\n\n")
                        playerinput = raw_input()
                        playerinput = playerinput.lower()
                        clear()
                        
                        if playerinput == 'a':
                                clear()
                                if random.randint(1,2) == 1:
                                  print "You hit the monster!\n\n"
                                  time.sleep(1)
                                  print "You did " + str(itemDamage) + " damage.\n\n"
                                  time.sleep(1)
                                  enemyHealth = enemyHealth - itemDamage
                                  
                                else:
                                  print "You missed the monster.\n\n"
                                  time.sleep(1)
                                                        
                        if playerinput == 'r': #retreats
                                if random.randint(1,2) == 1:
                                  print "You were able to retreat!"
                                  time.sleep(2)
                                  return pastState
                                
                                else:
                                  print "Retreat failed."
                                  time.sleep(2)
                                  return currentstate
                                                          
                        if playerinput != 'a' and playerinput != 'r':
                          print "Key not recognized."
                          kpe = True
                          time.sleep(1)
                        else:
                                                        kpe = False

                if kpe != True:
                        if random.randint(1, 2) == 1:
                                print "The monster hit you!\n\n"
                                time.sleep(1)
                                print "It did " + str(attackPower) + " damage.\n\n"
                                playerHealth = playerHealth - attackPower
                                time.sleep(1)
                                status_report(enemyHealth)
                                time.sleep(2)

                        else:
                                print "The monster missed.\n\n"
                                time.sleep(1)
                                status_report(enemyHealth)
                                time.sleep(2)
playerHealth = 10
playerItem = 'torch'
playerHealth = 10
maxHealth = 10
currentstate = "dungeon_01"
itemDamage = 1
playerTreasure = 0

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
                        "darkness conceals it. You are likely to be eaten by a grue.", 
                        returnkey + ", C to Continue", 'r', 'c', "dungeon_01", "grue")
                        
                if currentstate == "grue":
                        newState = one_room("You have been eaten by a grue!",
                        "Press C to Continue", 'c', "dungeon_01")
                        newState = "dead"
                        
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
                        "darkness conceals it. You are likely to be eaten by a grue.", 
                        returnkey + ", C to Continue", 'r', 'c', "dungeon_02", "grue")
                        
                if currentstate == "dungeon_03":
                        newState = three_room("The dungeon burns slightly brighter with the light of your torch.",
                        "D to try the Door, C to look in the Chest, T to inspect the Torch", 
                        'd', 'c', 't', 'door_03', "chest_03", "torch_03")
                        
                if currentstate == "chest_03":
                        newState = one_room("Well, aren't you persistent! Here's a bonus point for you!", returnkey,
                        'r', "dungeon_03")
                        chestPoint = True
                        
                if currentstate == "torch_03":
                        newState = one_room("Yep, still burning, but it might not burn forever, and the the grues will come out",
                        returnkey, 'r', "dungeon_03")
                        
                if currentstate == "door_03":
                        newState = two_room("An old dungeon door. It appears to be unlocked.",
                        returnkey + ", C to Continue", 'r', 'c', "dungeon_03", "corridor_03")
                        
                if currentstate == "corridor_03":
                        newState = two_room("At the end of the corridor, there is a door, set in stone.", returnkey + 
                        ", C to Continue", 'r', 'c', "dungeon_03", "gremlin1")
                        
                if currentstate == 'gremlin1':
                        newState = gremlin("It is dirty.", 'sword_room_1', 1)
                        print newState

                if currentstate == "sword_room_1":
                        newState = one_room("There is a obvious reason for the gremlin's presence. There is a chest in front with a sheithed sword poking out. The gremlin was pulling it out when you walked in",
                                            'Press P to Pick Up the sword', 'p', 'sword_room_2')

                if currentstate == "sword_room_2":
                        #this is an example of a player picking up a item
                        playerItem = "Rusted Sword"
                        itemDamage = 3

                        newState = one_room("You look at the sword. It is rusted, but should serve it's purpose.", "Press C to Continue", 'c', "sword_room_3")

                if currentstate == "sword_room_3":
                        newState = three_room("Looking around, you notice three doors set in the stone a round you.", "Press R to go through the Right Door, " +
                                              "L to go through the Left Door, C to go through the Center Door.", 'r', 'l', 'c', 'treasure_room_1', "dead_end_1", "troll_1")

                if currentstate == "treasure_room_1": #here is a room with treasure inside
                        newState = treasure_room("Good Job! This room contains a small box with treasure inside!", returnkey, 'r', 'sword_room_3', 100)

                if currentstate == "dead_end_1":
                        newState = one_room("Oops, this is a dead end. You will find several of these on your adventures.", returnkey, 'r', 'sword_room_3')

                if currentstate == "troll_1":
                        newState = troll("It towers above you.", 'eol', 1)

                #below this line is basic mechanincs: death, unrecongnized keys, assigning states, ect.
                if currentstate =="dead":
                        newState = one_room("You have Died! Try again?", "Press R to Retry!", 'r', 'dungeon_01')
                        playerHealth = 10
                        playerItem = 'torch'
                        playerHealth = 10
                        maxHealth = 10
                        currentstate = "dungeon_01"
                        itemDamage = 1
                        playerTreasure = 0

                if newState != "kpe":
                  pastState = currentstate
                  currentstate = newState
                else:
                        print("Key not recognized \n\n")
                        time.sleep(1)
