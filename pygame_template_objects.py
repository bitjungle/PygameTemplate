''' Pygame Template Objects

Copyright (C) 2020 BITJUNGLE Rune Mathisen
This code is licensed under a GPLv3 license 
See http://www.gnu.org/licenses/gpl-3.0.html 
'''
import pygame
import math

# ----------------------------------------------------------------------
class GameObject(pygame.sprite.Sprite):
    '''Base class for all game objects

    Extends the pygame.sprite.Sprite class. 

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

        # For storing previous position, initialize with start position
        self._top_prev, self._left_prev = self.rect.top, self.rect.left

    def __repr__(self):
        '''Returns object representation'''
        return '<{:s} at {:s} x:{:n} y:{:n} dx:{:n} dy:{:n}>'.format(
                self.__class__.__name__,
                hex(id(self)),
                self.rect.top,
                self.rect.left,
                self.dx,
                self.dy)

    def update(self):
        '''Move the object by dx and dy'''
        self._top_prev, self._left_prev = self.rect.top, self.rect.left
        self.rect.move_ip((self.dx, self.dy))

    def rewind(self):
        '''Move object back to previous location'''
        self.rect.top, self.rect.left = self._top_prev, self._left_prev

    def transfer_momentum(self, obj):
        '''Transfer momentum between two colliding objects'''
        # TODO Just a placeholder implementation for now
        self.dx, self.dy, obj.dx, obj.dy = -obj.dx, obj.dy, self.dx, -self.dy

    def get_tangent(self):
        '''Calculate and return tangent from dy/dx'''
        return math.atan2(-self.dy, self.dx)

    def get_angle(self):
        '''Calculate and return object angle of direction'''
        rad = self.get_tangent() % (2*math.pi)
        return (rad, 180*rad/math.pi)

    def get_bounce_angle(self):
        '''Calculate and return bounce angle from tangent'''
        return 2*self.get_tangent() - self.get_angle()

    def get_speed(self):
        '''Calculate and return speed from dx and dy using Pythagoras'''
        return math.hypot(self.dx, self.dy)

    def collide(self, group, **kwargs):
        '''Checks if object collide with object in another sprite group

        Args:
            group  (sprite.Group): Find collision with group member
            dokill (bool): True will remove all sprites that collide from group
            ratio  (float): Scale rects/circles to ratio
        '''
        dokill = kwargs.get('dokill', False)
        ratio = kwargs.get('ratio', 1.0)
        circle = kwargs.get('circle', False)

        if circle:
            hitlist = pygame.sprite.spritecollide(self, group, dokill, 
                            pygame.sprite.collide_circle_ratio(ratio))
        else:
            hitlist = pygame.sprite.spritecollide(self, group, dokill, 
                            pygame.sprite.collide_rect_ratio(ratio))

        return hitlist

    def collide_vert_window_edge(self, width):
        '''Returns True if collision with vertical window edges is detected
        
        Args:
            width (int): Window width
        '''
        collision = False
        if self.rect.left < 0 or self.rect.right > width:
            collision = True
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > width:
                self.rect.right = width
            else:
                pass
        return collision

    def collide_horiz_window_edge(self, height):
        '''Returns True if collision with horizontal window edges is detected
        
        Args:
            height (int): Window height
        '''
        collision = False
        if self.rect.top < 0 or self.rect.bottom > height:
            collision = True
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > height:
                self.rect.bottom = height
            else:
                pass
        return collision
        
    def move_to(self, **kwargs):
        '''Move the object to x and y'''
        if kwargs.get('x', None): 
            self.rect.centerx = kwargs.get('x')
        if kwargs.get('y', None): 
            self.rect.centery = kwargs.get('y')

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
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)
        border (int): Border thickness, default is a filled rectangle

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameRectangle(', kwargs, ')')
        super(GameRectangle, self).__init__(**kwargs)

        pygame.draw.rect(self.image, 
                         kwargs.get('fill', pygame.SRCALPHA), 
                         (0, 0, kwargs.get('width', 1), 
                         kwargs.get('height', 1)),
                         kwargs.get('border', 0))
        
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                        left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameEllipse(GameObject):
    '''Ellipse object
    
    Class for creating elliptical objects.

    Args:
        width (int): Rect width in pixels
        height (int): Rect height in pixels
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Object fill color (optional, default is transparent)
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)
        border (int): Border thickness, default is a filled ellipse

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameEllipse(', kwargs, ')')
        super(GameEllipse, self).__init__(**kwargs)

        pygame.draw.ellipse(self.image, 
                            kwargs.get('fill', pygame.SRCALPHA), 
                            (0, 0, kwargs.get('width', 1), 
                            kwargs.get('height', 1)),
                            kwargs.get('border', 0))
        
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                        left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameCircle(GameObject):
    '''Circle object
    
    Class for creating circular objects.

    Args:
        radius (int): Circle radius
        top (int): Top position (optional, default pos is 0)
        left (int): Left position (optional, default pos is 0)
        fill (pygame.Color): Circle/border fill color (optional, default is gray)
        border (int): Border width (optional, default is a filled circle)
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameCircle(', kwargs, ')')
        self.radius = kwargs.get('radius', 1)
        kwargs['width'] = kwargs['height'] = self.radius*2
        super(GameCircle, self).__init__(**kwargs)

        pygame.draw.circle(self.image, 
                           kwargs.get('fill', pygame.Color(128,128,128)), 
                           (self.radius, self.radius), self.radius, 
                           kwargs.get('border', 0))
        self.rect = self.image.get_rect(top=kwargs.get('top', 0),
                                        left=kwargs.get('left', 0))

# ----------------------------------------------------------------------
class GameLine(GameObject):
    '''Line object
    
    Class for creating line objects.

    Args:
        start_pos (list(int)): 
        end_pos (list(int)):
        line_width (int):
        fill (pygame.Color): Object fill color (optional, default is transparent)
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)

    Attributes:
        image (Surface): object for representing images
        rect  (Rect): object for storing rectangular coordinates
    '''

    def __init__(self, **kwargs):
        print('GameLine(', kwargs, ')')
        kwargs['width'] = kwargs['height'] = max(max(kwargs.get('start_pos', (1, 1))), 
                                                 max(kwargs.get('end_pos', (1, 1))))
        super(GameLine, self).__init__(**kwargs)

        pygame.draw.line(self.image,
                         kwargs.get('fill', pygame.SRCALPHA),
                         kwargs.get('start_pos', (0, 0)),
                         kwargs.get('end_pos', (1, 1)),
                         kwargs.get('line_width', 1))
        
        self.rect = self.image.get_rect()

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
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)

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

        self.rect.top = kwargs.get('top', 0)
        self.rect.left = kwargs.get('left', 0)

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
        '''Set the object to be where the mouse is.'''
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
        dx (int): Speed in x direction (pixels)
        dy (int): Speed in y direction (pixels)

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