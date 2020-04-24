''' Pygame Template

A pygame template to get my students quickly up and running.

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import sys
import math
import pygame
import pygame_template_colors as color
import pygame_template_objects as objects

# https://www.pygame.org/docs/ref/pygame.html#pygame.init
pygame.init()
# https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
clock = pygame.time.Clock()

# Screen settings ------------------------------------------------------
DISPLAY_WIDTH = 800  # pixels
DISPLAY_HEIGHT = 600 # pixels
WINDOW_TITLE = 'Your title here'
SCREEN_BG_COLOR = color.lightskyblue # From pygame_template_colors.py
FPS = 30             # Frames per second

# Creating objects -----------------------------------------------------
myrect = objects.Rectangle(top=10, left=10, 
                           width=200, height=100, 
                           dx=1, dy=1,
                           fill=color.crimson)

# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption
pygame.display.set_caption(WINDOW_TITLE)

running = True # The program will run as long as this variable is true

# Main loop ------------------------------------------------------------
while running:
    for event in pygame.event.get(): # Looking for keyboard/mouse events
        # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop

    # Clear the screen -------------------------------------------------
    screen.fill(SCREEN_BG_COLOR)

    # Do stuff ---------------------------------------------------------
    myrect.move() # Moving the rectangle using the given offset pixels

    # Refreshing the screen --------------------------------------------
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(myrect.surf, myrect.rect)     # Drawing the rectangle

    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# Exiting --------------------------------------------------------------
# https://www.pygame.org/docs/ref/pygame.html#pygame.quit
pygame.quit()
sys.exit()
