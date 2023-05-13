#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Space Mines
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 10 April 2023
Source: https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 24 of Computer Space Games, and it a python3 translation.

The goal of this game is for the player to escape from the planet. The player knows the gravity of the planet
but not the weight of the ship. The player needs to guess the force to be applied to launch the ship. If the
force is too high or too low, the ship won't budge, but the player will be informed if it is too high or too
low.

The player gets 10 shots to escape from the planet.

"""

instructions = "You are the newly elected lead of a mining colony on the planet Asteron. All\n"
instructions = "{}decisions concerning the sale of ore to Intergalactic Traders. food purchase\n".format(instructions)
instructions = "{}and sale, and purchase of mines are made by you. Can you keep the people\n".format(instructions)
instructions = "{}satisfied and sirvive your 10 years in office or will life in the colony\n".format(instructions)
instructions = "{}end in disaster under your rule?".format(instructions)

#Sets the variables for the start of the game
ore_stored = 0
satisfaction = 1
year = 1
mines = randint(5,7)
people = randint(40,99)
cash = randint(10,59)
food = randint(80,119)
ore_mine = randint(40,119)

#Resets for a new game
def reset():
	global ore_stored,satisfaction,year,mines,people,food,ore_mine

	ore_stored = 0
	satisfaction = 1
	year = 1
	mines = randint(5,7)
	people = randint(40,99)
	food = randint(80,119)
	ore_mine = randint(40,119)

#Displays the stats for the game
def display_stats(ore_price,mine_price):
	stats = "Year: {}\n\nThere are {} people in the colony.\nYou have {} mines and ${}\n".format(year,people,mines,cash)
	stats = "{}satisfaction Factor: {}\n\nMines produced {} tons each\n".format(stats,satisfaction,ore_mine)
	stats = "{}Ore in store: {} tons\n\nSelling\n".format(stats,ore_stored)
	stats = "{}Ore selling price: ${}\nMine selling price: ${}\n".format(stats,ore_price,mine_price)
	return stats

#Function for selling stuff
def to_sell(query,item_max,cash,price):

	to_sell = util.get_num_input(query,0,item_max)
	item_max -= to_sell
	cash += to_sell*price

	return item_max,cash

#Function for buying food and calculating satisfaction based on food purchased
def buy_food(satisfaction,cash,people):

		to_buy = util.get_num_input("How much to spend on food (approx 100 each)",0,cash)
		cash -= to_buy

		if (to_buy/people>120):
			satisfaction += 0.1
		elif (to_buy/people<80):
			satisfaction -= 0.2

		return satisfaction

#Function for buying mines
def buy_mines(mines,cash,buysell_price_mines):

	to_buy = util.get_num_input("\nHow many more mines to buy?",0,int(buysell_price_mines/cash))
	mines += to_buy
	cash -= to_buy*buysell_price_mines

	return mines,cash

#Function to calculate the results of the turn's decisions
def turn_calculation():

	global satisfaction,people,ore_mine
	result = ""

	if (satisfaction<0.6):
		return "The people are unhappy with your rule and have tossed you out",False

	if (people/mines<10):
		return "You've overworked everyone and you have been tossed out",False
		
	if (satisfaction>1.1):
		ore_mine += randint(1,20)
		people += randint(1,10)
	elif (satisfaction<0.9):
		ore_mine -= randint(1,20)
		people -= randint(1,20)

	if (people<30):
		return "There is not enough people left in your colony",False

	if (randint(1,100)<=1):
		result = "Radioactive leak ... many die"
		people = people/2

	if (ore_mine>150):
		result = "{}\nMarket Glut - price drops".format(result)
		ore_mine = ore_mine/2

	return result,True

def main_game():

	global ore_stored
	global cash
	global mines
	global satisfaction
	global ore_mine
	global people
	global year
	playing = True
	play_again = True

	while play_again:
		while playing:
		
			util.clear_screen()
		
			#Sets the buy/sell price for the year
			buysell_price_mines = randint(2000,3999)
			buysell_price_ore = randint(7,19)
		
			#Updates the storage
			ore_stored = ore_mine * mines
			print(display_stats(buysell_price_ore,buysell_price_mines))
	
			#Selling Phase
			ore_stored,cash = to_sell("How much ore would you like to sell? ",ore_stored,cash,buysell_price_ore)
			mines,cash = to_sell("How many mines would you like to sell? ",mines,cash,buysell_price_mines)

			#Buying Phase
			print("\n\nYou have ${} cash on hand\n\n".format(cash))
			print("Buying\n")
			satisfaction = buy_food(satisfaction,cash,people)
			mines,cash = buy_mines(mines,cash,buysell_price_mines)

			result,playing = turn_calculation()
		
			year +=1

			if (year>10):
				result = "You have satisfied your term in office"
				playing = False

			print(result)

		play_again = play_again(False)

		if play_again == True:
			reset()

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Space Mines",sys.modules[__name__])