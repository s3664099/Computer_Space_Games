# Computer Space Games

These files are a translation of an old programming book from the 1980s
called 'Computer Battle Games'. The idea was to teach children programming
using basic. Due to multiple different systems back in the day there were marks
advising of when the code needed to be changed for a specific machine.

I used a Commodore 64 for my machine.

However, I have decided to translate them into modern computer languages. Initially
I was going to do it using C++, Java, and Python however issues arose that made me
decide to just use python, due to things that don't exist in modern langauges and would
require threading to be able to execute properly (though not necessarily in the same way
as it was executed on the older computers)

[The book is now available online to download for free](https://drive.google.com/file/d/0Bxv0SsvibDMTNlMwTi1PTlVxc2M/view?resourcekey=0-kaU6eyAmIVhT3_H8RkHfHA)

## Executing the Games

A *shebang* has been included in the files so that they can be executed directly from the
command line. However, for that to work you will need to make the file executable. Since these
games run only on Linux, you will need to go to the directory on the command line and type

*chmod +x [game name].py*

To execute the game *Missile!*, PyGame needs to be installed.

## Issues

I have included the section from Computer Battle Games as the Get/Inkey is also an issue with these games.

<ins>Get/Inkey</ins>

Basic had two means of getting a user input, the *input* command, which would block the
program from going further until an input (followed by pressing Enter), and it would 
have the prompt '?'

The other means would be either *Get* or *inkey* depending on the computer you were using. This
command would check for a keypress *at a given instance* and if there was one, then it would be recorded.
It would be a means of getting rid of the annoying '?', or as a means of timing the input, except
only one character would be recorded. Normally it would for a loop, and once keypress is detected, it
would escape from the loop.

The main idea is that the *get* or *inkey* would not block the program from executing while waiting
for the user to press a key (or series of keys)

**Update**
[I have found this link](https://stackoverflow.com/questions/60896414/python-preferably-3-equivalent-to-inkey)
I have yet to try it out though.
No, it didn't work as I hoped it would.

**Keyboard**
There is a python package called [keyboard](https://pypi.org/project/keyboard/). This has a number of functions
one of them involving detecting key presses. However, there are a couple of problems:

1) When the key is pressed, it still appears on the screen (it doesn't with Inkey)
2) It will detect specific keys as opposed to general keypresses (though I believe it can detect that)
3) It will detect a key, not a combination of keys (though I looks like that is possible as well)
4) You require root privileges to access the command, otherwise an error will be thrown

I attempted to use it on one of the games, but unfortunately it didn't work as expected.

19 November 2022
I have found a python3 [import](https://pypi.org/project/pynput/) that seems to work is required. However
the problem is that the keys that have been pressed are then stored in a buffer, and released when an input is
requested.

There is also an issue with the buffer being recorded at the beginning, so I've had to skip the first turn 
for Asteroid Belt.

**Pygame**
This is also a solution, but it adds a lot more to the game than otherwise, and adds a lot of time to coding these
games.

## Games

**Starship Takeoff**
This is a simply guessing game. The player needs to guess a correct number to win. If the number is too high or
Too low, then a message advising the player is given. The player gets 10 guesses to succeed.

**Intergalactic Games**
This is another guessing game, though it is trickier than the previous since the calculations are somewhat complex.
Also, the player needs to enter two sets of numbers as opposed to one.

**Evil Alien**
Basically another guessing game where you have to guess the position of the enemy. In this one there are three numbers
you have to guess, representing a three dimensional grid.

**Beat the Bug Eyes**
This game will display a pair of eyes at one of 4 positions on the screen. The player needs to select which one of the
positions it is (by pressing 1,2,3 or 4). Any other key, or the wrong position, is a miss. The correct position adds
one to the score.

**Moonlander**
Basically a game where you need to land a ship on the moon. You control the amount of fuel you burn, and you can't land too fast, otherwise you will crash.

**Monsters of Galacticon**
You are confronted with one of four monsters, and have to chose a weapon with which to attack. After some complicated
calcuations, the result of the attack is displayed. You start with a specific number of men, and once all men are dead
you lose, unless you beat off all 8 monsters.

**Alien Snipers**
You need to solve a series of puzzles which are times. You are presented with a letter, and a number, and have to guess
the letter that is the exact number of numbers past the letter. The guesses are timed, and once you press the key
the guess is recorded. A score is kept.

**Asteroid Belt**
Another guessing game. A number of stars are placed on the screen, and you need to guess the number of stars in
a limited amount of time. I probably didn't need to use the inkey function though, just the timed input. However
I'll leave it as is.

**Trip into the Future**
This is a mathematical problem. You have to travel so many years into the future but you have to do it so that you
don't die. You are given a number of years you need to travel, and you need to do that in less than 50 year, and
arrive within 5 years of the target. You need to select a speed (a percentage of the speed of light) and a distance.
If the calculation is off, you lose, otherwise you win.

**Death Valley**
This is more of an arcade game where you have to maneuver your ship through a valley whose walls are regularly
changing. I have managed to hack together an inkey function that seems to work, though you require the getkey 
python library to run this game.

## Updates
**29 October 2022**
Created the initial folder to hold the contents on the game

**30 October 2022**
reconfigured the loader program to hold the start game function, and to call that start game function if the game
is launched outside of the loader

**31 October 2022**
Finished the first game. Created a shell for the new games.

**1st November 2022**
Added Intergalactic Games.

**6th November 2022**
Added Evil Alien, and also a function in util for getting a player input between two numbers

**8th November 2022**
Added Beat the Bug Eyes to the list of games

**13th November 2022**
Added Moonlander to the games

**17th November 2022**
Added a rough draft of Monsters of Galacticon

**19th November 2022**
Completed and tidied up Monsters of Galacticon.
Added Alien Snipers.
Also added an inkey function - [here](https://pypi.org/project/pynput/)

**20th November 2022**
Added Asteroid Belt.

## TO DO
Add Difficulty to Beat the Bug Eyes which means more positions, and more bugs (at the same time) and shorter time
