#!/usr/bin/env python3

import loader
import sys
import util
import pygame
import graphics
import time
from random import randint

"""
Title: Touchdown
Author: Daniel Isaaman & Jenny Tyler
Translator: David Sarkies
Version: 0
Date: 13 June 2023
Source: https://drive.google.com/file/d/part of your /view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA
This game can be found on page 30 of Computer Space Games, and it a python3 translation.

Lunar Lander Icon: <a href="https://www.flaticon.com/free-icons/lander" title="lander icons">Lander icons created by imaginationlol - Flaticon</a>

"""

instructions = "Ace space pilot, Captain Flash, is sitting next to you as you take the final\n"
instructions = "{}part of your Advanced Spacecraft Handling Test (Part III). Your lightweight,\n".format(instructions)
instructions = "{}two-person landing craft is rapidly approaching the Moon's surface. Your\n".format(instructions)
instructions = "{}velocity must be also zero as you touch down. Deftly you control the thrust,\n".format(instructions)
instructions = "{}pressing A to increase it and D to decrease it, watching your progress on\n".format(instructions)
instructions = "{}the screen at all time. If you use too much thrust you will begin to go back\n".format(instructions)
instructions = "{}up again. Too little and you will make a new crater in the Moon. Can you\n".format(instructions)
instructions = "{}impress Captain Flash with your skill?".format(instructions)

def main_game():

	graphics.set_caption("Touchdown")
	display = graphics.display_screen()

	#Display rugged ground at the bottom

	#Sets up the main variables
	height = 100
	fuel = 100
	thrust = 0
	velocity = 5+randint(1,10)
	gravity = (randint(1,40)+40)/100
	landerImg = graphics.create_icon("lander.png")
	landerImg = graphics.transform_icon(landerImg)
	landerImgUp = graphics.create_icon("lander_thrstup.png")
	landerImgUp = graphics.transform_icon(landerImgUp)
	landerImgDwn = graphics.create_icon("lander_thrstdwn.png")
	landerImgDwn = graphics.transform_icon(landerImgDwn)
	lander_x = graphics.get_width()/2
	lander_y = 0
	result = 0
	stars = display_stars()

	#Main Game Loop
	while result == 0:

		display.fill([0,0,0])
		graphics.display_stat("Gravity: {}".format(gravity),display,24,100,20)

		display_stats(display,fuel,velocity,height,thrust)

		if thrust < -8:
			graphics.display_icon(landerImgUp,lander_x,lander_y,display)
		elif thrust > 8:
			graphics.display_icon(landerImgDwn,lander_x,lander_y,display)
		else:
			graphics.display_icon(landerImg,lander_x,lander_y,display)

		graphics.draw_stars(display,stars)
		graphics.draw_ground(display)

		pygame.display.update()

		if (fuel > 0):
			thrust = check_keypress(thrust)
			vel_tmp = velocity-(thrust/(20+gravity)) 	#Change in Velocity
			fuel = fuel-abs(thrust/10) 					#Change in fuel
		else:
			thrust = 0
			vel_tmp = velocity

		if (fuel<0):
			fuel = 0

		height_tmp = height-((velocity+vel_tmp)/10) #Change in heigh

		result = check_result(height,velocity+vel_tmp)

		#Sets new values and updates position of lander if no result
		if (result == 0):
			velocity = vel_tmp
			height = height_tmp
			lander_y = (100-height)*4

			#Delay
			time.sleep(0.25)

	display_result(result, display)
	pygame.time.wait(1000)
	pygame.quit()


def check_result(height,velocity):

	result = 0

	if (height<0):
		result = 1
		if (velocity>8):
			result = 2
	elif (height>100):
		result = 3

	return result

#Checks for a key press to increase or decrease thrust
def check_keypress(thrust):

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				thrust -= 4
			if event.key == pygame.K_DOWN:
				thrust += 4	

	return thrust

def display_result(result, display):

	if result == 1:
		graphics.message_display("You landed safely",display,40,"centre")
	elif result == 2:
		graphics.message_display("You landed too fast and crashed",display,40,"centre")
	else:
		graphics.message_display("Lost in space",display,40,"centre")

def display_stars():

	stars = []

	for x in range(100):

		x_pos = randint(100,800)
		y_pos = randint(0,800)
		stars.append([x_pos,y_pos])

	return stars

#Updates the values of the game statistics
def display_stats(display,fuel,velocity,height,thrust):

	graphics.display_stat("Fuel:",display,24,150,20)
	graphics.draw_bar(display,[20,200],[20+fuel,200])
	
	graphics.display_stat("Vel:",display,24,250,20)
	graphics.draw_bar(display,[50,300],[50+velocity,300])
	
	graphics.display_stat("Height:",display,24,350,20)
	graphics.draw_bar(display,[20,400],[20+height,400])
	
	graphics.display_stat("Thrust:",display,24,450,20)
	graphics.draw_bar(display,[50,500],[50+thrust,500])

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Touchdown",sys.modules[__name__])