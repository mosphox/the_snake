from random import randint
import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)

BORDER_COLOR = (93, 216, 228)

APPLE_COLOR = (255, 0, 0)

SNAKE_COLOR = (0, 255, 0)

SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

clock = pygame.time.Clock()


class GameObject:
    """ None """
    def __init__(self, position=(0, 0)):
        self.position = position
        self.body_color = None

    def draw(self):
        """ None """
        pass


class Apple(GameObject):
    """ None """
    def __init__(self):
        super().__init__(self)
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """ None """
        self.position = (randint(0, SCREEN_WIDTH) * GRID_SIZE,
                         randint(0, SCREEN_HEIGHT) * GRID_SIZE)

    def draw(self):
        """ None """
        pass


class Snake(GameObject):
    """ None """
    def __init__(self):
        super().__init__(self)
        self.body_color = SNAKE_COLOR
        self.length = 1
        self.direction = RIGHT
        self.next_direction = None

    def update_direction(self):
        """ None """
        pass

    def move(self):
        """ None """
        pass

    def draw(self):
        """ None """
        pass

    def get_head_position(self):
        """ None """
        pass

    def reset(self):
        """ None """
        pass


def handle_keys():
    """ None """
    pass


def main():
    """ None """
    pygame.init()

    while True:
        clock.tick(SPEED)


if __name__ == '__main__':
    main()
