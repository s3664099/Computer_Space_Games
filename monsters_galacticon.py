#!/usr/bin/env python3

import loader
import sys
import util
import random

"""
Title: Monsters of Galacticon
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 20 October 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 14 of Computer Space Games, and it a python3 translation.

"""

instructions = "Landing on Galacticon was easy - but no one warned you that some of the nastiest\n"
instructions = "{}monsters in the known universe are to be found there.\n".format(instructions)
instructions = "{}As each monster threatens, you must choose one of your weapons - a ray gun, \n".format(instructions)
instructions = "{}a trypton blaster or a sword laser - to use against it. Can you make\n".format(instructions)
instructions = "{}the right choices? If so you may live to conquer Galacticon.\n".format(instructions)

def main_game():

	no_monsters = 4
	no_group = 5

	monsters = ["Sulfacidor","Flamgondar","Balnolotin","Golandor"]
	random.shuffle(monsters)

	util.clear_screen()
	for x in range(8):

		correct = False
		select_no = 0
		attacking = random.randint(0,no_monsters-1)
		print("No of soldiers: {}\n\n".format(no_group))
		print("Monster coming")
		print("It's a {}".format(monsters[attacking]))

		while correct == False:

			selection = input("Which weapon ( R, S or T): ").upper()

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
				print("Please enter R,S, or T")

		x_val = 0
		y_val = 0

		select_no = select_no-(81+(attacking+1))

		if select_no>3:
			x_val = -1

		if select_no>6:
			y_val = -1

		select_no = abs(select_no+(3*x_val)+(3*y_val))

		if select_no == 2:
			print("You've killed it")
		elif select_no == 3:
			print("No effect")
			if random.randint(0,10)>5:
				print("You angered the {} and it has eaten one of your group".format(monsters[attacking]))
				no_group -=1
		else:
			print("No use, it's eaten one of your group")
			no_group -=1

		if no_group<0:
			break

	if no_group>0:
		print("You have survived to conquer Galacticon")
	else:
		print("You're all dead")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Monsters of Galacticon",sys.modules[__name__])