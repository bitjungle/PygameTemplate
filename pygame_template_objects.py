''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import pygame_template_colors as color

class GameObject(pygame.sprite.Sprite):
    '''Base class for all game objects'''
    def __init__(self, **kwargs):
        print('GameObject(', kwargs, ')')
        super(GameObject, self).__init__()
        self.image = pygame.Surface((kwargs.get('width', 0), kwargs.get('height', 0)))
        self.rect = self.image.get_rect()
        self.rect.top = kwargs.get('top', 0)
        self.rect.left = kwargs.get('left', 0)
        self.offset = kwargs.get('offset', [0, 0])

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
        self.rect = self.rect.move(self.offset)

    def flip_x_offset(self):
        '''Flip the x value in the offset [x, y] pair'''
        self.offset[0] *= -1

    def flip_y_offset(self):
        '''Flip the y value in the offset [x, y] pair'''
        self.offset[1] *= -1

class Rectangle(GameObject):
    '''A rectangular object'''
    def __init__(self, **kwargs):
        print('Rectangle(', kwargs, ')')
        super(Rectangle, self).__init__(**kwargs)
        self.image.fill(kwargs.get('fill', color.gray))

class Image(GameObject):
    '''An image object'''
    def __init__(self, **kwargs):
        print('Image(', kwargs, ')')
        super(Image, self).__init__(**kwargs)
        self.image = pygame.image.load(kwargs.get('imagefile', None))
        self.rect = self.image.get_rect()

class Text(GameObject):
    '''Game text elements'''
    def __init__(self, **kwargs):
        print('Text(', kwargs, ')')
        super(Text, self).__init__(**kwargs)
        self.fontfile = kwargs.get('fontfile', 'Some-Time-Later.ttf')
        self.fontsize = kwargs.get('fontsize', 24)
        
        try: 
            self._font = pygame.font.Font(self.fontfile, self.fontsize)
        except OSError as err:
            self._font = pygame.font.SysFont('courier', self.fontsize)

        self.color = kwargs.get('color', (0,0,0))
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