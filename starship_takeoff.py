#!/usr/bin/env python3

import loader
import sys
from random import randint

"""
Title: Battle at Traitor's Castle
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 12 of Computer Battle Games, and it a python3 translation.

The goal of this game is for the player to escape from the planet. The player knows the gravity of the planet
but not the weight of the ship. The player needs to guess the force to be applied to launch the ship. If the
force is too high or too low, the ship won't budge, but the player will be informed if it is too high or too
low.

The player gets 10 shots to escape from the planet.

"""

instructions = "Starship Takeoff\n"
instructions = "{}================\n".format(instructions)
instructions = "{}You are a starship captain. You have crashed your shop on a\n".format(instructions)
instructions = "{}strange planet and must take off again quickly in the alien\n".format(instructions)
instructions = "{}ship you have captured. The ship's computer tells you the\n".format(instructions)
instructions = "{}gravity on the planet. You must guess the force required for a\n".format(instructions)
instructions = "{}successful take off. If you guess too low, the ship will not lift\n".format(instructions)
instructions = "{}off the ground. If you guess too high, the ship's fail-safe\n".format(instructions)
instructions = "{}mechanism comes into operation to prevent it being burnt\n".format(instructions)
instructions = "{}up. if you are still on the planet after ten tries, the aliens\n".format(instructions)
instructions = "{}will capture you\n\n".format(instructions)

#Sets the parameters for the game
def set_parameters():
	gravity = randint(0,20)
	weight = randint(0,40)
	esc_vel = gravity * weight

	#Player knows the gravity, but not the weight of the ship
	print("Gravity: {}".format(gravity))

	return esc_vel

#Checks the force the player uses to escape
def check_force(force, esc_vel):

	escaped = False
	result = ""

	#Compares the force with the escape velocity
	if force>esc_vel:
		result = "The force is too high. Fail-safe mechanism kicks in."
	elif force<esc_vel:
		result = "The force is too Low. The ship shudders but fails to take off."
	else:
		escaped = True

	return escaped, result

#Function to handle the input
def get_force(esc_vel):

	correct = False

	while not correct:

		force = input("Type in force: ")

		#The input has to be a number
		try:
			force = int(force)
			correct = True
		except:
			print("Please enter a number")

	#Checks if the player escaped
	escaped,result = check_force(force, esc_vel)

	return escaped,result


#Function that runs the main game
def main_game():

	esc_vel = set_parameters()

	#Player gets 10 guesses
	for x in range (10):

		escaped,result = get_force(esc_vel)		

		#If successful
		if escaped:
			break
		else:
			print("{} Try again".format(result))

	if escaped:
		print("Congratulations, you managed to escape the planet")
	else:
		print("Unfortunately you were too slow. The Aliens got you")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])