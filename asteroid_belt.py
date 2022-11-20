#!/usr/bin/env python3

import loader
import sys
import util
import time
from random import randint

"""
Title: Asteroid Belt
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 20 November 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 18 of Computer Space Games, and it a python3 translation.

With this game the player needs to guess the size of the asteroid within a certain amount of time. A correct
guess increased the score, while an invalid input, or no input, reduces the score (but not the kill count).
This game also uses the inkey function I created, however there are issues with the buffer, so that needs to
be cleared, which is why there is an extra shot, that is skipped at the beginning

"""

instructions = "You are on a trip through the Asteroid Belt. To avoid crashing\n"
instructions = "{}into the asteroids, you must destroy them and the force required\n".format(instructions)
instructions = "{}for doing this depends on their size.\n".format(instructions)
instructions = "{}Asteroids appear on your computer screen as groups of stars. To\n".format(instructions)
instructions = "{}destroy them you must press the number key corresponding to the\n".format(instructions)
instructions = "{}number of the stars. Be prepared - asteroids come at you think\n".format(instructions)
instructions = "{}and fast.\n".format(instructions)

#Displays the asteroids
def display(size):

		#Generates the position and size
		across = randint(0,18)
		down = randint(0,12)
		across_space = ""
		asteroid = ""

		#Scrolls down
		for d in range(down):
			print()

		#Builds the tab
		for a in range(across):
			across_space = "{} ".format(across_space)

		#Cycles the number of asteroids
		for n in range(size):

			if n != 1 and n != 4 and n != 7:
				asteroid = "{}*".format(asteroid)
			else:
				asteroid = "{}{}*".format(asteroid,across_space)

		#Displays the asteroids
		print(asteroid)

#Checks the player's response
def check_response(response,size,score,killed):

	try:
		#The size is correct
		if int(response) == size:
			print("\nYou destroyed it!")

			#Score is generated, and a kill number is increased
			score +=size
			killed += 1

		#The size is not correct
		elif int(response)>size:
			print("\nToo strong")
		else:
			print("\nNot strong enough")

	#Invalid, or no, input recorded
	except:
		print("\nYou crashed into the asteroid")
		score -= size

	return score,killed

#Main game loops
def main_game():

	#Resets the score
	score = 0
	killed = 0
	skip = True

	#Number of turns (one extra due to the inkey)
	for x in range(11):

		#Sets the screen
		util.clear_screen()
		size = randint(1,9)

		#Displays the asteroid and gets a reponse
		display(size)
		response = util.inkey(4)

		#The first one is skipped to clear the buffer
		#Otherwise checks the response and calculates the score
		if not skip:
			score,killed = check_response(response,size,score,killed)
			time.sleep(3)
		else:
			skip = False

	print("You destroyed {} out of 10 asteroids for a score of {}".format(killed, score))


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Asteroid Belt",sys.modules[__name__])