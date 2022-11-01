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

This is another guessing game, where you have to guess the angle and velocity to successfully launch a satellite.
You are provided with a height that you have to reach, and then asked to enter an angle and a velocity. If you
guess correctly, you win, otherwise you are provided with a hint for the next shot. You have eight chances in which
to successfully launch the satellite.

"""

instructions = "There is fierce competition among the world's TV companies\n"
instructions = "{}for exclusive coverage of the First Intergalactic Games.\n".format(instructions)
instructions = "{}Everything depends on which company wins the race to put\n".format(instructions)
instructions = "{}a satellite into orbit at the right height.".format(instructions)
instructions = "{}You are the Engineer in charge of the launch for New\n".format(instructions)
instructions = "{}Century TV. The crucial decisions about the angle and\n".format(instructions)
instructions = "{}speed of the launching rocket rests on your shoulders.\n".format(instructions)
instructions = "{}Can you do it?".format(instructions)

#This function generates a random height, and informs the player of the height required
def get_height():

	height = randint(1,100)

	print("You must launch a satellite to a height of {}".format(height))

	return height

#This function retrieves a numerical input.
def get_input(text,max_value):

	correct = False

	#Loops until a correct input is recieved.
	while not correct:

		try:
			response = int(input(text))

			#If the input is outside of the range, the player is informed
			if response>max_value:
				print("Please enter a value less than {}".format(max_value))
			elif response<0:
				print("Please enter a value greater than 0")
			else:
				correct = True

		#Catches the error if the input is not a number
		except:
			print("Please enter a number")

	return response

#Function that calculates the shot
def calculate_shot(angle,height,velocity):

	angle = angle-math.atan(height/3)*(180/3.14159)
	velocity = velocity-(3000*math.sqrt(height+1/height))

	return check_result(angle,velocity)

#Checks the result of the shot
def check_result(angle,velocity):

	result = ""

	#Shot is successful
	if abs(angle)<2 and abs(velocity)<100:
		result = True
	else:

		#Shot is not successful, so hits are provided
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

	#Gets the height required, and sets the success flag
	height = get_height()
	success = False

	#Set variables to calculate the bonus
	bonus = 0
	bonus_calculation = 0

	for x in range(8):

	 	#Gets the players input
		angle = get_input("Enter Angle (0-90): ",90)
		velocity = get_input("Enter Speed (0-40000): ",40000)

		#Gets the result of the shot
		result = calculate_shot(angle,height,velocity)

		if result == True:
			success = True
			bonus_calculation = x
			break
		else:
			print(result)

	if success:
		print("You've done it. NCTV wins - thanks to you")

		#Calculates the bonus earned this round
		bonus_earned = bonus+(1000/bonus_calculation)
		bonus = bonus + bonus_earned

		print("You have earned a bonus of ${}0".format(bonus_earned))
		print("Your total bonus is ${}0".format(bonus))
	else:
		print("You've failed. You're fired like a programmer at Twitter")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Intergalactic Games",sys.modules[__name__])