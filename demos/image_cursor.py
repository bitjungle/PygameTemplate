''' Pygame demo - image cursor

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
import math
import random 

# -- Game classes ------------------------------------------------------
sys.path.append('..') # Location of game classes, adjust as necessary
import pygame_template_colors as color
import pygame_template_objects as objects

# -- Game window properties --------------------------------------------
DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Image Cursor'
SCREEN_BG_COLOR = color.lightskyblue # From pygame_template_colors.py
FPS = 30                             # Frames per second

# -- Preparing game window ---------------------------------------------
# https://www.pygame.org/docs/ref/display.html?highlight=init#pygame.display.init
pygame.init() 
# https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
clock = pygame.time.Clock() 
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption
pygame.display.set_caption(WINDOW_TITLE)

running = True # The program will run as long as this variable is true

# -- Preparing game objects --------------------------------------------
sword = objects.GameImage(imagefile='sword.png',
                      width=25, height=25)
mymouse = objects.GameMousePointer(obj=sword)

black_holes = []

def make_black_hole(x, y, rad):
    return objects.GameCircle(radius=rad, width=rad*2, height=rad*2, 
                              fill=color.black, top=y-rad*2, left=x-rad*2,
                              border=0)

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() # Get pos when user release button
            black_holes.append(make_black_hole(pos[0], pos[1], 10))
        else:
            print('Unhandled event', event)

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    # -- Implement game code here --------------------------------------
    # Your code here
    #

    # -- Drawing game objects ------------------------------------------
    # screen.blit() your game objects here
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    for b in black_holes: # Draw all the black holes we have made so far
        screen.blit(b.surf, b.rect)

    mymouse.update()
    screen.blit(mymouse.obj.surf, mymouse.obj.rect)

    # Update the full display Surface to the screen
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# -- Exiting... --------------------------------------------------------
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
