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

**Pygame**
This is also a solution, but it adds a lot more to the game than otherwise, and adds a lot of time to coding these
games.

## Games

**Starship Takeoff**
This is a simply guessing game. The player needs to guess a correct number to win. If the number is too high or
Too low, then a message advising the player is given. The player gets 10 guesses to succeed.

##Updates
**29 October 2022**
Created the initial folder to hold the contents on the game

**30 October 2022**
reconfigured the loader program to hold the start game function, and to call that start game function if the game
is launched outside of the loader

**31 October 2022**
Finished the first game. Created a shell for the new games.