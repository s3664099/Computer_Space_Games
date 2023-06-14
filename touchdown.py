#!/usr/bin/env python3

import loader
import sys
import util
import pygame
import graphics
from random import randint

"""
Title: Touchdown
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 13 June 2023
Source: https://drive.google.com/file/d/part of your /view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 30 of Computer Space Games, and it a python3 translation.



"""

instructions = "Ace space pilot, Captain Flash, is sitting next to you as you take the final\n"
instructions = "{}part of your Advanced Spacecraft Handling Test (Part III). Your lightweight,\n".format(instructions)
instructions = "{}two-person landing craft is rapidly approaching the Moon's surface. Your\n".format(instructions)
instructions = "{}velocity must be also zero as you touch down. Deftly you control the thrust,\n".format(instructions)
instructions = "{}pressing A to increase it and D to decrease it, watching your progress on\n".format(instructions)
instructions = "{}the screen at all time. If you use too much thrust you will begin to go back\n".format(instructions)
instructions = "{}up again. Too little and you will make a new crater in the Moon. Can you\n".format(instructions)
instructions = "{}impress Captain Flash with your skill?".format(instructions)

def main_game():

	graphics.set_caption("Touchdown")
	display = graphics.display_screen()

	height = 100
	fuel = 100
	thrust = 0
	

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Touchdown",sys.modules[__name__])