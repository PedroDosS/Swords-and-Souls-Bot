from PIL import Image
from PIL import ImageGrab
from coords import get_spiral_coords
import pyautogui
import mouse
import sys
import os
import ast
import time

# Defines where the game screen is
game_screen = [0, 50, 800, 650]
game_width = game_screen[2] - game_screen[0]
game_height = game_screen[3] - game_screen[1]
game_dimensions = [game_width, game_height]
origin = [400, 358] # Defines where the apples will be moving towards
min_radius = 48 # Controls the radius around the player which is checked for apples
max_radius = 148

pyautogui.FAILSAFE = False

# Loads the cache of closest pixel coordinates to the player. If none are found, it will generate and save them
def get_cached_coords(path):
    coords = []
    if os.path.exists(path):
        with open(path) as file:
            print('Coods cache detected!')
            cached_dimensions = ast.literal_eval(file.readline())
            if cached_dimensions == game_screen:
                print('Loading coords...')
                coords = ast.literal_eval(file.readline())
                print('Coords cache successfully loaded!')
                return coords
            else:
                print('Coods cache does not meet expected dimensions')
    else:
        print('Could not find coords cache')

    if coords == []:
        print('Generating coords...')
        coords = get_spiral_coords(origin, game_screen, path, min_radius, max_radius)
        print('Done!')
        return coords


sorted_coords = get_cached_coords('Coords Cache.txt')


# Finds the pixel 180 degrees away, centered at the player
# This is used to avoid blocking stars
def get_opposite(coord):
    delta_x = origin[0] - coord[0]
    delta_y = origin[1] - coord[1]
    return [origin[0] + delta_x, origin[1] + delta_y]

# Captures the screen, detects where apples are, and aims the mouse to block them
def aim_at_apples():
    im = ImageGrab.grab(bbox = game_screen)
    im_width, im_height = im.size
    pix = im.load()

    # Checks the pixels around the player in closest to furthest order
    for abs_coord in sorted_coords:
        abs_x_coord = abs_coord[0]
        abs_y_coord = abs_coord[1]

        # Converts the pixel coordinate on screen to the local coordinate of the game's bounding box
        rel_x_coord = abs_x_coord - game_screen[0]
        rel_y_coord = abs_y_coord - game_screen[1]
        pixel = pix[rel_x_coord, rel_y_coord]
        if pixel == (153, 39, 41): # Detects red pixels (apples), aims the mouse towards them
            pyautogui.moveTo(abs_x_coord, abs_y_coord, _pause=False)
            return
        elif pixel == (241, 192, 0): # Detects yellow pixels (stars), aims the mouse away from them
            opposite_x, opposite_y = get_opposite(abs_coord)
            pyautogui.moveTo(opposite_x, opposite_y, _pause=False)
            return

# Main loop
# Holding the right mouse button is a failsafe to break out of the program, as it has no automatic stop
while not mouse.is_pressed(button='right'):
    start = time.time()
    aim_at_apples()
    print(time.time() - start)
