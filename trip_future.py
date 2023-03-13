#!/usr/bin/env python3

import loader
import sys
import util
import math
from random import randint

"""
Title: 
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 12 of Computer Space Games, and it a python3 translation.

The goal of this game is for the player to escape from the planet. The player knows the gravity of the planet
but not the weight of the ship. The player needs to guess the force to be applied to launch the ship. If the
force is too high or too low, the ship won't budge, but the player will be informed if it is too high or too
low.

The player gets 10 shots to escape from the planet.

"""

instructions = "Imagine you are in a spaceship travelling nearly as fast as light. Strangely\n"
instructions = "{}time is passing more slowly inside your spaceship than outside. So, having \n".format(instructions)
instructions = "{}set off on a long, fast space trip, you can return to Earth further in the \n".format(instructions)
instructions = "{}future than the clocks inside your ship indicate.\n".format(instructions)
instructions = "{}In this game, your computer tells you how many years must elapse on Earth\n".format(instructions)
instructions = "{}before you return. You then decide the length of your trip (in light\n".format(instructions)
instructions = "{}years) and the spee of your shop (in a fraction of the speed of light)\n".format(instructions)
instructions = "{}in order to achieve this. Take care not too far too slowly or you will\n".format(instructions)
instructions = "{}die of old age on the way.".format(instructions)

def main_game():
	time = randint(25,124)

	print("You wish to return {} years in the future".format(time))
	print()
	velocity = util.get_float_input("Speed of shop",0,1)
	distance = util.get_number_input("Distance of Trip")

	time_one = distance/velocity
	time_two = time_one/math.sqrt(1-velocity*velocity)

	print("The trip took {} years".format(time_one))
	print("And arrived {} years in the future".format(int(time_two)))

	if (time_one>50):
		print("You died on the way")
	elif (abs(time-time_two)<=5):
		print("You arrived on time")
	else:
		print("Not Even Close")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])