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
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 30 of Computer Space Games, and it a python3 translation.



"""

instructions = "Ace space pilot, Captain Flash, is sitting next to you as you take the final part of your\n"
instructions = "{}Advanced Spacecraft Handling Test (Part III). Your lightweight, two-person landing craft is\n".format(instructions)
instructions = "{}rapidly approaching the Moon's surface. Your velocity must be also zero as you touch down.\n".format(instructions)
instructions = "{}Deftly you control the thrust, pressing A to increase it and D to decrease it, watching\n".format(instructions)
instructions = "{}your progress on the screen at all time. If you use too much thrust you will begin to go\n".format(instructions)
instructions = "{}back up again. Too little and you will make a new crater in the Moon. Can you impress\n".format(instructions)
instructions = "{}Captain Flash with your skill?".format(instructions)

def main_game():

	graphics.set_caption("Touchdown")
	

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Touchdown",sys.modules[__name__])