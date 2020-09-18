''' Pygame template demo

A pygame template demo - detecting and handling collisions

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import sys
#import math   # Un-comment if needed
import random

# -- Game classes ------------------------------------------------------
import pygame_template_colors as color
import pygame_template_objects as objects

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
NUM_DISCS = 5
discs = pygame.sprite.Group()
c = 0
while c < NUM_DISCS:
    x = random.randint(0, 700)
    y = random.randint(0, 500)
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    d = objects.GameCircle(radius=25, 
                           fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 
                           top=y, left=x,
                           dx=dx, dy=dy)
    if not pygame.sprite.spritecollide(d, discs, False):
        # Making sure that we don't create overlapping discs
        discs.add(d)
        c += 1

NUM_SPIDERS = 25
spiders = pygame.sprite.Group()
c = 0
while c < NUM_SPIDERS:
    # Creating spiders with random start position and random speed/direction
    x = random.randint(0, 700)
    y = random.randint(0, 500)
    dx = random.randint(-4, 4)
    dy = random.randint(-4, 4)
    s = objects.GameImage(imagefile='spider.png', scale=0.1, 
                          top=y, left=x, dx=dx, dy=dy)
    if not pygame.sprite.spritecollide(s, spiders, False):
        # Making sure that we don't create overlapping spiders
        spiders.add(s)
        c += 1

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
            print('Mouse button released')
        else:
            print('Unhandled event', event)

    screen.fill(SCREEN_BG_COLOR)  # Blanking the screen

    # -- Implement game code here --------------------------------------
    for d in discs: # Loop through all disks to find collisions
        d.collide_window_edge(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        discs.remove(d)  # remove disc from group
        d.collide(discs, circle=True) # check for collision with objects in group
        discs.add(d)     # add disc back into group
    for s in spiders: # Loop through all spiders to find collisions
        s.collide_window_edge(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        spiders.remove(s)  # remove spider from group
        s.collide(spiders, ratio=0.6) # check for collision with objects in group
        spiders.add(s)     # add spider back into group
        
    # -- Drawing game objects ------------------------------------------
    # screen.blit() your game objects here
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    discs.draw(screen)
    spiders.draw(screen)

    # Update the full display Surface to the screen
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()

    # Limit the frame rate
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# -- Exiting... --------------------------------------------------------
pygame.quit() # https://www.pygame.org/docs/ref/pygame.html#pygame.quit
sys.exit()    # https://docs.python.org/3.8/library/sys.html#sys.exit
