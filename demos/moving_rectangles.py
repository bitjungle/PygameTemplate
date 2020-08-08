''' Pygame demo - moving rectangles

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
import math
import random

# ----------- Game classes -----------
sys.path.append('..')
import pygame_template_colors as color
import pygame_template_objects as objects

# https://www.pygame.org/docs/ref/display.html?highlight=init#pygame.display.init
pygame.init() 
# https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
clock = pygame.time.Clock() 

# ----------- Game window properties -----------
DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Moving rectangles'
SCREEN_BG_COLOR = color.black # From pygame_template_colors.py
FPS = 30                      # Frames per second

# ----------- Preparing game window -----------
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

running = True # The program will run as long as this variable is true

# ----------- Preparing game objects -----------
sq = objects.GameRectangle(top=100, left=100, 
                           width=20, height=20,
                           offset=[6, 4], fill=color.crimson)
p1 = objects.GameRectangle(top=100, left=50, 
                           width=10, height=100,
                           offset=[0, 4], fill=color.white)
p2 = objects.GameRectangle(top=100, left=DISPLAY_WIDTH - 50, 
                           width=10, height=100,
                           offset=[0, -3], fill=color.white)

def moveobject(obj):
    # check if the object is touching any edge of the window
    if obj.get_bottom() > DISPLAY_HEIGHT or obj.get_top() < 0:
        obj.flip_vert() # change y direction
    if obj.get_right() > DISPLAY_WIDTH or obj.get_left() < 0:
        obj.flip_horiz() # change x direction
    obj.move() # move the square with the given offset

def drawobject(obj):
    screen.blit(obj.image, obj.rect)

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    moveobject(sq)
    moveobject(p1)
    moveobject(p2)

    if sq.colliderect(p1) or sq.colliderect(p2):
        sq.flip_horiz()

# ----------- Drawing game objects -----------
    drawobject(sq)
    drawobject(p1)
    drawobject(p2)

    pygame.display.flip()
    clock.tick(FPS)

# Exiting...
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
