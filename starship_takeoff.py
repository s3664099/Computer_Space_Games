#!/usr/bin/env python3

import loader
import sys

"""
Title: Battle at Traitor's Castle
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 12 of Computer Battle Games, and it a python3 translation.

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

def main_game():
	print("Hello")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])