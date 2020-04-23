''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import pygame_template_colors as color

class GameObject(pygame.sprite.Sprite):# https://www.pygame.org/docs/ref/sprite.html
    '''Base class for all game objects'''

    def __init__(self, **kwargs):
        print('GameObject(', kwargs, ')')
        super(GameObject, self).__init__()

        DEFAULT_WIDTH = 0
        DEFAULT_HEIGHT = 0
        DEFAULT_TOP = 0
        DEFAULT_LEFT = 0
        DEFAULT_DX = 0
        DEFAULT_DY = 0

        self.imagefile = kwargs.get('imagefile', None)

        if self.imagefile:
            self.image = pygame.image.load(self.imagefile).convert_alpha()
            if kwargs.get('width', False) and kwargs.get('height', False):
                self.image = pygame.transform.smoothscale(self.image,
                                                          (kwargs.get('width'),
                                                           kwargs.get('height')))
        else:
            self.image = pygame.Surface((kwargs.get('width', DEFAULT_WIDTH), 
                                         kwargs.get('height', DEFAULT_HEIGHT)))
            self.image.fill(kwargs.get('fill', pygame.SRCALPHA))

        self.rect = self.image.get_rect(top=kwargs.get('top', DEFAULT_TOP), 
                                        left=kwargs.get('left', DEFAULT_LEFT))
        self.dx = kwargs.get('dx', DEFAULT_DX)
        self.dy = kwargs.get('dy', DEFAULT_DX)

    def set_top(self, pos):
        '''Set top position'''
        self.rect.top = pos 

    def set_left(self, pos):
        '''Set left position'''
        self.rect.left = pos 

    def center_on_rect(self, target_rect):
        '''Center the object in the middle of a target rect'''
        self.rect.top = (target_rect.height // 2) - (self.rect.height // 2)
        self.rect.left = (target_rect.width // 2) - (self.rect.width // 2)

    def colliderect(self, rect):
        '''Returns true if this object overlaps with the given rectangle'''
        # TODO groupcollide spritecollide
        return self.rect.colliderect(rect)

    def move(self):
        '''Move the object by dx and dy'''
        self.rect = self.rect.move((self.dx, self.dy))

    def flip_dx(self):
        '''Flip the dx value'''
        self.dx *= -1

    def flip_dy(self):
        '''Flip the dy'''
        self.dy *= -1

class Text(GameObject):
    '''Game text elements'''
    def __init__(self, **kwargs):
        print('Text(', kwargs, ')')
        super(Text, self).__init__(**kwargs)
        self.fontfile = kwargs.get('fontfile', None)
        self.fontsize = kwargs.get('fontsize', 24)
        
        try: 
            self._font = pygame.font.Font(self.fontfile, self.fontsize)
        except OSError as err:
            self._font = pygame.font.SysFont('courier', self.fontsize)

        self.color = kwargs.get('color', (0, 0, 0))
        self.text = kwargs.get('text', '')
        self.antialias = kwargs.get('antialias', True)
        self.render(self.text)

    def render(self, text=None):
        '''TODO'''
        if text is not None: 
            self.text = text
        self.image = self._font.render(self.text, self.antialias, self.color)


if __name__ == "__main__":
    pass