from os import system
from inputimeout import inputimeout, TimeoutOccurred

"""
Title: Util.py
Author: David Sarkies
Version: 1.1
Date: 26/1/2021

This file holds functions that are likely to be used across multiple
programs. The clear screen fuction operates under unix-like operating systems.

TimeoutExpired, alarm_handler, and input_with_timeout are fuctions that are
designed to limit the amount of time the user has to input a response. Unfortunately
the user will need to press enter to record the response.

The following package is required:
https://pypi.org/project/inputimeout/

Update 7/2/2021
Added a second input function that doesn't display 'too late'

Update 22/10/2022
Added a few more since, including a start game function that pretty much does what
all the games do at the beginning.
Added another input with timeout function to return true or false
"""

#Performs the start game functions.
def start_game(title):

	#Sets the replay flag
	replay = True
	answer = False
	clear_screen()
	print(title)

	answer = ask_instructions()

	return answer,replay

def clear_screen():
	_ = system('clear')

#Exception that is called when the time limit expires
class TimeoutExpired(Exception):
	print("Time Out")

def alarm_handler(signum, frame):
	raise TimeoutExpired

#Timeout function. Takes a prompt and a time in seconds
#For the timeout
def input_with_timeout(prompt, timeout):
	
	keypress = ""

	#Waits for the user input
	try:
		keypress = inputimeout(prompt, timeout)

	#If the time limit expires an error is thrown.
	except TimeoutOccurred:
		print("Too late!")
	return keypress

def input_with_timeout_02(prompt,timeout):

	try:
		inputimeout(prompt,timeout)

	except:
		return False
	return True

def input_with_timeout_no_comment(prompt, timeout):

	keypress = ""

	#Waits for the user input
	try:
		keypress = inputimeout(prompt, timeout)

	#If the time limit expires an error is thrown.
	except TimeoutOccurred:
		pass
	return keypress

#Handles asking the player a yes or no question
def yes_or_no(answer):

	correct = False

	#Loop while waiting for the correct answer
	while not correct:

		print()	
		reply = input()

		#Sets the flag as correct, and the player will replay
		if reply.upper() == "Y":
			answer = True
			correct = True

		#Sets the flag as correct and the player won't replay
		elif reply.upper() == "N":
			answer = False
			correct = True

		#Response for incorrect answer
		else:
			print()
			print("Please enter Y or N")
			print()
	return answer

#Function to handle query whether player wishes to replay the game
def play_again(replay):

	print()
	print("Do you wish to play again (Y/N) ?")

	replay = yes_or_no(replay)
	clear_screen()

	return replay

#Asks if the player wants instructions
def ask_instructions():

	#Asks player if they would like instructions
	answer = False

	print("Would you like instructions (Y/N) ?")
		
	#Calls the yes or no function
	answer = yes_or_no(answer)

	return answer

#Function that asks the player for a number between a min and max
#Checks if the response falls within the listed parameters and returns if it does
def get_num_input(description,minimum,maximum):

	#Sets query and correct flag
	correct = False
	query = -1

	#Loop while the response is incorrect
	while not correct:

		query = input("{} ({}-{}):".format(description,minimum,maximum))

		try:
			query = int(query)
			#Does it fall within the parameters
			if query > maximum:
				print("Please enter a number less than {}".format(maximum))
			elif query < minimum:
				print("Please enter a number greater than {}".format(minimum))
			else:
				correct = True
		#Is it a number
		except:
			print("Please enter a number between {} and {}".format(minimum,maximum))

	return query

