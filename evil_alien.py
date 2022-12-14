#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Evil Alien
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 8 of Computer Space Games, and it a python3 translation.

This is another guessing game, though this game is played on a three dimensional space. Thus the player needs
to guess the x,y,and z co-ordinates of the enemy. If the player misses, a hint is provided.

The size of the space is determined by the difficulty, and the number of goes is determined by the size of the screen

"""

instructions = "Somewhere beneath you, in the deepest, blackest space,\n"
instructions = "{}lurks Elron, the Evil Alient. You have managed to \n".format(instructions)
instructions = "{}deactivate all but his short range weapons but he can\n".format(instructions)
instructions = "{}still make his ship invisible. You know he is somewhere\n".format(instructions)
instructions = "{}within the three-dimensional grid you can see on your\n".format(instructions)
instructions = "{}ship's screen (see below), but where?\n".format(instructions)
instructions = "{}You have four space bombs. Each one can be exploded at\n".format(instructions)
instructions = "{}a position in the grid specified by three numbers between\n".format(instructions)
instructions = "{}0 and 9, which your computer will ask you for. Can you\n".format(instructions)
instructions = "{}blast the Evil Elron out of space before he creeps up\n".format(instructions)
instructions = "{}and captures you?".format(instructions)

#Compares the shot to the enemy's position
def check_coordinates(less,greater,comp_val,play_val):

	result = ""

	if play_val>comp_val:
		result = greater
	elif play_val<comp_val:
		result = less

	return result

#Checks to see the shot compared to the position of the enemy
def compare_shot(x,y,z,x1,y1,d1):

	result = "The shot was"

	#The player hit the enemy
	if (x==x1) and (y==y1) and (z==d1):
		return True

	#Provides the player with a hint as to where they went wrong
	result = "{}{}".format(result,check_coordinates(" north"," south",x,x1))
	result = "{}{}".format(result,check_coordinates(" east"," west",y,y1))
	result = "{}{}".format(result,check_coordinates(" too far"," not far enough",z,d1))

	print(result)
	return False

#Gets the player's input, and calculates the number of shots
def player_shots(x,y,z,goes):

	print("{} {} {}".format(x,y,z))

	for l in range(goes):

		#The player's turn
		x1 = util.get_num_input("X Position",0,9)
		y1 = util.get_num_input("Y Position",0,9)
		d1 = util.get_num_input("Distance",0,9)

		#Checks to see how good the player's guess is
		if compare_shot(x,y,z,x1,y1,d1):
			return True

	return False

def main_game():

	#Sets the difficulty of the game. The number of goes is determined by the size
	#of the game area
	difficulty = util.get_num_input("Please enter the difficulty",1,9)
	difficulty += 1
	size = difficulty*3
	goes = difficulty

	if goes<3:
		goes = 3

	#Sets the position of the evil alien
	x = randint(0,size)
	y = randint(0,size)
	z = randint(0,size)

	#Starts the game
	hit = player_shots(x,y,z,goes)

	#Prints out the result
	if hit:
		print("BOOOM!!!! You got him!!!")
	else:
		print("Your time has run out!!")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Evil Alien",sys.modules[__name__])