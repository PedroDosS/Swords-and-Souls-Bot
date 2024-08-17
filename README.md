# Swords and Souls Bot

## About:
<div align="center">
  <p>
    Swords and Souls, released in 2015, is an RPG game where the player must defeat waves of enemies in a battle arena. 
  </p>
  <img src="https://github.com/PedroDosS/Swords-and-Souls-Bot/assets/90741843/3245e85b-6e7e-4726-a6fc-e8d053b21177", alt="A view of the battle arena">
  <br><br>
  <p> 
    To progress further in the arena, the player can level up various combat-related skills by training in 5<br>
    different minigames. In the defense minigame, apples are thrown at the player from all directions, which<br>
    they must block. As the player's combo increases, the rate at which the apples appear also increases.
  </p>
  <img src="https://github.com/user-attachments/assets/2a68dae3-b1ed-4997-97b7-d78f6e42fc18", alt="The player standing in the middle of their training room, blocking apples">
  <br><br>
  <p>
    This bot is able to automatically play the blocking minigame by capturing the screen, detecting where<br>
    the apples are located, and moving the mouse to block them. It can run the game indefinitely without<br>
    breaking its combo, reaching a score of over 100,000 before it was stopped manually.
  </p>
  <img src="https://github.com/user-attachments/assets/2c162450-272b-467f-a8ba-6680e6c8e54d", alt="A recording of the bot automatically blocking the apples">
</div>
 
## How to Run:
- Place the game in the top-left corner of your screen
- If not using a 1920x1080p monitor, you may have to recompute the coordinates cache:
  - In *block.py*, adjust *game_screen* (line 12), to the location/size of the game screen (x, y, width, height)
  - Again in *block.py*, adjust *origin* (line 15), to match the position of the center of your player character 
  - Delete *CoordsCache.txt*
  - Run *coords.py* to regenerate *CoordsCache.txt*
- Run *block.py* to start the bot
- Right-click to exit the program

## Requirements:
- [Bluemaxima's Flashpoint](https://flashpointarchive.org/downloads): A Flash emulator used to run the game
- [Python 3](https://www.python.org/downloads/): Used to run the bot script
- [Pillow](https://pillow.readthedocs.io/en/stable/): Image processing library used to capture the screen
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/): Input library used to control the mouse
- [Mouse](https://pypi.org/project/mouse/): Input library used to detect user input
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Required for PyAutoGUI
