#!/usr/bin/env python3

import util
import time
import starship_takeoff
import intergalactic_games
import evil_alien
import beat_bug
import moonlander
import monsters_galacticon
import alien_sniper

#Function that displays the games available, and allows the user to select them
def select_game():
	
	selecting = True

	#Creates a while loops to hold the menu to select the game
	while (selecting):
		util.clear_screen()
		print("1) Starship Takeoff")
		print("2) Intergalactic Games")
		print("3) Evil Alien")
		print("4) Beat the Bug Eyes")
		print("5) Moonlander")
		print("6) Monsters of Galacticon")
		print("7) Alien Snipers")
		print("8) Asteroid Belt *")
		print("9) Trip into the Future *")
		print("10) Death Valley *")
		print("11) Space Mines *")
		print("12) Space Rescue *")
		print("13) Touchdown *")
		print("X) Exit")
		print()
		print("Games marked with an asterix '*' haven't been incorporated yet")
		print()
		response = input()

		#Executes the players selection
		if response.upper() == 'X':

			#Ends the program by letting it run out
			selecting = False

		elif response == "1":
			start_game("Starship Takeoff",starship_takeoff)
		elif response == "2":
			start_game("Intergalactic Games",intergalactic_games)
		elif response == "3":
			start_game("Evil Alien",evil_alien)
		elif response == "4":
			start_game("Beat the Bug Eyes",beat_bug)
		elif response == "5":
			start_game("Moonlander",moonlander)	
		elif response == "6":
			start_game("Monsters of Galacticon",monsters_galacticon)
		elif response == "7":
			start_game("Alien Snipers",alien_sniper)		
		else:
			print("You have entered an incorrect option")
			time.sleep(5)

#Start game function. Takes the input to be used, and the title of the game
def start_game(title,game):

	answer,replay = util.start_game(title)

	#Displays the instructions that are stored at the beginning of the game selected
	if answer:
		util.clear_screen()
		print(game.instructions)
		input("Press Enter to Continue: ")

	#Loop for replaying the game
	while replay:
		game.main_game()
		replay = util.play_again(replay)

if __name__ == '__main__':
	select_game()

