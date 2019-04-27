rooms = [
["You are at the shore of a deserted island; there is a wrecked dingy here. You recall the name of the ship: it's Makola. While you wonder about your past, you almost trip over a small, sharp rock.", {"W": 1, "E": 2, "N": 3,"S": 27}, ["rock"]],
["You walk down the shore and spot a turtle! It looks very relaxed with your presence", {"E": 0}, []],
["You head east but there is a giant hole in the way! It seems that you cannot continue any further.", {"W": 0, "D": 4}, []],
["You cautiously walk into the jungle. Something about how the tall trees wave back and forth in the wind unnerves you.", {"S": 0,"U": 15, "W": 23, "N": 25}, ["stick"]],
["You start climbing down the giant hole. It is a very sandy descent. But, eventually you reach the bottom, which happens to be made of stone.", {"U": 5, "W": 6}, []],
["You climb back up, slipping and sliding on the sides of the hole. After a while you finally get back up to the top.", {"W": 0, "D": 4}, []],
["You have found a Secret Door! Enter it? (yes or no?)", {"YES": 7,"NO": 8, "OR": 26}, []],
["You enter the Secret Door and are hit with a wave of cold air causing you to shiver. As you go further in, you hear the Secret Door close behind you. There is no turning back. There are three hallways, one to the west, one to the east, and one to the north.", {"W": 9,"E": 11,"N": 13}, []],
["You decide against entering the Secret Door and to stay in the hole for now.", {"U": 6, "W": 7}, []],
["You take the hallway to the west. You walk and walk and walk until you reach the end. There is something on the wall you can't make it out. \n Maybe something can make it clearer?", {"E": 10}, []],
["You walked back to the trident in the road. You decide to make your next move.", {"W": 9,"E":11 ,"N": 13}, []],
["The east hallway a perfect choice. You walk down the hallway, as you go further and further there are pictures each one is the exact same. You feel like you should turn back but you haven't reached the end yet.", {"E": 12,"W": 10}, []],
["You man up and keep walking forward, you reach the end. there is a room, inside it has a picture of the ones you have seen in the hallway. There is something off about this picture though.", {"W": 14}, []],
["You went north, because middle is the best! Wait... isn't that only for oreo's? Your thoughts get interupted as you reach the end of the north hallway. There is a giant door, but it seems as if something has to be done first.", {"S": 10}, []],
["You walk back from the room back into the east hallway. You see the pictures again. These seem right.", {"E": 12,"W": 10}, []],
["You for some reason decided to climb a tree. You go all the way up to the thinnest branches you can go without breaking them. You look around and spot a symbol * in the sand \n Maybe it have some meaning?", {"D": 16}, []],
["You climb down the tree. You are glad ground is under your feet again!", {"U": 17,"S": 0}, []],
["You climb up the tree again. You look over to the symbol, its *.", {"D": 18}, []],
["You climb down, you feel like you are done climbing for now...", {"U": 19,"S": 0}, []],
["You apparently weren't done climbing. You climb the tree yet again! The symbol is *.", {"D": 20}, []],
["You reach the ground (again...) and finally, you are ready to continue your journey!", {"U": 21,"S": 0}, []],
["You climbed back up the tree, you decided you weren't ready for the journey just yet. You don't even look at the symbols anymore because you got them memorized, right?", {"D": 22}, []],
["You climb back down. Hopefully you're ready to continue because you clearly cant decide if you want to stay in the tree or continue.", {"U": 21,"S": 0}, []],
["You start walking west. But not long after, you run into heavy foilage. You cannot get through.", {"E": 24}, []],
["You walk back to the place where you entered the jungle. The trees still unnerve you...", {"S": 0,"U": 15, "W": 23, "N": 25}, []],
["You head further into the forest. There seems to be a structure east of here. But it doesn't seem like you can head that way yet because of the prickle bushes.", {"S": 24}, []],
["You're funny, aren't ya?", {"W": 6,"N": 6,"S": 6,"E": 6}, []],
["You head into the ocean, sadly you didnt grab your floaties. You soon drown (R to reset)", {"S": 27}, []],
["You got through the prickle bushes, there before you is the structure you saw. Its a temple", {}, []]
["You enter the newly opened door, there is a gem. Pick it up? (yes or no)", {}, []]
]
items = {"rock": ("drop", "use", "combine"), 
"stick": ("drop", "use", "combine"),
"spear:": ("drop", "use")
}
buildable_items ={("rock","stick"): "spear"}

def display_current_location(room_index):
	print(rooms[room_index][0])
	if len (rooms[room_index]) > 2:
		if len (rooms[room_index][2]) == 1:
			print("There is a")
			for item in rooms[room_index][2]:
				print(item)
		if len (rooms[room_index][2]) > 1:
			print("There are")
			for item in rooms[room_index][2]:
				print(item)

def manage_inventory(room_index):
	print(player_inventory)
	room = rooms[room_index]
	room_items = rooms[room_index][2]
	while(True):
		item = input("What item do you want to work with: ")
		if not item:
			return
		if item in items:
			print(items[item])
		action = input("What action do you want to do: ")
		if not action:
			return
		if action in (items[item]):
			if action.lower()=="drop":
				room_items.append(item)
				print("You have dropped a {0}".format(item))
				player_inventory.remove(item)
			if action.lower()=="use":
				if item == "rock":
					print("This item may not be used in this form.")
				if item == "stick":
					print("This item may not be used in this form.")
			if action.lower()=="combine":
				combine = input("What item do you want to combine this with: ")
				if not combine:
					return
				recipe = tuple([item, combine].sort())
					if recipe in buildable_items:
						player_inventory.append(buidlable_items[recipe])
						player_inventory.remove(item, combine)
			print(player_inventory)

room_index = 0
player_inventory = []
welcome_text = "Welcome to The Ridgehacks Text Adventure Game. You are now Frederick the 55th. You wake up groggy and confused. After a minute, you realize you are on the shore with the ocean at your heels. You try to remember how you got here and what happened but you don't remember anything from the past couple of days. How did you get here? And how do you get back?"
print (welcome_text)
display_current_location(room_index)
commands = ("Commands: \n N: Move North \n E: Move East \n S: Move South \n W: Move West \n U: Move Up \n D: Move Down \n Inventory (I): Look at items in your inventory \n Collect (C): Pick up an item \n Use (US): Use selected item \n H: Help \n Q: Quit Game \n R: Restart Game")
print (commands)
while(True):
	move = input("Make a move: ").upper()
	if move in rooms[room_index][1]:
		room_index = rooms[room_index][1][move]
	elif move == "I":
		manage_inventory(room_index)
	elif move == "Q":
		break		
	elif move == "R":
		print (welcome_text)
		room_index = 0		
	elif move == "C":
		room = rooms[room_index]
		room_items = rooms[room_index][2]
		if (len(room) > 2) and (len(room_items) >= 1):
			player_inventory.append(room_items[0])
			print("You have picked up a {0}".format(room_items[0]))
			room_items.remove(room_items[0])
	elif move == "H":
		print (commands)
	else:
		print("Not a valid move")
  
	
	display_current_location(room_index)
