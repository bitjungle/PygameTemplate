''' Pygame template demo

A pygame template demo - responding to keyboard events

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
#import math   # Un-comment if needed
#import random # Un-comment if needed

# -- Game classes ------------------------------------------------------
import pygame_template_colors as color
import pygame_template_objects as objects

# -- Game window properties --------------------------------------------
DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Your Title Here'
SCREEN_BG_COLOR = color.black # From pygame_template_colors.py
FPS = 60                      # Frames per second

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
PAD_SPEED = 5 # pixels per frame
PAD_WIDTH = 100 # pixels
PAD_HEIGHT = 25 # pixels
xpos = DISPLAY_WIDTH // 2 - PAD_WIDTH // 2 # pad x start position
ypos = DISPLAY_HEIGHT - 2*PAD_HEIGHT
pad = objects.GameRectangle(width=PAD_WIDTH, height=PAD_HEIGHT, 
                            top=ypos, left=xpos, dx = 0, dy = 0,
                            fill=color.tomato)
ellipse = objects.GameEllipse(width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, 
                              top=0, left=0, fill=color.darkslategray,
                              border=100)
line = objects.GameLine(start_pos=(0, DISPLAY_HEIGHT // 2), 
                        end_pos=(DISPLAY_WIDTH, DISPLAY_HEIGHT // 2), 
                        line_width=10, fill=color.slategray)

while running: # Main loop
    for event in pygame.event.get(): # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                pad.dx = -PAD_SPEED # move pad 10 pixels to the left
            if key[pygame.K_RIGHT]:
                pad.dx = PAD_SPEED # move pad 10 pixels to the right
        elif event.type == pygame.KEYUP:
            pad.dx = 0 # stop the pad
        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            print('Mouse pos: ', mouse)
        elif event.type == pygame.MOUSEBUTTONUP:
            print('Mouse button released')
        else:
            print('Unhandled event', event)

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    # -- Implement game code here --------------------------------------
    pad.update() # Move the pad

    if pad.collide_vert_window_edge(DISPLAY_WIDTH): 
        pad.dx = 0 # Stop pad at screen edge

    # -- Drawing game objects ------------------------------------------
    # screen.blit() your game objects here
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    screen.blit(ellipse.image, ellipse.rect)
    screen.blit(line.image, line.rect)
    screen.blit(pad.image, pad.rect)
    
    # Update the full display Surface to the screen
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()

    # Limit the frame rate
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# -- Exiting... --------------------------------------------------------
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
