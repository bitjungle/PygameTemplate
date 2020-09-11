''' Pygame template

A pygame template to get my students quickly up and running.

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
import math
#import random 

# -- Game classes ------------------------------------------------------
import pygame_template_colors as color

# -- Game window properties --------------------------------------------
DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Your Title Here'
SCREEN_BG_COLOR = color.black # From pygame_template_colors.py
FPS = 30                      # Frames per second

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
# Loading and displaying an image
# https://www.pygame.org/docs/ref/image.html#pygame.image.load
image = pygame.image.load('snake.png')
xstart = 200
ystart = 100
n = [i/100 for i in range(-314, 314)] # -pi to pi, used for calculating x and y
k = 0 # pointer to current n value
kmax = len(n) - 1

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop
        else:
            print('Unhandled event', event)

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    # -- Implement game code here --------------------------------------
    if k > kmax: # end of list
        k = 0    # reset
    x = int(xstart + math.sin(n[k])* 100) # calculate new x position
    y = int(ystart + math.cos(n[k])* 100) # calculate new y position
    k += 1 # moving the pointer to the next n value

    # -- Drawing game objects ------------------------------------------
    # screen.blit() your game objects here
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    screen.blit(image, (x, y))

    # Update the full display Surface to the screen
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# -- Exiting... --------------------------------------------------------
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
