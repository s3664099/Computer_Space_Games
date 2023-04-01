#!/usr/bin/env python3

import loader
import sys
import util
import time
from random import randint

"""
Title: Alien Sniper
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 19 November 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 16 of Computer Space Games, and it a python3 translation.

In this game you have to solve a problem in a set amount of time. A letter is selected and you have to
guess what letter is x number of spaces past the letter. The game runs for 10 turns, and every answer you guess
your score increases by one.

I have managed to replicate the inkey, which I have placed in util, however I won't be going back and updating the
other programs I have already finished.
"""

instructions = "You are the captain of an interstellar cruiser which, through damage to one\n"
instructions = "{}of its hyperspace motors, has strayed into a forbidden area. Alien sniper\n".format(instructions)
instructions = "{}ships are attacking you and, to make things worse, are using a jamming\n".format(instructions)
instructions = "{}device on your radar which  makes it give false readings. Luckily your\n".format(instructions)
instructions = "{}computer knows a code which yoy can use to work out the correct locations\n".format(instructions)
instructions = "{}of the enemy ships. But you must be quick - they don't stay in one place\n".format(instructions)
instructions = "{}for long!\n".format(instructions)
instructions = "{}Your computer will print a letter (the false enemy location) and a code\n".format(instructions)
instructions = "{}number. You must think through the alphabet by that number of letters and\n".format(instructions)
instructions = "{}type in the letter you get to. EG: for M 4 you must type Q, and for C 2\n".format(instructions)
instructions = "{}you must type E and so on. Typing in a letter automatically triggers off\n".format(instructions)
instructions = "{}your laser gun, so if your letter is correct you'll score a hit. You can\n".format(instructions)
instructions = "{}choose the difficulty of each game. This is a number between 1 and 10\n".format(instructions)
instructions = "{}and is the maximum number of letters to be added on each time. You\n".format(instructions)
instructions = "{}get 10 alien snipers each game. See how many you can hit".format(instructions)

#Sets the details for the current alien
def set_alien(difficulty):

	alien = randint(0,25)
	code = randint(0,difficulty)
	coded_alien = alien+code
	coded_alien = coded_alien%25

	return alien,coded_alien,code

#main game loop
def main_game():

	#Gets the difficulty	
	difficulty = util.get_num_input("Difficulty",1,10)
	score = 0

	#Sets the time delay
	time_delay = 5+(difficulty/2)
	alphabet = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"

	#Loops through the number of aliens encountered
	for x in range(10):

		#Generates the alien and the code
		alien, coded_alien,code = set_alien(difficulty)

		#Displays the alien and the code
		time.sleep(1)
		util.clear_screen()
		print("{} {}".format(alphabet[alien],code))

		#Retrieves the player's guess
		guess = util.inkey(time_delay)

		#Checks if it was a hit
		if (guess == alphabet[coded_alien]):
			print("\nYou hit")
			score +=1

	#Displays the final score
	print("Score: {}/10".format(score))
	time.sleep(1)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Alien Snipers",sys.modules[__name__])