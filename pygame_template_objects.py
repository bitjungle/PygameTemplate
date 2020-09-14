''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame

# ----------------------------------------------------------------------
class GameRectangle(pygame.sprite.Sprite):
    '''Rectangular object
    
    Class for creating rectangular objects.

    Args:
        width (int): Rect width in pixels
        height (int): Rect height in pixels
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Object fill color (optional, default is transparent)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameRectangle(', kwargs, ')')
        super(GameRectangle, self).__init__()

        self.image = pygame.Surface((kwargs.get('width', 1), 
                                     kwargs.get('height', 1)))
        self.image.fill(kwargs.get('fill', pygame.SRCALPHA))
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                        left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameCircle(pygame.sprite.Sprite):
    '''Circle object
    
    Class for creating circular objects.

    Args:
        radius (int): Circle radius (optional)
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Circle/border fill color (optional, default is gray)
        border (int): Border width (optional, default is a filled circle)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameCircle(', kwargs, ')')
        super(GameCircle, self).__init__()
        r = kwargs.get('radius', 1)
        self.image = pygame.Surface((r*2, r*2))
        self.image.fill(pygame.SRCALPHA)
        pygame.draw.circle(self.image, 
                           kwargs.get('fill', pygame.Color(128,128,128)), 
                           (r, r), r, 
                           kwargs.get('border', 0))
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                       left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameImage(pygame.sprite.Sprite):
    '''Image object
    
    Create an image object

    Args:
        imagefile (str): Image path/filename
        width (int): Image width (optional, will scale the image)
        height (int): Image height (optional, will scale the image)
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''
    
    def __init__(self, **kwargs):
        print('GameImage(', kwargs, ')')
        super(GameImage, self).__init__()

        self.image = self.image = pygame.image.load(kwargs.get('imagefile', None))

        if kwargs.get('width', False) and kwargs.get('height', False):
            self.scale(kwargs.get('width'), kwargs.get('height'))
        else:
            self.rect = self.image.get_rect()

        self.rect.top = kwargs.get('top', 0)   # must set after loading image
        self.rect.left = kwargs.get('left', 0) # must set after loading image

    def scale(self, width, height):
        '''Resizes the object Surface to a new resolution, use original image.'''
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect()

# ----------------------------------------------------------------------
class GameMousePointer(pygame.sprite.Sprite):
    ''' A custom mouse pointer 

    Args:
        img (GameImage): An image used for the mouse pointer (optional)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''
    def __init__(self, **kwargs):
        print('GameMousePointer(', kwargs, ')')
        super().__init__()

        self.obj = kwargs.get('img', None)

        if self.obj:
            pygame.mouse.set_visible(False)
            self.image = self.obj.image
            self.rect = self.obj.rect
        else:
            self.image = pygame.Surface((1,1))
            self.rect = self.image.get_rect()
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
 
    def update(self):
        """Set the object to be where the mouse is. """
        pos = pygame.mouse.get_pos()
        self.obj.move_to(x=pos[0], y=pos[1])

# ----------------------------------------------------------------------
class GameTextElement(pygame.sprite.Sprite):
    '''Text element
    
    Text element

    Args:
        text (str): The text to display (optional)
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fontfile (str): Name of font file to load (optional)
        fontsize (int): Font size (optional, default is 24)
        antialias (bool): Turn antialias on/off
        fontcolor (pygame.Color): Font color

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameTextElement(', kwargs, ')')
        super(GameTextElement, self).__init__()

        self.fontfile = kwargs.get('fontfile', None)
        self.fontsize = kwargs.get('fontsize', 24)
        try: 
            self._font = pygame.font.Font(self.fontfile, self.fontsize)
        except OSError as e:
            self._font = pygame.font.SysFont('courier', self.fontsize)

        self.color = kwargs.get('color', (0,0,0))
        self.text = kwargs.get('text', '')
        self.antialias = kwargs.get('antialias', True)
        self.render(self.text)
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                       left=kwargs.get('left', 0))
    
    def render(self, text=None):
        '''TODO'''
        if text is not None: 
            self.text = text
        self.image = self._font.render(self.text, self.antialias, self.color)

if __name__ == "__main__":
    pass