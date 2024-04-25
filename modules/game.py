from random import choice

import pygame

from modules.constants import SCREEN_HEIGHT, SCREEN_WIDTH, GRID_SIZE
from modules.constants import RIGHT
from modules.constants import Colors, ObjPoints


class GameObject:
    """Basic class for in game objects."""

    def __init__(self, position=(0, 0), body_color=Colors.black):
        self.position = position
        self.body_color = body_color

    def draw(self, screen):
        """Draw object on screen surface."""
        raise NotImplementedError('"draw" method is not defined')


class Grid(GameObject):
    """Creating a grid to make outlines between squares."""

    # Define field boarders. 1 pixel wide.
    boarders_grid = [
        (0, 0, SCREEN_WIDTH, 1),
        (0, 0, 1, SCREEN_HEIGHT),
        (SCREEN_WIDTH - 1, 0, SCREEN_WIDTH - 1, SCREEN_HEIGHT),
        (0, SCREEN_HEIGHT - 1, SCREEN_WIDTH, SCREEN_HEIGHT - 1)
    ]

    # Define horizontal lines. 2 pixels wide.
    vertical_grid = [(x - 1, 0, 1, SCREEN_HEIGHT)
                     for x in range(GRID_SIZE, SCREEN_WIDTH, GRID_SIZE)]

    # Define vertical lines. 2 pixels wide.
    horizontal_grid = [(0, y - 1, SCREEN_WIDTH, 1)
                       for y in range(GRID_SIZE, SCREEN_HEIGHT, GRID_SIZE)]

    grid = boarders_grid + vertical_grid + horizontal_grid

    def __init__(self, body_color=Colors.black):
        super().__init__(body_color=body_color)

    def draw(self, screen):
        """Draw a grid based on class defined point sets."""
        for point_set in self.grid:
            pygame.draw.rect(screen, self.body_color, point_set)


class GameGrid(Grid):
    """Creating a grid to make outlines between squares."""

    # Define field boarders. 1 pixel wide.
    boarders_grid = [(0, 7 * GRID_SIZE, 1, SCREEN_HEIGHT),
                     (SCREEN_WIDTH - 1, 7 * GRID_SIZE, SCREEN_WIDTH - 1,
                     SCREEN_HEIGHT),
                     (0, SCREEN_HEIGHT - 1, SCREEN_WIDTH, SCREEN_HEIGHT - 1)
                     ]

    # Define horizontal lines. 2 pixels wide.
    vertical_grid = [(x - 1, 7 * GRID_SIZE, 1, SCREEN_HEIGHT)
                     for x in range(GRID_SIZE, SCREEN_WIDTH, GRID_SIZE)]

    # Define vertical lines. 2 pixels wide.
    horizontal_grid = [(0, y - 1, SCREEN_WIDTH, 1)
                       for y in range(7 * GRID_SIZE, SCREEN_HEIGHT, GRID_SIZE)]

    grid = boarders_grid + vertical_grid + horizontal_grid


class Apple(GameObject):
    """Ingame object, with a position and color"""

    def __init__(self, position=(8 * GRID_SIZE, 8 * GRID_SIZE),
                 body_color=Colors.apple):
        super().__init__(position, body_color)

    def randomize_position(self, snake_positions):
        """Get random position of new apple. Random position cannot be
        inside the snake. Choice is used here, as usual random will be
        really inefficient as snake grows.
        """
        return choice(tuple(ObjPoints.cells - set(snake_positions)))

    def update(self, screen, snake_positions):
        """Check if the snake's head is colliding with apple.
        If so, get new position for an apple and return True for snake.
        """
        if self.position in snake_positions:
            self.position = self.randomize_position(snake_positions)
            self.draw(screen)

            return True

        else:
            # Draw an apple anyway, no matter if snake has eaten it.
            self.draw(screen)

            return False

    def draw(self, screen):
        """Draws an apple on screen."""
        pygame.draw.rect(screen,
                         self.body_color,
                         (self.position[0],
                          self.position[1],
                          GRID_SIZE - 1,
                          GRID_SIZE - 1)
                         )


class Snake(GameObject):
    """The snake itself. Handles movement logic as well as the
    rendering part and movement animations.
    """

    def __init__(self, position=(0, 0), body_color=Colors.snake):
        super().__init__(position, body_color)

        self.direction = RIGHT  # Initial direction is always RIGHT.
        self.next_direction = []  # Queue for next movement commands.

        # Initial positions list. Last 2 cells are never rendered.
        # However, they are used by some of the animation methods.
        # So they do exist here :)
        self.positions = [(10 * GRID_SIZE, 10 * GRID_SIZE),
                          (10 * GRID_SIZE, 11 * GRID_SIZE),
                          (10 * GRID_SIZE, 12 * GRID_SIZE)]

    def update_direction(self, direction):
        """Define a new direction for a snake to move."""
        # Get our current direction.
        # As there is a direction queue, get the last direction from it.
        # If the queue is empty, get current direction.
        facing = (self.next_direction[-1] if self.next_direction
                  else self.direction)
        # This actually allows the snake to turn around without lag.
        # E.g: [LEFT, DOWN] in queue will make
        # the snake take a left turn firstly.
        # And then turn down.

        # Check if we aren't going the opposite way.
        if (abs(facing[0]) == abs(direction[0]) or abs(facing[1])
                == abs(direction[1])):
            return

        # If directions queue isn't too large, append new direction to it.
        if len(self.next_direction) < 2:
            self.next_direction.append(direction)

    def move(self, apple_feast):
        """Move the snake in a given direction."""
        # If there is something in queue, get the first item.
        # First in first out queue, btw.
        if self.next_direction:
            self.direction = self.next_direction.pop(0)

        # Calculate new snake's head position with a fix for screen boarders.
        head = (((self.positions[0][0] + self.direction[0]) % SCREEN_WIDTH,
                 SCREEN_HEIGHT - GRID_SIZE)
                if self.positions[0][1] + self.direction[1] < 7 * GRID_SIZE
                else ((self.positions[0][0]
                       + self.direction[0]) % SCREEN_WIDTH, 7 * GRID_SIZE)
                if self.positions[0][1] + self.direction[1]
                > SCREEN_HEIGHT - GRID_SIZE
                else ((self.positions[0][0] + self.direction[0])
                      % SCREEN_WIDTH,
                      self.positions[0][1] + self.direction[1]))

        # Update positions list. Keep last tile if the snake ate an apple.
        # Else remove it. (tile, not apple).
        if head in self.positions[:-2]:
            return True

        self.positions = ([head] + self.positions if apple_feast
                          else [head] + self.positions[:-1])

    def draw(self, screen, jump):
        """Draw snake animation. Stage of animation depends on a
        frame counter 'jump'.
        """
        # Range is reversed, cause head should be drawn last,
        # in order to appear on top.
        for i in reversed(range(len(self.positions) - 2)):

            # Check if moving tile is at the corner + ignore last 2 tiles
            # as they are not rendered.
            if (self.positions[i][0] - self.positions[i + 2][0] != 0
                    and self.positions[i][1] - self.positions[i + 2][1] != 0
                    and i + 3 != len(self.positions)):
                # If so, draw a ghost tile that should cover ugly animations :)
                pygame.draw.rect(screen,
                                 Colors.snake,
                                 (self.positions[i + 1][0],
                                  self.positions[i + 1][1],
                                  GRID_SIZE - 1,
                                  GRID_SIZE - 1)
                                 )

            # Check if tile is moving outside of screen on X axis.
            if (abs(self.positions[i][0] - self.positions[i + 1][0])
                    == SCREEN_WIDTH - GRID_SIZE):

                # If tile is moving outside left boarder:
                if self.positions[i][0] - self.positions[i + 1][0] > 0:

                    # Create 2 ghost tiles: one moving inside the boarder,
                    # another moving outside from opposite side.
                    positions = [(self.positions[i],
                                  (SCREEN_WIDTH, self.positions[i][1])),
                                 ((-20, self.positions[i][1]),
                                  self.positions[i + 1])]

                # If tile is moving outside right boarder:
                else:
                    positions = [(self.positions[i],
                                  (-20, self.positions[i][1])),
                                 ((SCREEN_WIDTH, self.positions[i][1]),
                                  self.positions[i + 1])]

            # Check if tile is moving outside of screen on Y axis.
            elif (abs(self.positions[i][1] - self.positions[i + 1][1])
                  == SCREEN_HEIGHT - GRID_SIZE - (7 * GRID_SIZE)):

                # If tile is moving outside top boarder:
                if self.positions[i][1] - self.positions[i + 1][1] > 0:
                    positions = [(self.positions[i],
                                  (self.positions[i][0], SCREEN_HEIGHT)),
                                 ((self.positions[i][0], GRID_SIZE * 6),
                                  self.positions[i + 1])]

                # If tile is moving outside bottom boarder:
                else:
                    positions = [(self.positions[i],
                                  (self.positions[i][0], GRID_SIZE * 6)),
                                 ((self.positions[i][0], SCREEN_HEIGHT),
                                  self.positions[i + 1])]

            # If tile is moving on screen, no boarders stuff:
            else:
                # Set to positions: where the tile was before and where
                # the tile should appear.
                positions = [(self.positions[i], self.positions[i + 1])]

            # Change color to snake head color, if i = 0, as i = 0 is a head.
            color = Colors.snake if i else Colors.snake_head

            for position in positions:
                # For every position in list draw
                # animation based on animation stage.
                pygame.draw.rect(
                    screen,
                    color,
                    (((position[0][0] - position[1][0])
                      * min((jump + 1) / 6, 1)) + position[1][0],
                     ((position[0][1] - position[1][1])
                      * min((jump + 1) / 6, 1)) + position[1][1],
                     GRID_SIZE - 1,
                     GRID_SIZE - 1)
                )

        # Increment animation stage.
        return jump + 1
