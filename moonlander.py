#!/usr/bin/env python3

import loader
import sys
import util

"""
Title: Moonlander
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1.0
Date: 13 November 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 12 of Computer Space Games, and it a python3 translation.

I noticed that no random calculations are used in this game, but the goal of the game is that they player
needs to land safely on the moon. This is done by burning fuel and that descending. The thing is that
the velocity on touch down must be under a certain number, otherwise the player will crash.

"""

instructions = "You are in controls of a lunar module which is taking a small team of astronauts\n"
instructions = "{}down to the moon's surface. In order to land safely you must slow down your\n".format(instructions)
instructions = "{}descent but that takes fuel and you only have a limited supply.\n".format(instructions)
instructions = "{}Your computer will tell you your starting height, speed and fuel supply and ask\n".format(instructions)
instructions = "{}how much fuel you wish to burn. It will then work out your new and and speed. A\n".format(instructions)
instructions = "{}burn of 5 will keep your speed constant. A higher number will reduce it. Try to\n".format(instructions)
instructions = "{}have your speed as close to zero as you can when you land. Can you land safely\n".format(instructions)
instructions = "{}on the moon?".format(instructions)

#Display Stats
def display_stats(time,height,velocity,fuel):
	print("Time: {} Height: {}".format(time,height))
	print("Vel: {} Fuel: {}".format(velocity,fuel))

#Main Game
def main_game():

	#Sets game stats
	time = 0
	height = 500
	velocity = 50
	fuel = 150

	#Main loop
	while height>0:

		#Clears the screen and displays the main stats
		util.clear_screen()
		display_stats(time,height,velocity,fuel)

		burn = fuel

		#Checks to see how much fuel is left, and requests player input
		if fuel >0:
			burn = util.get_num_input("Burn",0,30)

			#Cannot burn more fuel than is in the tank
			if burn > fuel:
				burn = fuel

		#Calculates velocity
		burn_vel = velocity - burn + 5
		fuel -= burn

		#Checks how close to the ground the player is
		if ((burn_vel+velocity)/2) <= height:
			height -= (burn_vel+velocity)/2
			time += 1
			velocity = burn_vel
		else:
			height -= (burn_vel+velocity)/2
			burn_vel = velocity+((5-burn)*(height/velocity))

	#Calculates if the player crashed or not	
	if burn_vel > 5:
		print("You crashed - all dead!")
	elif burn_vel > 1:
		print("OK - but some injuries")
	else:
		print("Good Landing")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Moonlander",sys.modules[__name__])