#!/usr/bin/env python3

import loader
import sys
import util
import math
from random import randint

"""
Title: Intergalactic Games
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 31 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 6 of Computer Space Games, and it a python3 translation.


"""

instructions = "There is fierce competition among the world's TV companies\n"
instructions = "{}for exclusive coverage of the First Intergalactic Games.\n".format(instructions)
instructions = "{}Everything depends on which company wins the race to put\n".format(instructions)
instructions = "{}a satellite into orbit at the right height.".format(instructions)
instructions = "{}You are the Engineer in charge of the launch for New\n".format(instructions)
instructions = "{}Century TV. The crucial decisions about the angle and\n".format(instructions)
instructions = "{}speed of the launching rocket rests on your shoulders.\n".format(instructions)
instructions = "{}Can you do it?".format(instructions)

def get_height():

	height = randint(1,100)

	print("You must launch a satellite to a height of {}".format(height))

	return height

def get_input(text,max_value):

	correct = False

	while not correct:

		try:
			response = int(input(text))

			if response>max_value:
				print("Please enter a value less than {}".format(max_value))
			elif response<0:
				print("Please enter a value greater than 0")
			else:
				correct = True
		except:
			print("Please enter a number")

	return response

def calculate_shot(angle,height,velocity):

	angle = angle-math.atan(height/3)*(180/3.14159)
	velocity = velocity-(3000*math.sqrt(height+1/height))

	print(angle)
	print(velocity)

	return check_result(angle,velocity)

def check_result(angle,velocity):

	result = ""

	if abs(angle)<2 and abs(velocity)<100:
		result = True
	else:
		if angle<-2:
			result = "Too Shallow"
		elif angle>2:
			result = "Too Steep"
		if velocity<-100:
			result = "{} Too Slow".format(result)
		elif velocity>100:
			result = "{} Too Fast".format(result)

	return result

def main_game():

	height = get_height()
	success = False

	for x in range(8):

		angle = get_input("Enter Angle (0-90): ",90)
		velocity = get_input("Enter Speed (0-40000): ",40000)

		result = calculate_shot(angle,height,velocity)

		if result == True:
			success = True
			break
		else:
			print(result)

	if success:
		print("You've done it. NCTV wins - thanks to you")
	else:
		print("You've failed. You're fired like a programmer at Twitter")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Intergalactic Games",sys.modules[__name__])