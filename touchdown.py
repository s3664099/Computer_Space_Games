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

	#Display Star Background for the display
	#Display rugged ground at the bottom

	#Sets up the main variables
	height = 100
	fuel = 100
	thrust = 0
	velocity = 5+randint(1,10)
	gravity = (randint(1,40)+40)/100

	#Main Game Loop
	while True:

		display.fill([0,0,0])
		graphics.display_stat("Gravity: {}".format(gravity),display,24,100,20)

		display_stats(display,fuel,velocity,height,thrust)

		pygame.display.update()


	#Displays the ship at the top
	#Checks for a key press to increase or decrease thrust

	#The calculation for each move
	#V1=V-T/20+G - Change in velocity
	#F=F-T/10 - change in fuel
	#H1=H-(V+V1)/10 Change in height

	#If H<0 then landed
	#IF (V+V1)<8 Check for a safe landing

	#If H>100 then lost in space

#Updates the values of the game statistics
def display_stats(display,fuel,velocity,height,thrust):

	graphics.display_stat("Fuel:",display,24,150,20)
	graphics.draw_bar(display,[20,200],[20+fuel,200])
	
	graphics.display_stat("Vel:",display,24,250,20)
	graphics.draw_bar(display,[20,300],[20+velocity,300])
	
	graphics.display_stat("Height:",display,24,350,20)
	graphics.draw_bar(display,[20,400],[20+height,400])
	
	graphics.display_stat("Thrust:",display,24,450,20)
	graphics.draw_bar(display,[20,500],[20+thrust,500])





#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Touchdown",sys.modules[__name__])