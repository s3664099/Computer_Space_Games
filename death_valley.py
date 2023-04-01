#!/usr/bin/env python3

import loader
import sys
import util
import time
from random import randint
from getkey import getkey

"""
Title: Death Valley
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 22 of Computer Space Games, and it a python3 translation.

This is a game that involves you making your way through a narrow valley and avoiding colliding with the sides. You
need to go a set number of spaces to escape, and if you do then you win.

I managed to get an inkey working using the getkey and that there is a while loop that pauses the game for around half
a second.

To change how long the game lasts you adjust the 'max_goes' variable. The speed variable increases/slows down the game

One trick would be to make the valley narrower.

"""

instructions = "There is only one way to escape the forces of the evil Dissectitrons. You will\n"
instructions = "{}have to steel every nerve and fly your single-seater Speed Dart along the\n".format(instructions)
instructions = "{}jagged, bottomless ravine known as Death Valley.\n".format(instructions)
instructions = "{}Your computer will ask you for the width of the valley. Try 15 first and the\n".format(instructions)
instructions = "{}work your way down - 8 is quite difficult. Steer your Speed Dart by pressing\n".format(instructions)
instructions = "{}Q to go left and P to go right, and see if you can make it safely through Death\n".format(instructions)
instructions = "{}Valley.\n".format(instructions)

def main_game():

	no_goes = 0
	max_goes = 200
	width = util.get_num_input("Width",1,40)
	width = int(width/2)
	margin = 10
	left_distance = width
	right_distance = width	
	game = True
	speed = 0.5

	#Main Gam Loop
	while game:

		#Builds and displays the current row
		margin,left_distance,right_distance = change_size(margin,left_distance,right_distance)
		display = "{}I".format(display_screen(margin,""))
		display = "{}*".format(display_screen(left_distance,display))
		display = "{}I".format(display_screen(right_distance,display))
		print(display)

		#Gets the player's input
		start_time = time.time()
		while (time.time() - start_time<speed):
			key = getkey(blocking=False)

			if (key == "q"):
				left_distance -=1
				right_distance +=1
			elif (key == "p"):
				left_distance +=1
				right_distance -=1

		#Checks if you have either crashed or escaped Death Valley
		if (left_distance <1) or (right_distance <1):
			print("You crashed into the wall and disintegrated")
			game = False
		else:
			no_goes +=1
			if no_goes == max_goes:
				print("Well done, you made it through Death Valley")
				game=False

#Sets up the game
def change_size(margin,left_distance,right_distance):

	correct = False

	#Determines whether the valley curves
	while not correct:
		distance = randint(-1,1)

		if (left_distance+distance>-1) or (right_distance+distance<21):
			correct = True

	#Adjusts the distances
	margin = margin+distance
	left_distance = left_distance-distance
	right_distance = right_distance+distance

	return margin,left_distance,right_distance

def display_screen(number,display):

	if number>0:
		for x in range(number):
			display+=" "

	return display

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Death Valley",sys.modules[__name__])