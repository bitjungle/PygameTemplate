''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame

# ----------------------------------------------------------------------
class GameObject(pygame.sprite.Sprite):
    '''Base class for all game objects

    Extends the pygame.sprite.Sprite class. 
    Base class for all game objects.

    Args:
        dx (int): Number of pixels to move object in x direction
        dy (int): Number of pixels to move object in y direction

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)
    '''
    def __init__(self, **kwargs):
        print('GameObject(', kwargs, ')')
        super(GameObject, self).__init__()

        self.image = pygame.Surface((kwargs.get('width', 1), 
                                     kwargs.get('height', 1)))
        self.image.fill(pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.dx = kwargs.get('dx', 0)
        self.dy = kwargs.get('dy', 0)

    def update(self):
        '''Move the object by dx and dy'''
        self.rect = self.rect.move((self.dx, self.dy))

    def move_to(self, **kwargs):
        '''Move the object to x and y'''
        if kwargs.get('x', None): self.rect.centerx = kwargs.get('x')
        if kwargs.get('y', None): self.rect.centery = kwargs.get('y')

# ----------------------------------------------------------------------
class GameRectangle(GameObject):
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
        super(GameRectangle, self).__init__(**kwargs)

        pygame.draw.rect(self.image, kwargs.get('fill', pygame.SRCALPHA), 
                         (0, 0, kwargs.get('width', 1), kwargs.get('height', 1)),
                          width=0)
        
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                        left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameCircle(GameObject):
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
        r = kwargs.get('radius', 1)
        kwargs['width'] = kwargs['height'] = r*2
        super(GameCircle, self).__init__(**kwargs)

        pygame.draw.circle(self.image, 
                           kwargs.get('fill', pygame.Color(128,128,128)), 
                           (r, r), r, kwargs.get('border', 0))
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                        left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameImage(GameObject):
    '''Image object
    
    Create an image object

    Args:
        imagefile (str): Image path/filename
        width (int): Image width (optional, will scale the image)
        height (int): Image height (optional, will scale the image)
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        scale (float): scale image by factor

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''
    
    def __init__(self, **kwargs):
        print('GameImage(', kwargs, ')')
        super(GameImage, self).__init__(**kwargs)

        self.image = pygame.image.load(kwargs.get('imagefile', None))

        if kwargs.get('width', False) and kwargs.get('height', False):
            self.scale(kwargs.get('width'), kwargs.get('height'))
        else:
            self.rect = self.image.get_rect()

        if kwargs.get('scale', False):
            self.scale(int(self.rect.width * kwargs.get('scale')), 
                       int(self.rect.height * kwargs.get('scale')))

        self.rect.top = kwargs.get('top', 0)   # must set after loading image
        self.rect.left = kwargs.get('left', 0) # must set after loading image

    def scale(self, width, height):
        '''Resizes the object Surface to a new resolution, use original image.'''
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect()

# ----------------------------------------------------------------------
class GameMousePointer(GameObject):
    ''' A custom mouse pointer 

    Args:
        img (GameImage): An image used for the mouse pointer (optional)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''
    def __init__(self, **kwargs):
        print('GameMousePointer(', kwargs, ')')
        super(GameMousePointer, self).__init__(**kwargs)

        self.obj = kwargs.get('img', None)

        if self.obj:
            pygame.mouse.set_visible(False)
            self.image = self.obj.image
            self.rect = self.obj.rect
        else:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            self.rect = self.image.get_rect()
 
    def update(self):
        """Set the object to be where the mouse is. """
        pos = pygame.mouse.get_pos()
        self.obj.move_to(x=pos[0], y=pos[1])

# ----------------------------------------------------------------------
class GameTextElement(GameObject):
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
        super(GameTextElement, self).__init__(**kwargs)

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