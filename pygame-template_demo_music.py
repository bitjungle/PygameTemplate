''' Pygame template demo

A pygame template demo - playing sound

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
WINDOW_TITLE = 'Playing sound'
SCREEN_BG_COLOR = color.darkred # From pygame_template_colors.py
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
# https://www.pygame.org/docs/ref/music.html
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
playing = True
helptext = objects.GameTextElement(text='Mouse click to pause/resume',
                                   color=color.white, top=100, left=100)

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
        elif event.type == pygame.MOUSEBUTTONUP:
            if playing: # pause playback
                playing = False
                pygame.mixer.music.pause()
            else: # resume playback
                playing = True 
                pygame.mixer.music.unpause()
        else:
            print('Unhandled event', event)

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    # -- Implement game code here --------------------------------------
    # Your code here
    #

    # -- Drawing game objects ------------------------------------------
    # screen.blit() your game objects here
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    screen.blit(helptext.image, helptext.rect)

    # Update the full display Surface to the screen
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()

    # Limit the frame rate
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# -- Exiting... --------------------------------------------------------
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
