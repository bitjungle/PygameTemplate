''' Pygame template demo

A pygame template demo - a moving ball

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
#import math
#import random 

# -- Game classes ------------------------------------------------------
import pygame_template_colors as color

# -- Game window properties --------------------------------------------
DISPLAY_WIDTH = 800   # pixels
DISPLAY_HEIGHT = 600  # pixels
WINDOW_TITLE = 'Your Title Here'
SCREEN_BG_COLOR = color.lawngreen # RGB color code
FPS = 30 # Frames per second

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
# Making a moving ball 
radius = 20 # pixels
ball = pygame.Surface((radius*2, radius*2))
pygame.draw.circle(ball, color.indianred, (radius, radius), radius)
x = 200 # ball x coordinate starting position (pixels)
y = 200 # ball x coordinate starting position (pixels)
dx = 5  # movement in x direction for each loop
dy = 3  # movement in y direction for each loop

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            print('Key pressed: ', key)
        elif event.type == pygame.KEYUP:
            print('Key released')
        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            print('Mouse pos: ', mouse)
        else:
            print('Unhandled event', event)

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    # -- Implement game code here --------------------------------------
    # Check for collision with screen edges
    if x > (DISPLAY_WIDTH - 2*radius) or x < 0:
        dx *= -1 # change dx sign
    if y > (DISPLAY_HEIGHT - 2*radius) or y < 0:
        dy *= -1 # change dy sign

    # Move the demo ball by dx and dy pixels
    x += dx
    y += dy

    # -- Drawing game objects ------------------------------------------
    # screen.blit() your game objects here
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    screen.blit(ball, (x, y))

    # Update the full display Surface to the screen
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()

    # Limit the frame rate
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# -- Exiting... --------------------------------------------------------
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
