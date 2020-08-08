''' Pygame demo growing snake

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
WINDOW_TITLE = 'Growing snake'
SCREEN_BG_COLOR = color.olive # From pygame_template_colors.py
FPS = 30                      # Frames per second

# ----------- Preparing game window -----------
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

snake = objects.GameImage(imagefile='snake.png', 
                          offset=[1, 1], 
                          width=40, height=40)
text = objects.GameTextElement(fontfile=None, fontsize=48, 
                               text='The snake is growing!', 
                               top=400, left=400,
                               offset=[-1, 0],
                               color=color.lightcoral)

running = True # The program will run as long as this variable is true

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    snake.move() # Moving the snake using the given offset pixels
    snake.grow(10, 10)
    text.move()  # Moving the text using the given offset pixels

    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    screen.blit(text.image, text.rect)     # Drawing the text
    screen.blit(snake.image, snake.rect)   # Drawing the snake

    pygame.display.flip()
    clock.tick(FPS)

# Exiting...
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
