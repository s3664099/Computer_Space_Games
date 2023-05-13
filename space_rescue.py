#!/usr/bin/env python3

import loader
import sys
import util
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

instructions = "You are about to embark on a mission to a distant planet in urgent need\n"
instructions = "{}of medical supplies. You must first ready your ship for the trip by\n".format(instructions)
instructions = "{}allocating some of the ship's energy to the engines, shields, and\n".format(instructions)
instructions = "{}life support. You are then put to sleep for the main part of the trip,\n".format(instructions)
instructions = "{}after which you will get a report of the events on the way. You must\n".format(instructions)
instructions = "{}then land on the planet ...".format(instructions)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])