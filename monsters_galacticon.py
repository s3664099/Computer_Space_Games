#!/usr/bin/env python3

import loader
import sys
import util
import random

"""
Title: Monsters of Galacticon
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 1
Date: 19 November 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 14 of Computer Space Games, and it a python3 translation.

The game shuffles and produces a random monster, and you have three options to kill it. The game then performs
some obscure calculations to produce a number between 1 and 3, which provides a response to the attack (or rather)
the defense. The player has a number of men, and 8 monsters to face. If the number of men goes below 0, then it is
game over.

The problem here is that what I could suggests that you can add more monsters, it is difficult to determine if
by increasing the number of monsters will break the calculations. However, it is possible to make it harder by
reducing the number of men, increasing the number of monsters that need to be fought, and making it more likely
that you will anger the monster. Apparently there is a forth way, but I can't see it off the top of my head

"""

instructions = "Landing on Galacticon was easy - but no one warned you that some of the nastiest\n"
instructions = "{}monsters in the known universe are to be found there.\n".format(instructions)
instructions = "{}As each monster threatens, you must choose one of your weapons - a ray gun, \n".format(instructions)
instructions = "{}a trypton blaster or a sword laser - to use against it. Can you make\n".format(instructions)
instructions = "{}the right choices? If so you may live to conquer Galacticon.\n".format(instructions)

#Retrieves the player input
def get_input():

	#Sets the variable
	select_no = 0
	correct = False

	#Loop to retrieve an input, and to prevent an incorrect input
	#Sets the input to upper case
	while correct == False:

		selection = input("Which weapon ( R, S or T): ").upper()

		#Converts the selection into the ASCII no for the C64 (upon which the calculations were based)
		#Also sets the correct value to escape the loop
		if selection == 'R':
			select_no = 82
			correct = True
		elif selection == 'S':
			select_no = 83
			correct = True
		elif selection == 'T':
			select_no = 84
			correct = True
		else:

			#Incorrect entry
			print("Please enter R,S, or T")

	return select_no

#Function to calculate whether the attack was successful
def calculate_hit(select_no,attacking,no_group):

	#Place holders
	x_val = 0
	y_val = 0

	select_no = select_no-(81+(attacking+1))

	#The original code involved some boolean operators that I haven't seen in
	#Modern languages, so I have translated them as follows
	if select_no>3:
		x_val = -1

	if select_no>6:
		y_val = -1

	select_no = abs(select_no+(3*x_val)+(3*y_val))

	return select_no

#Displays the results of the attacks. Takes the selection, the numbers in the group, and the monster
def display_result(select_no,no_group,monster):

	if select_no == 2:
		print("You've killed it")

	elif select_no == 3:
		print("No effect")

		#A no effect will have a further random respose
		if random.randint(0,10)>5:
			print("You angered the {} and it has eaten one of your group".format(monster))
			no_group -=1

	else:
		print("No use, it's eaten one of your group")
		no_group -=1	

	return no_group


#Main game loop
def main_game():

	#Sets the initial variables
	no_monsters = 4
	no_group = 5

	#Creates an array to hold the monsters, and to shuffle the array
	monsters = ["Sulfacidor","Flamgondar","Balnolotin","Golandor"]
	random.shuffle(monsters)

	util.clear_screen()

	#The player gets 8 turns
	for x in range(8):

		#Selects a random monster and informs the player
		attacking = random.randint(0,no_monsters-1)
		print("No of soldiers: {}\n\n".format(no_group))
		print("Monster coming")
		print("It's a {}".format(monsters[attacking]))

		#Calls the function to get the input
		select_no = get_input()

		#Calculates the result of the hit
		select_no = calculate_hit(select_no,attacking,no_group)
		no_group = display_result(select_no,no_group,monsters[attacking])

		#If no men are left, the game is over
		if no_group<0:
			break

	#Gave over - are there any survivors?
	if no_group>0:
		print("You have survived to conquer Galacticon")
	else:
		print("You're all dead")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Monsters of Galacticon",sys.modules[__name__])