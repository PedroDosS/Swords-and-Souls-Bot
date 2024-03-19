# Swords-and-Souls-Bot
A Python script to automatically play the defense training minigame in Swords and Souls

# About:
This is a bot created to automatically play the defense training minigame in Swords and Souls. It captures
the screen to detect where apples/stars are and block/dodge them respectively. The bot can reach a 
seemingly infinite score (up to a 100,000 combo before I stopped it).

# How to Run:
- Download block.py, CoordsCache.txt, coords.py
- By default, the game screen should be placed in the top-left corner of your screen
- To move or resize the game screen (not recommended):
  - Adjust game_screen and origin in block.py to the desired location of the screen
  - Delete CoordsCache.txt
  - coords.py
- Run block.py to start the bot
- Right-click to exit the program

# Requirements:
- [Bluemaxima's Flashpoint](https://flashpointarchive.org/downloads): A Flash emulator used to run the game
- [Python 3](https://www.python.org/downloads/): Used to run the bot script
- [Pillow](https://pillow.readthedocs.io/en/stable/): Image processing library used to capture the screen
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/): Input library used to control the mouse
- [Mouse](https://pypi.org/project/mouse/): Input library used to detect user input

