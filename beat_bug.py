#!/usr/bin/env python3

import loader
import sys
import util
import time
from random import randint

"""
Title: Beat the Bug Eyes
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 8 November 2022
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 10 of Computer Space Games, and it a python3 translation.

This is a bit trickier in that bug eyes will appear at random positions on the screen, and you need to guess
which position it is (there are 4 positions, labelled 1 to 4) within a time limit. If you guess correctly, you
get a point. This game also differs in that if you press an incorrect key, that being any key other than 1 to 4
that is counted as a miss.

The input is timed, and you need to press enter after selecting the number.

The player gets 10 shots.

The book had a challange of adding more bugs, and more positions. I haven't made any further additions to this game
but will add a TODO in case I decide to revisit it.

"""

instructions = "You're trapped! Everywhere you turn you catch a glimps of the steely\n"
instructions = "{}cold light of a space bug's eyes before it slithers down behind a rock\n".format(instructions)
instructions = "{}again. Slowly the bugs edge towards you. hemming you in, waiting for a\n".format(instructions)
instructions = "{}chance to bind you in their sticky web-like extrusions. Luckily you have\n".format(instructions)
instructions = "{}your proton blaster with you.\n".format(instructions)
instructions = "{}The bug eyes pop up in four different places on your screen and these\n".format(instructions)
instructions = "{}correspond to keys 1 to 4. Press the correct key while the bug's eyes are\n".format(instructions)
instructions = "{}on the screen and you will black it There are 10 bugs in all - the more\n".format(instructions)
instructions = "{}you blast, the greater your chance of escape.\n".format(instructions)

def display_eyes(down,across,eyes_symbol):

	for x in range(down):
		print()

	eyes = ""

	for x in range(across):
		eyes = "{}  ".format(eyes)

	print("{}{}".format(eyes,eyes_symbol))

def display_top(score,delay):

		util.clear_screen()
		print("Score: {}".format(score))
		time.sleep(delay)

def main_game():
	score = 0

	for x in range(10):

		delay = randint(3,5)
		display_top(score,delay)

		position = randint(1,4)

		down = 0
		across = 0

		if position == 1:
			down = 5
			across = 1
		elif position == 2:
			down = 1
			across = 9
		elif position == 3:
			down = 5
			across = 18
		else:
			down = 10
			across = 7

		display_eyes(down,across,"OO")

		response = util.input_with_timeout_no_comment("",3)

		try:
			if int(response) == position:
				score += 1
				display_top(score,0)
				display_eyes(down,across,"**")
				time.sleep(2)			
		except:
			pass

	print("You blasted {} bugs".format(score))

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Beat the Bug Eyes",sys.modules[__name__])