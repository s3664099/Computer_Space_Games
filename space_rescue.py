#!/usr/bin/env python3

import loader
import sys
import util
import math
import time
from random import randint

"""
Title: 
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 13 May 2023
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 26 of Computer Space Games, and it a python3 translation.

The goal of this game is for the player to escape from the planet. The player knows the gravity of the planet
but not the weight of the ship. The player needs to guess the force to be applied to launch the ship. If the
force is too high or too low, the ship won't budge, but the player will be informed if it is too high or too
low.

The player gets 10 shots to escape from the planet.

"""

instructions = "You are about to embark on a mission to a distant planet in urgent need\n"
instructions = "{}of medical supplies. You must first ready your ship for the trip by\n".format(instructions)
instructions = "{}allocating some of the ship's energy to the engines, shields, and\n".format(instructions)
instructions = "{}life support. You are then put to sleep for the main part of the trip,\n".format(instructions)
instructions = "{}after which you will get a report of the events on the way. You must\n".format(instructions)
instructions = "{}then land on the planet ...".format(instructions)

#Sets the variables for the game
def set_variables():
	distance = randint(101,900)
	energy = randint(401,800)
	time = int(distance/math.sqrt(energy/5) + 0.5)

	return distance,energy,time

#Displays the stats
def display_stats(distance,energy,time):
	print("The planet is {} units away".format(distance))
	print("You have {} units of energy".format(energy))
	print("And a time limit of {} days".format(time))

#Get details of the flight
def get_flight(energy):

	sufficient_power = False

	while not sufficient_power:
		print("\nEnergy Distribution")
		power = util.get_number_input("to engines")
		life_support = util.get_number_input("to life support")
		shields = util.get_number_input("to shields")

		if(power+life_support+shields>energy):
			print("You don't have enough energy")
		else:
			sufficient_power = True

	return power,life_support,shields	

#Determines the events that may occur during the trip
def events(shields,distance,velocity,life_support):

	#Determines a number of possible events
	for i in range(1, randint(6, 10)):

		#Generates a random potential event - 1/2
		rand_num = randint(0, 10)

		if (rand_num == 0):
			print("Asteroid Storm - Shields Damaged")
			shields = shields - 20 - randint(1,40)
		elif (rand_num == 1):
			print("Computer Breakdown - delay in repairing")
			distance = distance + randint(1,20)
		elif (rand_num == 2):
			print("Engine trouble - must slow down")
			velocity = velocity - 0.5
		elif (rand_num == 3):
			print("X-Ray damage - life support damaged")
			life_support = life_support - randint(1,40)
		else:
			pass

		time.sleep(1)

	return shields,distance,velocity,life_support

#Determines the player's arrival status
def arrival(shields,life_support,velocity,time,eta):

	arrived_safely = True

	if shields<0:
		print("Shields destroyed - you were blown up")
		arrived_safely = False
	elif life_support <=0:
		print("Life support inactive - you are dead")
		arrived_safely = False
	elif velocity <= 0:
		print("Engines are non-functional")
		arrived_safely = False
	elif eta>time:
		print("You took too long about it")
		arrived_safely = False

	return arrived_safely

#Generates the stats of the planet
def planet_stats(value):

	stat = "High"

	if value < 8:
		stat = "Low"
	elif value <12:
		stat = "Medium"

	return value,stat

#Function for landing on the planet
def planet(excess_power):

	sufficient_power = False

	while not sufficient_power:

		boosters = util.get_number_input("How much energy to boosters")
		heat_shields = util.get_number_input("How much energy to heat shields")

		if boosters+heat_shields > excess_power:
			print("You do not have enough power")
		else:
			sufficient_power = True

	return boosters,heat_shields

#Determines the results of landing on the planet
def landing_result(boosters,heat_shields,gravity,atmosphere):

	landed_safely = True

	if boosters >= gravity*10:
		print("You made a new crater")
		landed_safely = False
	elif heat_shields >= atmosphere*10:
		print("You made a wonderful shooting star")
		landed_safely = False

	return landed_safely

def main_game():

	util.clear_screen()
	distance,energy,time_to_planet = set_variables()
	display_stats(distance,energy,time_to_planet)

	power,life_support,shields = get_flight(energy)

	excess_power = energy-power-life_support-shields
	velocity = int(math.sqrt(power))
	eta = int(distance/velocity)

	util.clear_screen()

	print("Your velocity is {}".format(velocity))
	print("You have an ETA of {} days".format(eta))

	shields,distance,velocity,life_support = events(shields,distance,velocity,life_support)

	time.sleep(5)

	#Determines Arrival States
	eta = int(distance/velocity)
	print("Arrived in {} days".format(eta))

	#If the player arrived safely
	if (arrival(shields,life_support,velocity,time_to_planet,eta)):

		gravity,grav = planet_stats(randint(5,15))
		atmosphere,atmos = planet_stats(randint(5,15))

		print("\nYou are now orbitting the planet")
		print("Surplus Energy = {}".format(excess_power))
		print("Gravity is {}".format(grav))
		print("Atmosphere is {}".format(atmos))

		boosters,heat_shields = planet(excess_power)

		if (landing_result(boosters,heat_shields,gravity,atmosphere)):

			print("You landed successfully - well done")

			if (excess_power-heat_shields-boosters<=25):
				print("Pity you don't have enough energy to open the door")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Starship Takeoff",sys.modules[__name__])