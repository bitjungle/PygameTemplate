''' Pygame Template

A pygame template to get my students quickly up and running.

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
import math
import pygame_template_colors as color
import pygame_template_objects as objects

pygame.init()
clock = pygame.time.Clock()

DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Your title here'
SCREEN_BG_COLOR = color.olive # From pygame_template_colors.py
FPS = 30                      # Frames per second

snake = objects.Image(imagefile='snake.png', 
                            offset=[1,1])
text = objects.Text(fontfile=None, 
                    fontsize=48, 
                    text='The snake is moving!', 
                    top=400,
                    left=400,
                    color=color.lightcoral)
myrect = objects.Rectangle(top=200,
                           left=400,
                           width=200,
                           height=100,
                           fill=color.crimson)

screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

running = True # The program will run as long as this variable is true

while running: # Main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop

    screen.fill(SCREEN_BG_COLOR)

    snake.move() # Moving the snake using the given offset pixels

    screen.blit(text.image, text.rect)     # Drawing the text
    screen.blit(snake.image, snake.rect)   # Drawing the snake
    screen.blit(myrect.image, myrect.rect) # Drawing the rectangle

    pygame.display.flip()
    clock.tick(FPS)

# Exiting...
pygame.quit()
sys.exit()
