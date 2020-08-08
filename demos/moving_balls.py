''' Pygame demo - moving balls

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
import math
import random

# ----------- Game classes -----------
sys.path.append('..') # Location of game classes, adjust as necessary
import pygame_template_colors as color
import pygame_template_objects as objects

# https://www.pygame.org/docs/ref/display.html?highlight=init#pygame.display.init
pygame.init() 
# https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
clock = pygame.time.Clock() 

# ----------- Game window properties -----------
DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Moving ball'
SCREEN_BG_COLOR = color.forestgreen # From pygame_template_colors.py
FPS = 30                      # Frames per second

# ----------- Preparing game window -----------
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

running = True # The program will run as long as this variable is true

# ----------- Preparing game objects -----------
NUM_BALLS = 10
ballgroup = pygame.sprite.Group() 
for _ in range(NUM_BALLS):
    xoffset = random.randint(1, 10)
    yoffset = random.randint(1, 10)
    # Create all ball objects and add them to a sprite group
    ballgroup.add(objects.GameImage(imagefile='ball.png',
                                    width=40, height=40,
                                    top=xoffset*50, left=yoffset*50, 
                                    offset=[xoffset, yoffset])) 

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop

    screen.fill(SCREEN_BG_COLOR) # Blanking the screen

    for ball in ballgroup:
        # check if the square is touching any edge of the window
        if ball.get_bottom() > DISPLAY_HEIGHT or ball.get_top() < 0:
            ball.flip_vert() # change y direction
        if ball.get_right() > DISPLAY_WIDTH or ball.get_left() < 0:
            ball.flip_horiz() # change x direction
        
        ball.collidegroup(ballgroup) # check for collisions within the group

        ball.move() # move the ball with the given offset
        screen.blit(ball.image, ball.rect)

    ballgroup.update()

    pygame.display.flip()
    clock.tick(FPS)

# Exiting...
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
