#adventure game by adam mehter
#debug by minto
import json
import sys, time, os
import getpass
class Opening:
    def startText():
        text="Welcome to the Adventure Game, here you will embark on a journey to defeat the Dragon named Justin, and rescue The Princess Cherry, your story begins in the small town of Jolt, type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions. Good luck"
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
    startText()
    #command list
    def commands():
        commTitle="\n\nCommand List"
        print(commTitle)
        heading="\nMovement"
        print(heading)
        moveCommands=["\nNorth", "\nSouth", "\nWest", "\nEast"]
        for char in moveCommands:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        heading2="\n\nUtil"
        print(heading2)
        utilCommands=["\nUse", "\nInventory", "\nLook", "\nSearch", "\nCommands"]
        for char in utilCommands:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    commands()
items=[]
#yeah
allPossibleItems=["saw", "3 Gold Pieces", "iron ore", "wood", "battleaxe", "Atari"]

place=1

town=2

forest=3

mine=4

lair=5

dead=6

game=0

on=90

win=91

game=on

place=town

lose=92

def credits(timer:float):
    time.sleep(timer)
    print('\n\n CREDITS  ')
    print('\n\n  DEVS')
    devs=["Adam Mehter", "Minto"]
    print(devs)
    print('\n\nCONTRIBUTORS')
    contribs=["Chris", "Reyes"]
    print(contribs)
    user = getpass.getuser()
    endingTxt= open('thanks.txt', 'w')
    endingTxt.write("Hey " + user + " Thank you for playing !!  You have completed this game. Good on you! The Devs thank you for playing")
while game==on:
   

    while place==town:

        direction=input("\nWhat would you like to do?\n")

        if direction=="west":
            if "iron ore" and "wood" and "3 Gold Pieces" in items:
                print ("the blacksmith greets you, and you tell him that you have the items and money he requires, you also give him the saw to make up for some of the difference, he then forges you a battleaxe and wishes you luck on the rest of your quest")
                items.remove ("saw")
                items.remove ("3 Gold Pieces")
                items.remove ("iron ore")
                items.remove ("wood")
                items.append ("battleaxe")
                print("You go back to town")
                place=town
            else:
              print ("You are at the blacksmith shop, many different kinds of weapons decorate the walls, the blacksmith is a tall, hairy man who smiles as you enter the door.  You tell him that you need a weapon to kill Kibbles the Evil Dragon. He laughs and says, 'Mah boy! Killing Justin is what all true warriors strive for! But you can't do it with any of my weapons, you need Atari, the magic sword that lies in the cave east of the forest.  Many have tried to get it, but all have failed as it is guarded by the evil wizard Gwonam!  If you're looking to fight Gwonam, I can make you an axe, but you need to bring me iron ore, wood, and some gold for my troubles.'  You then decide to head into the forest to seek out the materials for the blacksmith")
         
        
        elif direction=="north":
            print ("You walk up the gates of the King Adam Mehter's castle, the guards stop and ask you to state your business, you tell them that you want to rescue Princess Cherry.  They laugh and tell you that you should probably obtain a weapon first, you head back to the center of town")

        elif direction=="east":
            print ("You head into the residential district of town, a few huts line the streets, but there isn't much else of note here, you decide to head back to the center of town")

        elif direction=="south":
            print ("You head deep into the forest")
            place=forest

        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")

        elif direction=="inventory":
            print (items)
    
        elif direction=="look":
            print ("You're located in the small town of Jersey, here you see a blacksmith shop to the west, the king's castle to the north, houses to the east, and the town's exit to the forest to your south")

        elif "use" in direction:
            print ("You have nothing to use")

        elif "search" in direction:
            print ("There's nothing of importance to search")

        else:
            print ("Please type a command")

    while place==forest:

        direction=input("What would you like to do?\n")

        if direction=="west":
            print ("You head into the mine")
            place=mine
        
        elif direction=="south":
            print ("The mountains look too treacherous to try and pass through.  It might not hurt to try and look for that man though.")

        elif direction=="east":
            if "battleaxe" in items:
                print ("You head into Gwonam's Lair")
                place=lair
            else:
                print ("it's not a good idea to go to Gwonam's lair unprotected")

        elif direction=="north":
            print ("You head back to Jersey")
            place=town

        elif direction=="look":
            print ("You are at the center of a vast forest, surrounded by many tall trees, you could defintiely obtain some wood from some of them, but you would need the proper tools.  To your west lies a mine, to your south a group of impassable mountains, but you can hear a person in the distance, to your east lies the evil gwonam's lair, and to the north lies Jersey")

        elif "use" in direction:
            if "pickaxe" in direction:
                if "iron ore" in items:
                    if "man" or "person" in direction:
                        print ("The man looks at the pickaxe with sorrow and tells you that this was his brothers pickaxe, he offers you his saw for it and you accept.")
                        items.append ("saw")
                        items.remove ("pickaxe")
                        
            if "saw" in direction:
                if "saw" in items:
                    if "tree" in direction:
                        print ("you use the saw to cut some wood off of a nearby tree")
                        items.append ("wood")
                else:
                   print ("you can't use that")
                
                        
        elif direction=="inventory":
            print (items)

        elif "search" in direction:
            if direction== "search person":
                print ("You find the man, he appears to be a lumberjack and is carrying a large saw.  You tell him about your quest and the items you are looking for.  He directs you to the mine for the iron ore and tells you that he's always wanted to be a miner like his brother.  He tells you that his brother is in the mines right now if you should need any help.")
            else:
                print ("You can't search for that")
        
        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")


    while place==mine:

        direction=input("What would you like to do?\n")

        if direction=="west":
            print ("The cavern is too dark to travel down, you head back to the center of the mine")

        elif direction=="east":
            print ("You head back to the forest")
            place=forest
    
        elif direction=="south":
            print ("You are at a desposit of rich iron, this is perfect for the blacksmith, the only problem is you don't have a way to mine it")

        elif direction=="north":
            print ("You are in a small cavern with a dead body on the floor, you are not sure how he died.  You see a pickaxe underneath him and a bag around his waist")

        elif direction=="look":
            print ("You find yourself in the center of a large mine.  To your east lies the exit back to the forest, to your north lies a cavern with a dead body, to your south lies an iron deposit, and to your west lies a very dark cavern.")

        elif "search" in direction:
            if "body" in direction:
                if "pickaxe" not in items:
                    print ("You take the pickaxe and the bag which contained 3 Gold Pieces")
                    items.append ("pickaxe")
                    items.append ("3 Gold Pieces")
            else:
                print ("You cannot search that")

        elif "use" in direction:
            if "pickaxe" in direction:
                if "pickaxe" in items:
                    if "iron" in direction:
                        print ("You use the pickaxe to mine the iron ore")
                        items.append ("iron ore")
            else:
                print ("You cannot use that")

        elif direction=="inventory":
           print (items)

        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")


    while place==lair:

        direction=input("What would you like to do?\n")

        if direction=="west":
            print ("You head back into the forest")
            place==forest

        elif direction=="south":
            if "Atari" not in items:
                print ("You see Gwoman's scary looking 'Faces of Evil' paintings hanging on the wall, you head down the corridor and come face to face with the evil wizard.  He screams 'Zreep!' and tries to attack you with a magic spell!")

                action=input("What will you do?")
            
                if "axe" in action:
                    print ("You manage to dodge the spell, you lunge forward and cut off Gwonam's head.  He screams 'Squadalllllllllahhhhhhhhhhh' as he dies as if it's some sort of spell, but who cares, you did it!  Atari the magic sword hangs on the wall, it's finally yours now, time to fight Justin!")
                    items.append ("Atari")
                    print ("You head back to the center of the lair")
                    place=lair

                else:
                    print ("You get hit with the spell, you can hear Gwonam laughing as you feel immense pain and everything begins to fade to black.  You realize that this is it, and you do not feel bad about losing your own life, only that you could not save Princess Cherry.  Here is where your Adventure ends.")
                    game==lose
                    place=dead

        elif direction=="east":
                (cell)=1
                locked=2
                (cell)=locked
                while cell==locked:
                    action=input("What would you like to do?")
                    if "key" in action:
                        if "key in inventory:
                            cell=1
                            print ("You unlock the cell door and rescue the Princess!  She hugs you and thanks you for saving her.  You escort her back to Jolt and become a legendary hero!")
                            game=win
                            place=dead
                        else:
                            print("You don't have the key")
                else: print ("You head down a long hallway and reach a jail cell holding Princess Catherine, she screams to you for help, but the door is locked.  She tells you the key is in the room and guarded by Justin the Evil Dragon.  You promise her that you will save her and head back to the center of the lair")

        elif direction=="north":
            if "Atari" in items:
                print ("You run down the hallway and reach a giant room.  You finally come face to face with the Evil Justin the Dragon.  He towers over you and begins to roar when you enter the room.  He charges at you and breathes fire in your direction")
                action=input("What will you do?")
                if "Atari" or "Sword" in action:
                    print ("You unsheate Atari, it begins to glow and surrounds you with a protective shield.  The fire bounces off the shield and you swing it at Justin's neck, decapitating him.  You did it!  You pick up the key on the table that Justin was guarding, now all that's left is to save the Princess!")
                    items.append ("key")
                else:
                    print ("You get hit by the fire, it scorches your body and you feel excrutiating pain all over.  A deep sense of regret fills you as you realize that you were unable to save Princess Catheine.  Kibbles picks you up and beings to devour you whole.  Your adventure ends here.")
                    game=lose
                    place=dead

            else:
                print ("You do not have Atari yet, it would be suicide to try and fight Justin")

        elif direction=="look":
            print ("You are at the center of the evil Gwonam's lair.  To the north lies Justin the evil dragon, to the south lies Gwonam's room, to the east lies the jail, and to the west is the exit back to the forest.")

        elif "use" in direction:
            print ("I would worry about using that now, let's just try and rescue the Princess")

        elif direction=="commands":
            print ("type the commands north, south, east, and west in order to navigate,type the command use followed by the item name to use an item, type the command inventory to look at the items in your posession, type the command look to look around you, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")

        elif direction=="inventory":
            print(items)

        elif "search" in direction:
            print ("Let's not search that now, we have to save the Princess!")

while game==lose:
    print ("Thank you for playing, Try again and see if you can rescue Princess Cherry!")
    game=99
    input("Press enter to exit the program")

while game==win:
    print ("Congratulations! You beat the Adventure game! Thank you for playing!")
    game=99
    input("Press enter to exit the program")
    credits(4)
    time.sleep(10)
    quit()
    
