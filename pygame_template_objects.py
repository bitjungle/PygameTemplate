''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import pygame_template_colors as color

class GameObject(pygame.sprite.Sprite):# https://www.pygame.org/docs/ref/sprite.html
    '''Base class for all game objects

    Extends the pygame.sprite.Sprite class. Base class for visible game objects.

    Args:
        width (int): Rect width in pixels
        height (int): Rect height in pixels
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Object fill color (optional, default is transparent)

    Attributes:
        surf (Surface): object for representing images
        rect (Rect): object for storing rectangular coordinates
        dx (int): Number of pixels to move object in x direction for each move()
        dy (int): Number of pixels to move object in y direction for each move()
    '''

    def __init__(self, **kwargs):
        print('GameObject(', kwargs, ')')
        super(GameObject, self).__init__()

        DEFAULT_WIDTH = 0
        DEFAULT_HEIGHT = 0
        DEFAULT_TOP = 0
        DEFAULT_LEFT = 0
        DEFAULT_DX = 0
        DEFAULT_DY = 0

        self.dx = kwargs.get('dx', DEFAULT_DX)
        self.dy = kwargs.get('dy', DEFAULT_DX)

        self.surf = pygame.Surface((kwargs.get('width', DEFAULT_WIDTH), 
                                    kwargs.get('height', DEFAULT_HEIGHT)))
        self.surf.fill(kwargs.get('fill', pygame.SRCALPHA))
        self.rect = self.surf.get_rect(top=kwargs.get('top', DEFAULT_TOP),
                                       left=kwargs.get('left', DEFAULT_LEFT))

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

    def move(self, **kwargs):
        '''Move the object by dx and dy'''
        if kwargs.get('dx', None): self.dx = kwargs.get('dx')
        if kwargs.get('dy', None): self.dy = kwargs.get('dy')
        self.rect = self.rect.move((self.dx, self.dy))

    def move_to(self, **kwargs):
        '''Move the object to x and y'''
        if kwargs.get('x', None): self.rect.centerx = kwargs.get('x')
        if kwargs.get('y', None): self.rect.centery = kwargs.get('y')

    def flip_dx(self):
        '''Flip the dx value'''
        self.dx *= -1

    def flip_dy(self):
        '''Flip the dy value'''
        self.dy *= -1

class Rectangle(GameObject):
    '''Rectangular object
    
    Class for creating rectangular objects.

    Args:
        width (int): Rect width in pixels
        height (int): Rect height in pixels
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Object fill color (optional, default is transparent)

    Attributes:
        surf (Surface): object for representing images
        rect (Rect): object for storing rectangular coordinates
        dx (int): Number of pixels to move object in x direction for each move()
        dy (int): Number of pixels to move object in y direction for each move()
    '''

    def __init__(self, **kwargs):
        print('Rectangle(', kwargs, ')')
        super(Rectangle, self).__init__(**kwargs)

class Image(GameObject):
    '''Image object
    
    Create an image object

    Args:
        imagefile (str): Image path/filename
        width (int): Image width (optional, will scale the image)
        height (int): Image height (optional, will scale the image)
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)

    Attributes:
        surf (Surface): object for representing images
        rect (Rect): object for storing rectangular coordinates
        dx (int): Number of pixels to move object in x direction for each move()
        dy (int): Number of pixels to move object in y direction for each move()
    '''
    
    def __init__(self, **kwargs):
        print('Image(', kwargs, ')')
        super(Image, self).__init__(**kwargs)
        self.surf = pygame.image.load(kwargs.get('imagefile')).convert_alpha()
        if kwargs.get('width', False) and kwargs.get('height', False):
            self.surf = pygame.transform.smoothscale(self.surf,
                                                     (kwargs.get('width'),
                                                      kwargs.get('height')))

class Circle(GameObject):
    '''Circle object
    
    Class for creating circular objects.

    Args:
        width (int): Rect width in pixels
        height (int): Rect height in pixels
        radius (int): Circle radius (optional)
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Circle/border fill color (optional, default is gray)
        border (int): Border width. A value of 0 will fill the circle

    Attributes:
        surf (Surface): object for representing images
        rect (Rect): object for storing rectangular coordinates
        dx (int): Number of pixels to move object in x direction for each move()
        dy (int): Number of pixels to move object in y direction for each move()
        radius (int): Circle radius
    '''

    def __init__(self, **kwargs):
        print('Circle(', kwargs, ')')
        super(Circle, self).__init__(**kwargs)
        self.radius = kwargs.get('radius', kwargs.get('width', 2) // 2)

        self.surf.fill(pygame.SRCALPHA)
        pygame.draw.circle(self.surf, kwargs.get('fill', color.gray), 
                            (self.radius, self.radius), self.radius, 
                            kwargs.get('border', 1))

class Text(GameObject):
    '''Text element
    
    Text element

    Args:
        text (str): The text to display
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fontfile (str): 
        fontsize (int): 
        antialias (bool): Turn antialias on/off
        fontcolor (pygame.Color): Font color

    Attributes:
        surf (Surface): object for representing images
        rect (Rect): object for storing rectangular coordinates
        dx (int): Number of pixels to move object in x direction for each move()
        dy (int): Number of pixels to move object in y direction for each move()
    '''

    def __init__(self, **kwargs):
        print('Text(', kwargs, ')')
        super(Text, self).__init__(**kwargs)
        self.fontfile = kwargs.get('fontfile', None)
        self.fontsize = kwargs.get('fontsize', 24)
        
        try: 
            self._font = pygame.font.Font(self.fontfile, self.fontsize)
        except OSError as err:
            self._font = pygame.font.SysFont('courier', self.fontsize)

        self.color = kwargs.get('fontcolor', (0, 0, 0))
        self.text = kwargs.get('text', '')
        self.antialias = kwargs.get('antialias', True)
        self.render(self.text)

    def render(self, text=None):
        '''TODO'''
        if text is not None: 
            self.text = text
        self.surf = self._font.render(self.text, self.antialias, self.color)

class MousePointer(pygame.sprite.Sprite):
    ''' Mouse pointer 

    Args:
        obj (GameObject): A game object used for the mouse pointer (optional)

    Attributes:
        obj.surf (Surface): object for representing images
        obj.rect (Rect): object for storing rectangular coordinates
    '''
    def __init__(self, obj=None):
        """ Create the player image. """
        super().__init__()
        if obj:
            self.obj = obj
            pygame.mouse.set_visible(False)
        else:
            self.obj = GameObject()
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
 
    def update(self):
        """Set the object to be where the mouse is. """
        pos = pygame.mouse.get_pos()
        self.obj.move_to(x=pos[0], y=pos[1])

if __name__ == "__main__":
    pass