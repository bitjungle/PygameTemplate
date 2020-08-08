''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import pygame_template_colors as color

# ----------------------------------------------------------------------
class GameObject(pygame.sprite.Sprite):
    '''Base class for all game objects'''
    def __init__(self, **kwargs):
        print('GameObject(', kwargs, ')')
        super(GameObject, self).__init__()
        self.image = pygame.Surface((kwargs.get('width', 1), 
                                     kwargs.get('height', 1)))
        self.rect = self.image.get_rect()
        self.rect.top = kwargs.get('top', 0)
        self.rect.left = kwargs.get('left', 0)
        self.offset = kwargs.get('offset', [0, 0])

    def move(self):
        self.rect = self.rect.move(self.offset)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def collidegroup(self, group):
        '''Check for collision within a sprite group'''
        for item in group:
            if self != item and self.rect.colliderect(item.rect):
                self.flip_horiz()

    def flip_horiz(self):
        '''Flip the x value in the offset [x, y] pair'''
        self.offset[0] *= -1
        self.rect.left += self.offset[0]*2

    def flip_vert(self):
        '''Flip the y value in the offset [x, y] pair'''
        self.offset[1] *= -1
        self.rect.top += self.offset[1]*2

    def set_top(self, pos):
        '''Set top position'''
        self.rect.top = pos 

    def set_left(self, pos):
        '''Set left position'''
        self.rect.left = pos 

    def get_top(self):
        '''Return top position'''
        return self.rect.top

    def get_left(self):
        '''Return left position'''
        return self.rect.left

    def get_bottom(self):
        '''Return bottom position'''
        return self.rect.bottom

    def get_right(self):
        '''Return right position'''
        return self.rect.right

    def center_on_rect(self, target_rect):
        '''Center the object in the middle of a target rect'''
        self.rect.top = (target_rect.height // 2) - (self.rect.height // 2)
        self.rect.left = (target_rect.width // 2) - (self.rect.width // 2)
    
    def scale(self, width, height):
        '''Resizes the object Surface to a new resolution.'''
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def grow(self, w, h):
        self.scale(self.rect.width + w, self.rect.height + h)    

# ----------------------------------------------------------------------
class GameRectangle(GameObject):
    '''A rectangular object'''
    def __init__(self, **kwargs):
        print('GameRectangle(', kwargs, ')')
        super(GameRectangle, self).__init__(**kwargs)
        self.image.fill(kwargs.get('fill', color.gray))

# ----------------------------------------------------------------------
class GameImage(GameObject):
    '''A moving image object'''
    def __init__(self, **kwargs):
        print('GameImage(', kwargs, ')')
        super(GameImage, self).__init__(**kwargs)
        self.image = self.image_orig = pygame.image.load(kwargs.get('imagefile', None))
        if kwargs.get('width', False) and kwargs.get('height', False):
            self.scale(kwargs.get('width'), kwargs.get('height'))
        else:
            self.rect = self.image.get_rect()
        self.rect.top = kwargs.get('top', 0)   # must set after loading image
        self.rect.left = kwargs.get('left', 0) # must set after loading image

    def scale(self, width, height):
        '''Resizes the object Surface to a new resolution, use original image.'''
        self.image = pygame.transform.smoothscale(self.image_orig, (width, height))
        self.rect = self.image.get_rect()

# ----------------------------------------------------------------------
class GameTextElement(GameObject):
    '''Game text elements'''
    def __init__(self, **kwargs):
        print('GameTextElement(', kwargs, ')')
        super(GameTextElement, self).__init__(**kwargs)
        self.fontfile = kwargs.get('fontfile', 'Some-Time-Later.ttf')
        self.fontsize = kwargs.get('fontsize', 24)
        try: 
            self._font = pygame.font.Font(self.fontfile, self.fontsize)
        except OSError as e:
            self._font = pygame.font.SysFont('courier', self.fontsize)

        self.color = kwargs.get('color', (0,0,0))
        self.text = kwargs.get('text', '')
        self.antialias = kwargs.get('antialias', True)
                
        self.render(self.text)
    
    def render(self, text=None):
        if text != None: 
            self.text = text
        self.image = self._font.render(self.text, self.antialias, self.color)


if __name__ == "__main__":
    pass