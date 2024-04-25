from math import sqrt
from random import choice

from modules.constants import SCREEN_HEIGHT, SCREEN_WIDTH, GRID_SIZE, RES_MULT
from modules.constants import UP, DOWN, LEFT, RIGHT
from modules.constants import Colors

from modules.game import GameObject

import pygame
vec = pygame.math.Vector2


class Particle(GameObject):
    """Particle. Used in some animations. Has its own position,
    size and velocity.
    Dies over certain period of time.
    """

    def __init__(self, pos, preset):
        super().__init__(vec(pos[0] + GRID_SIZE // 2, pos[1] + GRID_SIZE // 2),
                         preset[2])
        self.velocity = vec(preset[0])
        self.size = vec(preset[1])

        # The time period in pygame ticks.
        # (Not iter_counter used in several other animations).
        # If lifetime has expired, particle will be removed
        # from rendering lists.
        self.lifetime = preset[3]

        # The time when particle was created (also in pygame ticks).
        self.timestamp = pygame.time.get_ticks()

        # Flag to indicate if lifetime has not expired.
        self.alive = True

    def move_shrink(self):
        """Move the particle around the screen based on given velocity.
        Make particle smaller, more time it lives - the smaller it gets.
        """
        # Check if the particle is still alive.
        self.alive = max(1 - ((pygame.time.get_ticks() - self.timestamp)
                              / self.lifetime), 0)

        # If so, update its size and position.
        if self.alive:
            self.position += self.velocity
            self.size = self.size * self.alive

    def draw(self, screen):
        """Draw a particle on the screen.
        Update particle's position and size after it has been rendered.
        """
        pygame.draw.rect(screen,
                         self.body_color,
                         (self.position.x,
                          self.position.y,
                          self.size.x,
                          self.size.y)
                         )
        self.move_shrink()


class SearchLight:
    """Beam of light that goes from the head of the snake,
    indicating path the snake will cover if the direction is unchanged.
    """

    def __init__(self, snake):
        self.snake = snake
        self.positions = []

    def draw(self, screen):
        """Draw searchlight on screen."""
        # Clear old positions from the list
        self.positions = []

        head = self.snake.positions[0]
        direction = self.snake.direction

        # Based on a current direction, get all tiles which located
        # between the head and the screen boarder.
        if direction == UP:
            for i in range((head[1] // GRID_SIZE) + 1):
                self.positions.append((head[0], head[1] - i * GRID_SIZE))
        elif direction == DOWN:
            for i in range(((SCREEN_HEIGHT - head[1]) // GRID_SIZE)):
                self.positions.append((head[0], head[1] + i * GRID_SIZE))
        elif direction == LEFT:
            for i in range((head[0] // GRID_SIZE) + 1):
                self.positions.append((head[0] - i * GRID_SIZE, head[1]))
        elif direction == RIGHT:
            for i in range(((SCREEN_WIDTH - head[0]) // GRID_SIZE)):
                self.positions.append((head[0] + i * GRID_SIZE, head[1]))

        # Draw them on screen
        for position in self.positions:
            pygame.draw.rect(screen,
                             Colors.searchlight,
                             (position[0],
                              position[1],
                              GRID_SIZE - 1,
                              GRID_SIZE - 1))


class Bit:
    """Tile. Text in menu screen is made out of this."""

    def __init__(self, point, color_set=Colors.logo_anime, change_colors=True):
        # Coordinates of tile on screen.
        self.point = point

        # Color of the tile. A list, contains all possible colors tile can be
        self.color = choice(color_set)
        self.change_colors = change_colors

        # Direction in which tile is moving around its colors list
        # Positive / negative - movement forward or backward.
        # The number itself - step or increment
        self.direction = 3

    def draw(self, screen, positions=[]):
        """Draw a tile in the screen. Boarder and inside color of tile
        depends on randomness and positions variable respectively.
        """
        # Get current color index in colors list.

        if self.change_colors:
            current_index = Colors.logo_anime.index(self.color)

            if current_index >= len(Colors.logo_anime) - abs(self.direction):
                # If current index is higher than number of colors in list
                # - change direction.
                self.direction = -abs(self.direction)
            elif current_index <= abs(self.direction) - 1:
                # If current index is lower than minimum color
                # - change direction.
                self.direction = abs(self.direction)
            else:
                pass

            # Change color by incrementing index.
            self.color = Colors.logo_anime[current_index + self.direction]

        # If tile is filled, the inside color = boarder color.
        # Else default inside color
        # Which tiles are filled described in positions variable
        inside_color = (self.color if self.point in positions
                        else Colors.tile_inside_color)

        # Draw boarder tile, then inside tile on top.
        # The inside tile is smaller, to make boarder visible.
        pygame.draw.rect(screen,
                         self.color,
                         (self.point[0] - 1,
                          self.point[1] - 1,
                          GRID_SIZE + 1,
                          GRID_SIZE + 1)
                         )
        pygame.draw.rect(screen,
                         inside_color,
                         (self.point[0],
                          self.point[1],
                          GRID_SIZE - 1,
                          GRID_SIZE - 1)
                         )


class TextAnimation:
    """Used to smoothly fill the text on the button with color
    if mouse is over this button.
    """

    def __init__(self, obj, from_, _to, mouse):
        # 'Object' - text on screen. Set of points, representing this object
        self.obj = obj

        self.start = from_  # Frame from which animation is started
        self.stop = _to  # Frame till animation is running

        self.proximity, self.initial, self.delta = self.get_proximity(mouse)

    def get_proximity(self, mouse):
        """Calculating values used in animation."""
        # Get proximity of all points in the object to mouse
        proximity = [(point,
                      sqrt((mouse[0] - point[0]) ** 2
                           + (mouse[1] - point[1]) ** 2))
                     for point in self.obj]

        # Get the closest point, from here the animation will start
        initial = min([point[1] for point in proximity])

        # The difference between the closest and the farthest point.
        # Actually describes how big is the difference between
        # previous and current frame
        delta = max([point[1] for point in proximity]) - initial

        return proximity, initial, delta

    def update(self, iter_counter):
        """Get the next step of animation."""
        # Calculate the fraction, from 0 to 1, this is current
        # stage of animation in percents.
        progress = (iter_counter - self.start) / self.stop + 0.3

        if progress > 1:
            # If animation is complete, return all tiles filled.
            return [apoint[0] for apoint in self.proximity]

        # Else return only tiles which should be filled.
        return [apoint[0] for apoint in self.proximity
                if apoint[1] <= self.initial + self.delta * progress]


class MouseGlow:
    """Highlight tiles that are below the mouse.
    Positions list of those tiles recreates with every frame.
    """

    def __init__(self):
        self.positions = []
        self.fix = 2 if RES_MULT == 1 else 1

    def draw(self, screen, mouse, update_only=False):
        """Draw bright tiles below the mouse current position."""
        # Check if mouse is somewhere on the gamewindow.
        if pygame.mouse.get_focused():
            # If so, proceed.
            pass

        else:
            # If not, reset positions, as they are used by other classes.
            self.positions = []
            # Then quit.
            return

        mouse_x, mouse_y = mouse

        # Get tiles proximity to the mouse.
        tiles = [(x, y, abs(sqrt((mouse_x - x) ** 2 + (mouse_y - y) ** 2)))
                 for x in range(0, SCREEN_WIDTH, GRID_SIZE)
                 for y in range(0, SCREEN_HEIGHT, GRID_SIZE)]

        # Remove tiles that are too far away from mouse.
        glowing_tiles = [tile for tile in tiles if tile[2] < 5 * GRID_SIZE]

        # Get rid of proximity part,
        # as this list will be used in other classes.
        self.positions = [(item[0], item[1]) for item in glowing_tiles]

        if update_only:
            return

        # Draw tiles using proximity value, the closer tile
        # is to the mouse - the brighter is that tile
        for tile in glowing_tiles:
            pygame.draw.rect(screen,
                             (0,
                              max((200 - (tile[2] * self.fix)), 50),
                              0),
                             (tile[0] - 1,
                              tile[1] - 1,
                              GRID_SIZE + 1,
                              GRID_SIZE + 1)
                             )

            pygame.draw.rect(screen,
                             Colors.black,
                             (tile[0], tile[1],
                              GRID_SIZE - 1, GRID_SIZE - 1)
                             )


class Cover(pygame.Rect):
    """Rect to cover end of the grid"""
    def __init__(self,
                 from_x=0,
                 from_y=0,
                 size_x=SCREEN_WIDTH,
                 size_y=GRID_SIZE * 7 - 1
                 ):

        super().__init__(from_x, from_y, size_x, size_y)

    def draw(self, screen):
        """Draw rect"""
        pygame.draw.rect(screen, Colors.black, self)


class ShadowCover(pygame.Surface):
    """Transparent screen for pause or gameover menu"""

    def __init__(self, from_x, from_y, size_x, size_y):
        super().__init__((size_x, size_y))
        self.from_x = from_x
        self.from_y = from_y

        self.set_alpha(128)
        self.fill(Colors.black)

    def draw(self, screen):
        """Draw screen"""
        screen.blit(self, (self.from_x, self.from_y))
