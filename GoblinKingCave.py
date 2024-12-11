victoryText = r'''
 ___      ___ ___  ________ _________  ________  ________      ___    ___ 
|\  \    /  /|\  \|\   ____\\___   ___\\   __  \|\   __  \    |\  \  /  /|
\ \  \  /  / | \  \ \  \___\|___ \  \_\ \  \|\  \ \  \|\  \   \ \  \/  / /
 \ \  \/  / / \ \  \ \  \       \ \  \ \ \  \\\  \ \   _  _\   \ \    / / 
  \ \    / /   \ \  \ \  \____   \ \  \ \ \  \\\  \ \  \\  \|   \/  /  /  
   \ \__/ /     \ \__\ \_______\  \ \__\ \ \_______\ \__\\ _\ __/  / /    
    \|__|/       \|__|\|_______|   \|__|  \|_______|\|__|\|__|\___/ /     
                                                             \|___|/      
'''
gameOverText = r'''
 ________  ________  _____ ______   _______           ________  ___      ___ _______   ________     
|\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \   
 \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__       \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__|/       \|_______|\|__|\|__|
'''
hasWeapon = False
isCursed = False
health = 100

print(r'''⠀⠀⠀⠀⠀⠀
*******************************************************************************
███████████████████████████████████
███████████████████████████████████
███████████████████████████████████
█████████████▒▒▒▒▒▒▒▒▒█████████████
█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████
███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████
█████▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█████
████▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒████
███▒▒▒▒██████▒▒▒▒▒▒▒▒▒██████▒▒▒▒███
███▒▒▒███▐▀███▒▒▒▒▒▒▒███▀▌███▒▒▒███
███▒▒▒██▄▐▌▄███▒▒▒▒▒███▄▐▌▄██▒▒▒███
███▒▒▒▒██▌███▒▒▒█▒█▒▒▒███▐██▒▒▒▒███
██▒▒▒▒▒▒███▒▒▒▒██▒██▒▒▒▒███▒▒▒▒▒▒██
█▒▒▒▒▒▒▒▒█▒▒▒▒██▒▒▒██▒▒▒▒█▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒█▒▒█▒▒▒▒██▒▒▒▒▒██▒▒▒▒█▒▒█▒▒▒▒█
██▒▒▒█▒▒█▒▒▒▒█▒██▒██▒█▒▒▒▒█▒▒█▒▒▒██
███▒█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒███
█████▒▒█▒▒▒▐███████████▌▒▒▒█▒▒█████
███████▒▒▒▐█▀██▀███▀██▀█▌▒▒▒███████
███████▒▒▒▒█▐██▐███▌██▌█▒▒▒▒███████
███████▒▒▒▒▒▐▒▒▐▒▒▒▌▒▒▌▒▒▒▒▒███████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
█████████▒▒█▒█▒▒▒█▒▒▒█▒█▒▒█████████
█████████▒██▒█▒▒▒█▒▒▒█▒██▒█████████
██████████████▒▒███▒▒██████████████
██████████████▒█████▒██████████████
███████████████████████████████████
███████████████████████████████████
*******************************************************************************
''')
print("Welcome to Goblin King Cave.")
print("Your quest is to find the treasure.")
print("You've entered a creepy dungeon in search of treasure.\nYour path of entrance has been sealed, the only way "
      "out is forward.")
print("You've reached a fork in the path...")

decision1 = input("Will you go left or right? \n")

if decision1.lower() == "left":
    print("You found a secret water passage")
    decision2 = input("Only way forward is to swim. dive or retreat? \n")
    if decision2.lower() == "dive":
        print("You swim through and reach an open area.\nYou see a skeleton holding a sword.")
        decision3 = input("I may be smart to protect yourself...\nTake or leave? \n")
        if decision3.lower() == "take":
            print("You take up the sword, and feel a strange tingling sensation in you hands.\nSharp spikes jet out of "
                  "swords hilt and peirce hand.\nYou feel an immense pain travel up your arm and pass out.")
            hasWeapon = True
            print("You awake from a voice, 'Kill!, Kill!!, Kill!!!'.\nAnd you can not put the sword down.")
            print("You have acquired the Curse Blade,\nYou feel immense power, like your being compelled but drained, "
                  "like half you life force is gone")
            isCursed = True
            if isCursed:
                health -= 50
            print("Inner thought: 'Lets hurry and find this treasure!'")
            print("You continue forward further into the cave...")
        else:
            print("You continue forward further into the cave...")
            print("Inner thought: 'Something tells me something was up with that sword, bad juju'")
            print("Inner thought: 'Lets hurry and find this treasure!'")

        print("You find three paths...")
        decision4 = input("Will you go left, right or center? \n")
        if decision4.lower() == "left":
            if hasWeapon:
                print("You run into an ambush and the Goblin King the keeper of the cave\nHe takes back his sword "
                      "and kills you in one swing!")
                print("Since you were cursed by the sword, if the keeper of the cave defeats you in battle, "
                      "you trade places")
                print("You are now the new Goblin King, keeper of the cave")
                print(gameOverText)
            else:
                print("You run into an ambush and the Goblin King\nHe hits you and kills you in one swing!")
                print(gameOverText)
        elif decision4.lower() == "center":
            if hasWeapon:
                print("You found the treasure.\nYou use the potion inside to remove the curse.")
                health += 50
                isCursed = False
                print("The Goblin King enters and you battle to the death and Win.")
                print("You exit the cave with the treasure, and they will for ever speak your name in glory.")
                print(victoryText)
            else:
                print("You found the treasure.\nYou use the potion inside to remove the curse.")
                print("The Goblin King enters and you battle to the death and Lose. He eats you and grows stronger.")
                print(gameOverText)
        elif decision4.lower() == "right":
            if hasWeapon:
                print("You exit the cave with nothing but the sword.\nIt compels you to kill everyone in town and "
                      "return to the cave near the water!")
                print(gameOverText)
            else:
                print("You exit the cave and leave empty handed\nNO GLORY and live out your days as humble "
                      "farmer\nthen killed by some mad man wielding that weird sword")
                print(gameOverText)
        else:
            print("You chose to do nothing and a gob of goblins found you feasted on your bones.")


    else:
        print("You ran into a gob of goblins and they feasted on your bones.")
        print(gameOverText)
else:
    print("You ran into a gob of goblins and they feasted on your bones.")
    print(gameOverText)

