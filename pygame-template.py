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
DISPLAY_WIDTH = 800           # pixels
DISPLAY_HEIGHT = 600          # pixels
WINDOW_TITLE = 'Your title here'
SCREEN_BG_COLOR = color.lightskyblue # From pygame_template_colors.py
FPS = 30                      # Frames per second

# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption
pygame.display.set_caption(WINDOW_TITLE)

# Creating objects -----------------------------------------------------
snake = objects.Image(imagefile='snake.png',
                      dx=1, 
                      dy=1)
ball = objects.Image(imagefile='football.png',
                     top=300,
                     left=0,
                     width=50,
                     height=50)
mysword = objects.Image(imagefile='sword.png',
                        width=25,
                        height=25)
text = objects.Text(fontfile='Some-Time-Later.ttf',
                    fontsize=48,
                    text='The snake is moving!',
                    top=400,
                    left=200,
                    fontcolor=color.orangered)
myrect = objects.Rectangle(top=200,
                           left=200,
                           width=200,
                           height=100,
                           fill=color.crimson)
mycircle = objects.Circle(radius=100,
                          width=200,
                          height=100,
                          top=150,
                          left=300,
                          border=0, 
                          fill=color.palevioletred)

mymouse = objects.MousePointer(mysword)

running = True # The program will run as long as this variable is true

ball_x = 0           # Ball x start position
ball_x_direction = 1 # Ball x direction speed (px)

# Main loop ------------------------------------------------------------
while running:
    for event in pygame.event.get(): # Looking for keyboard/mouse events
        # https://www.pygame.org/docs/ref/event.html
        if event.type == pygame.QUIT: 
            running = False # Exiting the main loop
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print('Mouse pos:', pos)

    screen.fill(SCREEN_BG_COLOR)

    snake.move() # Moving the snake using the given offset pixels
    if snake.rect.top + snake.rect.height > DISPLAY_HEIGHT or snake.rect.top < 0:
        snake.flip_dy()
    if snake.rect.left + snake.rect.width > DISPLAY_WIDTH or snake.rect.left < 0:
        snake.flip_dx()

    ball_x += ball_x_direction # Moving the ball
    ball_y = 300 + 100*math.sin(ball_x*(1/(4*math.pi)))
    ball.move_to(x=ball_x, y=ball_y)
    if ball.rect.left + ball.rect.width > DISPLAY_WIDTH or ball_x < 0:
        ball_x_direction *= -1 # Flip the ball x direction

    # Refreshing the screen --------------------------------------------
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(myrect.surf, myrect.rect) # Drawing the rectangle
    screen.blit(mycircle.surf, mycircle.rect) # Drawing the circle
    screen.blit(snake.surf, snake.rect)   # Drawing the snake
    screen.blit(ball.surf, ball.rect)     # Drawing the ball
    screen.blit(text.surf, text.rect)     # Drawing the text

    mymouse.update()
    screen.blit(mymouse.obj.surf, mymouse.obj.rect)

    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    clock.tick(FPS)

# Exiting --------------------------------------------------------------
# https://www.pygame.org/docs/ref/pygame.html#pygame.quit
pygame.quit()
sys.exit()
