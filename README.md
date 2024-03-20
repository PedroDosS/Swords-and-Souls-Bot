# Swords and Souls Bot

![Screenshot](https://github.com/PedroDosS/Swords-and-Souls-Bot/assets/90741843/8f26c13b-30a9-42a6-b4f6-514ab25f2d72)

https://github.com/PedroDosS/Swords-and-Souls-Bot/assets/90741843/c286fa22-158a-4a64-85e6-2685e1845796

# About:
Swords and Souls is a 2015 RPG where the player must defeat waves of enemies in a 
battle arena. To progress further, the player can level up various combat-related 
skills in 5 different minigames. In the defense minigame, apples are thrown at the 
player from all directions, which the player must block. This bot automatically plays
this minigame by capturing the screen, detecting where the apples are, and blocking them.
This bot is able to play the minigame infinitely, reaching a score of over 100,000
before it was stopped manually.

# How to Run:
- Download block.py, CoordsCache.txt, coords.py
- By default, the game screen should be placed in the top-left corner of your screen
- To move or resize the game screen (not recommended):
  - Adjust game_screen and origin in block.py to the desired location of the screen
  - Delete CoordsCache.txt
  - Run coords.py to regenerate CoordsCache.txt
- Run block.py to start the bot
- Right-click to exit the program

# Requirements:
- [Bluemaxima's Flashpoint](https://flashpointarchive.org/downloads): A Flash emulator used to run the game
- [Python 3](https://www.python.org/downloads/): Used to run the bot script
- [Pillow](https://pillow.readthedocs.io/en/stable/): Image processing library used to capture the screen
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/): Input library used to control the mouse
- [Mouse](https://pypi.org/project/mouse/): Input library used to detect user input
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Required for PyAutoGUI
