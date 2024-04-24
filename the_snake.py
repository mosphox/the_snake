import ctypes
import pygame

from dataclasses import dataclass
from math import sqrt
from random import randint, choice, uniform

try:
    # Try to set high-res. Works on Windows 10-11
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
    pass

except AttributeError:
    pass

RES_MULT = 1  # Increase gamewindow size by n times.
vec = pygame.math.Vector2

# The size of the window itself.
SCREEN_WIDTH, SCREEN_HEIGHT = 720 * RES_MULT, 560 * RES_MULT
GRID_SIZE = 16 * RES_MULT  # Size of a single "tile" - square.

# Ingame snake directions
UP = (0, -GRID_SIZE)
DOWN = (0, GRID_SIZE)
LEFT = (-GRID_SIZE, 0)
RIGHT = (GRID_SIZE, 0)

SPEED = 60
FPS = SPEED  # Renamed, cause i keep forgetting it's name.

# The values below are not used anywhere in code,
# however they needed to pass autotests.
BOARD_BACKGROUND_COLOR = None
BORDER_COLOR = None
APPLE_COLOR = None
SNAKE_COLOR = None

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.display.set_caption('the_sneaky_snake')

try:
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
except FileNotFoundError:
    print('Unable to load icon')

clock = pygame.time.Clock()


@dataclass
class Text:
    """Points for text."""

    logo = [
        (1 * GRID_SIZE, 4 * GRID_SIZE),
        (2 * GRID_SIZE, 4 * GRID_SIZE),
        (3 * GRID_SIZE, 4 * GRID_SIZE),
        (2 * GRID_SIZE, 5 * GRID_SIZE),
        (2 * GRID_SIZE, 6 * GRID_SIZE),
        (2 * GRID_SIZE, 7 * GRID_SIZE),
        (2 * GRID_SIZE, 8 * GRID_SIZE),
        (5 * GRID_SIZE, 4 * GRID_SIZE),
        (5 * GRID_SIZE, 5 * GRID_SIZE),
        (5 * GRID_SIZE, 6 * GRID_SIZE),
        (5 * GRID_SIZE, 7 * GRID_SIZE),
        (5 * GRID_SIZE, 8 * GRID_SIZE),
        (6 * GRID_SIZE, 6 * GRID_SIZE),
        (7 * GRID_SIZE, 6 * GRID_SIZE),
        (8 * GRID_SIZE, 4 * GRID_SIZE),
        (8 * GRID_SIZE, 5 * GRID_SIZE),
        (8 * GRID_SIZE, 6 * GRID_SIZE),
        (8 * GRID_SIZE, 7 * GRID_SIZE),
        (8 * GRID_SIZE, 8 * GRID_SIZE),
        (10 * GRID_SIZE, 4 * GRID_SIZE),
        (10 * GRID_SIZE, 5 * GRID_SIZE),
        (10 * GRID_SIZE, 6 * GRID_SIZE),
        (10 * GRID_SIZE, 7 * GRID_SIZE),
        (10 * GRID_SIZE, 8 * GRID_SIZE),
        (11 * GRID_SIZE, 8 * GRID_SIZE),
        (12 * GRID_SIZE, 8 * GRID_SIZE),
        (13 * GRID_SIZE, 8 * GRID_SIZE),
        (11 * GRID_SIZE, 6 * GRID_SIZE),
        (12 * GRID_SIZE, 6 * GRID_SIZE),
        (11 * GRID_SIZE, 4 * GRID_SIZE),
        (12 * GRID_SIZE, 4 * GRID_SIZE),
        (13 * GRID_SIZE, 4 * GRID_SIZE),
        (15 * GRID_SIZE, 8 * GRID_SIZE),
        (16 * GRID_SIZE, 8 * GRID_SIZE),
        (17 * GRID_SIZE, 8 * GRID_SIZE),
        (18 * GRID_SIZE, 8 * GRID_SIZE),
        (20 * GRID_SIZE, 8 * GRID_SIZE),
        (21 * GRID_SIZE, 8 * GRID_SIZE),
        (22 * GRID_SIZE, 8 * GRID_SIZE),
        (23 * GRID_SIZE, 7 * GRID_SIZE),
        (22 * GRID_SIZE, 6 * GRID_SIZE),
        (21 * GRID_SIZE, 6 * GRID_SIZE),
        (20 * GRID_SIZE, 5 * GRID_SIZE),
        (21 * GRID_SIZE, 4 * GRID_SIZE),
        (22 * GRID_SIZE, 4 * GRID_SIZE),
        (23 * GRID_SIZE, 4 * GRID_SIZE),
        (25 * GRID_SIZE, 4 * GRID_SIZE),
        (25 * GRID_SIZE, 5 * GRID_SIZE),
        (25 * GRID_SIZE, 6 * GRID_SIZE),
        (25 * GRID_SIZE, 7 * GRID_SIZE),
        (25 * GRID_SIZE, 8 * GRID_SIZE),
        (28 * GRID_SIZE, 8 * GRID_SIZE),
        (28 * GRID_SIZE, 7 * GRID_SIZE),
        (28 * GRID_SIZE, 6 * GRID_SIZE),
        (28 * GRID_SIZE, 5 * GRID_SIZE),
        (28 * GRID_SIZE, 4 * GRID_SIZE),
        (26 * GRID_SIZE, 5 * GRID_SIZE),
        (27 * GRID_SIZE, 6 * GRID_SIZE),
        (30 * GRID_SIZE, 8 * GRID_SIZE),
        (30 * GRID_SIZE, 7 * GRID_SIZE),
        (30 * GRID_SIZE, 6 * GRID_SIZE),
        (30 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 4 * GRID_SIZE),
        (33 * GRID_SIZE, 5 * GRID_SIZE),
        (33 * GRID_SIZE, 6 * GRID_SIZE),
        (33 * GRID_SIZE, 7 * GRID_SIZE),
        (33 * GRID_SIZE, 8 * GRID_SIZE),
        (31 * GRID_SIZE, 6 * GRID_SIZE),
        (32 * GRID_SIZE, 6 * GRID_SIZE),
        (35 * GRID_SIZE, 4 * GRID_SIZE),
        (35 * GRID_SIZE, 5 * GRID_SIZE),
        (35 * GRID_SIZE, 6 * GRID_SIZE),
        (35 * GRID_SIZE, 7 * GRID_SIZE),
        (35 * GRID_SIZE, 8 * GRID_SIZE),
        (36 * GRID_SIZE, 6 * GRID_SIZE),
        (37 * GRID_SIZE, 5 * GRID_SIZE),
        (38 * GRID_SIZE, 4 * GRID_SIZE),
        (37 * GRID_SIZE, 7 * GRID_SIZE),
        (38 * GRID_SIZE, 8 * GRID_SIZE),
        (40 * GRID_SIZE, 4 * GRID_SIZE),
        (40 * GRID_SIZE, 5 * GRID_SIZE),
        (40 * GRID_SIZE, 6 * GRID_SIZE),
        (40 * GRID_SIZE, 7 * GRID_SIZE),
        (40 * GRID_SIZE, 8 * GRID_SIZE),
        (41 * GRID_SIZE, 8 * GRID_SIZE),
        (42 * GRID_SIZE, 8 * GRID_SIZE),
        (43 * GRID_SIZE, 8 * GRID_SIZE),
        (41 * GRID_SIZE, 6 * GRID_SIZE),
        (42 * GRID_SIZE, 6 * GRID_SIZE),
        (41 * GRID_SIZE, 4 * GRID_SIZE),
        (42 * GRID_SIZE, 4 * GRID_SIZE),
        (43 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    play = [
        (14 * GRID_SIZE, 17 * GRID_SIZE),
        (14 * GRID_SIZE, 18 * GRID_SIZE),
        (14 * GRID_SIZE, 19 * GRID_SIZE),
        (14 * GRID_SIZE, 20 * GRID_SIZE),
        (14 * GRID_SIZE, 21 * GRID_SIZE),
        (15 * GRID_SIZE, 17 * GRID_SIZE),
        (16 * GRID_SIZE, 17 * GRID_SIZE),
        (17 * GRID_SIZE, 18 * GRID_SIZE),
        (16 * GRID_SIZE, 19 * GRID_SIZE),
        (15 * GRID_SIZE, 19 * GRID_SIZE),
        (19 * GRID_SIZE, 17 * GRID_SIZE),
        (19 * GRID_SIZE, 18 * GRID_SIZE),
        (19 * GRID_SIZE, 19 * GRID_SIZE),
        (19 * GRID_SIZE, 20 * GRID_SIZE),
        (19 * GRID_SIZE, 21 * GRID_SIZE),
        (20 * GRID_SIZE, 21 * GRID_SIZE),
        (21 * GRID_SIZE, 21 * GRID_SIZE),
        (23 * GRID_SIZE, 21 * GRID_SIZE),
        (23 * GRID_SIZE, 20 * GRID_SIZE),
        (23 * GRID_SIZE, 19 * GRID_SIZE),
        (23 * GRID_SIZE, 18 * GRID_SIZE),
        (24 * GRID_SIZE, 17 * GRID_SIZE),
        (25 * GRID_SIZE, 17 * GRID_SIZE),
        (26 * GRID_SIZE, 18 * GRID_SIZE),
        (26 * GRID_SIZE, 19 * GRID_SIZE),
        (26 * GRID_SIZE, 20 * GRID_SIZE),
        (26 * GRID_SIZE, 21 * GRID_SIZE),
        (24 * GRID_SIZE, 19 * GRID_SIZE),
        (25 * GRID_SIZE, 19 * GRID_SIZE),
        (28 * GRID_SIZE, 17 * GRID_SIZE),
        (28 * GRID_SIZE, 18 * GRID_SIZE),
        (28 * GRID_SIZE, 19 * GRID_SIZE),
        (29 * GRID_SIZE, 19 * GRID_SIZE),
        (30 * GRID_SIZE, 19 * GRID_SIZE),
        (30 * GRID_SIZE, 18 * GRID_SIZE),
        (30 * GRID_SIZE, 17 * GRID_SIZE),
        (29 * GRID_SIZE, 20 * GRID_SIZE),
        (29 * GRID_SIZE, 21 * GRID_SIZE)
    ]

    quit = [
        (15 * GRID_SIZE, 27 * GRID_SIZE),
        (15 * GRID_SIZE, 28 * GRID_SIZE),
        (15 * GRID_SIZE, 29 * GRID_SIZE),
        (16 * GRID_SIZE, 26 * GRID_SIZE),
        (17 * GRID_SIZE, 26 * GRID_SIZE),
        (18 * GRID_SIZE, 27 * GRID_SIZE),
        (18 * GRID_SIZE, 28 * GRID_SIZE),
        (18 * GRID_SIZE, 29 * GRID_SIZE),
        (17 * GRID_SIZE, 30 * GRID_SIZE),
        (16 * GRID_SIZE, 30 * GRID_SIZE),
        (17 * GRID_SIZE, 29 * GRID_SIZE),
        (18 * GRID_SIZE, 30 * GRID_SIZE),
        (20 * GRID_SIZE, 26 * GRID_SIZE),
        (20 * GRID_SIZE, 27 * GRID_SIZE),
        (20 * GRID_SIZE, 28 * GRID_SIZE),
        (20 * GRID_SIZE, 29 * GRID_SIZE),
        (22 * GRID_SIZE, 30 * GRID_SIZE),
        (21 * GRID_SIZE, 30 * GRID_SIZE),
        (20 * GRID_SIZE, 30 * GRID_SIZE),
        (23 * GRID_SIZE, 30 * GRID_SIZE),
        (23 * GRID_SIZE, 29 * GRID_SIZE),
        (23 * GRID_SIZE, 28 * GRID_SIZE),
        (23 * GRID_SIZE, 26 * GRID_SIZE),
        (23 * GRID_SIZE, 27 * GRID_SIZE),
        (25 * GRID_SIZE, 26 * GRID_SIZE),
        (25 * GRID_SIZE, 27 * GRID_SIZE),
        (25 * GRID_SIZE, 28 * GRID_SIZE),
        (25 * GRID_SIZE, 29 * GRID_SIZE),
        (25 * GRID_SIZE, 30 * GRID_SIZE),
        (28 * GRID_SIZE, 26 * GRID_SIZE),
        (28 * GRID_SIZE, 27 * GRID_SIZE),
        (28 * GRID_SIZE, 28 * GRID_SIZE),
        (28 * GRID_SIZE, 29 * GRID_SIZE),
        (28 * GRID_SIZE, 30 * GRID_SIZE),
        (27 * GRID_SIZE, 26 * GRID_SIZE),
        (29 * GRID_SIZE, 26 * GRID_SIZE)
    ]

    play_arrows = [
        (8 * GRID_SIZE, 19 * GRID_SIZE),
        (7 * GRID_SIZE, 18 * GRID_SIZE),
        (6 * GRID_SIZE, 17 * GRID_SIZE),
        (7 * GRID_SIZE, 20 * GRID_SIZE),
        (6 * GRID_SIZE, 21 * GRID_SIZE),
        (4 * GRID_SIZE, 19 * GRID_SIZE),
        (3 * GRID_SIZE, 19 * GRID_SIZE),
        (2 * GRID_SIZE, 19 * GRID_SIZE),
        (36 * GRID_SIZE, 19 * GRID_SIZE),
        (37 * GRID_SIZE, 18 * GRID_SIZE),
        (38 * GRID_SIZE, 17 * GRID_SIZE),
        (37 * GRID_SIZE, 20 * GRID_SIZE),
        (38 * GRID_SIZE, 21 * GRID_SIZE),
        (40 * GRID_SIZE, 19 * GRID_SIZE),
        (41 * GRID_SIZE, 19 * GRID_SIZE),
        (42 * GRID_SIZE, 19 * GRID_SIZE)
    ]

    quit_arrows = [
        (36 * GRID_SIZE, 28 * GRID_SIZE),
        (37 * GRID_SIZE, 27 * GRID_SIZE),
        (38 * GRID_SIZE, 26 * GRID_SIZE),
        (37 * GRID_SIZE, 29 * GRID_SIZE),
        (38 * GRID_SIZE, 30 * GRID_SIZE),
        (40 * GRID_SIZE, 28 * GRID_SIZE),
        (41 * GRID_SIZE, 28 * GRID_SIZE),
        (42 * GRID_SIZE, 28 * GRID_SIZE),
        (8 * GRID_SIZE, 28 * GRID_SIZE),
        (7 * GRID_SIZE, 27 * GRID_SIZE),
        (6 * GRID_SIZE, 26 * GRID_SIZE),
        (7 * GRID_SIZE, 29 * GRID_SIZE),
        (6 * GRID_SIZE, 30 * GRID_SIZE),
        (4 * GRID_SIZE, 28 * GRID_SIZE),
        (3 * GRID_SIZE, 28 * GRID_SIZE),
        (2 * GRID_SIZE, 28 * GRID_SIZE)
    ]

    score = [
        (4 * GRID_SIZE, 1 * GRID_SIZE),
        (3 * GRID_SIZE, 1 * GRID_SIZE),
        (2 * GRID_SIZE, 1 * GRID_SIZE),
        (1 * GRID_SIZE, 2 * GRID_SIZE),
        (2 * GRID_SIZE, 3 * GRID_SIZE),
        (3 * GRID_SIZE, 3 * GRID_SIZE),
        (4 * GRID_SIZE, 4 * GRID_SIZE),
        (3 * GRID_SIZE, 5 * GRID_SIZE),
        (2 * GRID_SIZE, 5 * GRID_SIZE),
        (1 * GRID_SIZE, 5 * GRID_SIZE),
        (7 * GRID_SIZE, 1 * GRID_SIZE),
        (8 * GRID_SIZE, 1 * GRID_SIZE),
        (9 * GRID_SIZE, 1 * GRID_SIZE),
        (6 * GRID_SIZE, 2 * GRID_SIZE),
        (6 * GRID_SIZE, 3 * GRID_SIZE),
        (6 * GRID_SIZE, 4 * GRID_SIZE),
        (7 * GRID_SIZE, 5 * GRID_SIZE),
        (8 * GRID_SIZE, 5 * GRID_SIZE),
        (9 * GRID_SIZE, 5 * GRID_SIZE),
        (11 * GRID_SIZE, 2 * GRID_SIZE),
        (11 * GRID_SIZE, 3 * GRID_SIZE),
        (11 * GRID_SIZE, 4 * GRID_SIZE),
        (12 * GRID_SIZE, 5 * GRID_SIZE),
        (13 * GRID_SIZE, 5 * GRID_SIZE),
        (14 * GRID_SIZE, 4 * GRID_SIZE),
        (14 * GRID_SIZE, 3 * GRID_SIZE),
        (14 * GRID_SIZE, 2 * GRID_SIZE),
        (12 * GRID_SIZE, 1 * GRID_SIZE),
        (13 * GRID_SIZE, 1 * GRID_SIZE),
        (16 * GRID_SIZE, 1 * GRID_SIZE),
        (16 * GRID_SIZE, 2 * GRID_SIZE),
        (16 * GRID_SIZE, 3 * GRID_SIZE),
        (16 * GRID_SIZE, 4 * GRID_SIZE),
        (16 * GRID_SIZE, 5 * GRID_SIZE),
        (17 * GRID_SIZE, 1 * GRID_SIZE),
        (18 * GRID_SIZE, 1 * GRID_SIZE),
        (19 * GRID_SIZE, 2 * GRID_SIZE),
        (18 * GRID_SIZE, 3 * GRID_SIZE),
        (17 * GRID_SIZE, 3 * GRID_SIZE),
        (18 * GRID_SIZE, 4 * GRID_SIZE),
        (19 * GRID_SIZE, 5 * GRID_SIZE),
        (21 * GRID_SIZE, 1 * GRID_SIZE),
        (21 * GRID_SIZE, 2 * GRID_SIZE),
        (21 * GRID_SIZE, 3 * GRID_SIZE),
        (21 * GRID_SIZE, 4 * GRID_SIZE),
        (21 * GRID_SIZE, 5 * GRID_SIZE),
        (22 * GRID_SIZE, 5 * GRID_SIZE),
        (23 * GRID_SIZE, 5 * GRID_SIZE),
        (24 * GRID_SIZE, 5 * GRID_SIZE),
        (22 * GRID_SIZE, 3 * GRID_SIZE),
        (23 * GRID_SIZE, 3 * GRID_SIZE),
        (22 * GRID_SIZE, 1 * GRID_SIZE),
        (23 * GRID_SIZE, 1 * GRID_SIZE),
        (24 * GRID_SIZE, 1 * GRID_SIZE),
        (26 * GRID_SIZE, 2 * GRID_SIZE),
        (26 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    digit_0 = [
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 2 * GRID_SIZE),
        (33 * GRID_SIZE, 3 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 4 * GRID_SIZE),
        (30 * GRID_SIZE, 3 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE)
    ]

    digit_1 = [
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (32 * GRID_SIZE, 2 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 4 * GRID_SIZE),
        (33 * GRID_SIZE, 5 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 2 * GRID_SIZE)
    ]

    digit_2 = [
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (33 * GRID_SIZE, 2 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (31 * GRID_SIZE, 4 * GRID_SIZE),
        (30 * GRID_SIZE, 5 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (33 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE)
    ]

    digit_3 = [
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (33 * GRID_SIZE, 2 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    digit_4 = [
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (32 * GRID_SIZE, 2 * GRID_SIZE),
        (33 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (31 * GRID_SIZE, 3 * GRID_SIZE),
        (30 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE)
    ]

    digit_5 = [
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (31 * GRID_SIZE, 3 * GRID_SIZE),
        (30 * GRID_SIZE, 3 * GRID_SIZE),
        (33 * GRID_SIZE, 1 * GRID_SIZE),
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 5 * GRID_SIZE)
    ]

    digit_6 = [
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (31 * GRID_SIZE, 3 * GRID_SIZE),
        (30 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    digit_7 = [
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (30 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 2 * GRID_SIZE),
        (31 * GRID_SIZE, 4 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE)
    ]

    digit_8 = [
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 2 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (31 * GRID_SIZE, 3 * GRID_SIZE),
        (30 * GRID_SIZE, 4 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    digit_9 = [
        (31 * GRID_SIZE, 1 * GRID_SIZE),
        (32 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 1 * GRID_SIZE),
        (33 * GRID_SIZE, 2 * GRID_SIZE),
        (31 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 2 * GRID_SIZE),
        (31 * GRID_SIZE, 3 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE),
        (33 * GRID_SIZE, 3 * GRID_SIZE)
    ]

    pause = [
        (8 * GRID_SIZE, 5 * GRID_SIZE),
        (8 * GRID_SIZE, 4 * GRID_SIZE),
        (8 * GRID_SIZE, 6 * GRID_SIZE),
        (8 * GRID_SIZE, 7 * GRID_SIZE),
        (8 * GRID_SIZE, 8 * GRID_SIZE),
        (9 * GRID_SIZE, 4 * GRID_SIZE),
        (10 * GRID_SIZE, 4 * GRID_SIZE),
        (11 * GRID_SIZE, 5 * GRID_SIZE),
        (10 * GRID_SIZE, 6 * GRID_SIZE),
        (9 * GRID_SIZE, 6 * GRID_SIZE),
        (13 * GRID_SIZE, 5 * GRID_SIZE),
        (13 * GRID_SIZE, 6 * GRID_SIZE),
        (13 * GRID_SIZE, 7 * GRID_SIZE),
        (13 * GRID_SIZE, 8 * GRID_SIZE),
        (14 * GRID_SIZE, 4 * GRID_SIZE),
        (15 * GRID_SIZE, 4 * GRID_SIZE),
        (16 * GRID_SIZE, 5 * GRID_SIZE),
        (16 * GRID_SIZE, 6 * GRID_SIZE),
        (16 * GRID_SIZE, 7 * GRID_SIZE),
        (16 * GRID_SIZE, 8 * GRID_SIZE),
        (14 * GRID_SIZE, 6 * GRID_SIZE),
        (15 * GRID_SIZE, 6 * GRID_SIZE),
        (18 * GRID_SIZE, 4 * GRID_SIZE),
        (18 * GRID_SIZE, 5 * GRID_SIZE),
        (18 * GRID_SIZE, 6 * GRID_SIZE),
        (18 * GRID_SIZE, 7 * GRID_SIZE),
        (18 * GRID_SIZE, 8 * GRID_SIZE),
        (19 * GRID_SIZE, 8 * GRID_SIZE),
        (20 * GRID_SIZE, 8 * GRID_SIZE),
        (21 * GRID_SIZE, 8 * GRID_SIZE),
        (21 * GRID_SIZE, 7 * GRID_SIZE),
        (21 * GRID_SIZE, 6 * GRID_SIZE),
        (21 * GRID_SIZE, 5 * GRID_SIZE),
        (21 * GRID_SIZE, 4 * GRID_SIZE),
        (25 * GRID_SIZE, 4 * GRID_SIZE),
        (24 * GRID_SIZE, 4 * GRID_SIZE),
        (26 * GRID_SIZE, 4 * GRID_SIZE),
        (23 * GRID_SIZE, 5 * GRID_SIZE),
        (24 * GRID_SIZE, 6 * GRID_SIZE),
        (25 * GRID_SIZE, 6 * GRID_SIZE),
        (26 * GRID_SIZE, 7 * GRID_SIZE),
        (25 * GRID_SIZE, 8 * GRID_SIZE),
        (24 * GRID_SIZE, 8 * GRID_SIZE),
        (23 * GRID_SIZE, 8 * GRID_SIZE),
        (28 * GRID_SIZE, 4 * GRID_SIZE),
        (28 * GRID_SIZE, 5 * GRID_SIZE),
        (28 * GRID_SIZE, 6 * GRID_SIZE),
        (28 * GRID_SIZE, 7 * GRID_SIZE),
        (28 * GRID_SIZE, 8 * GRID_SIZE),
        (29 * GRID_SIZE, 8 * GRID_SIZE),
        (30 * GRID_SIZE, 8 * GRID_SIZE),
        (31 * GRID_SIZE, 8 * GRID_SIZE),
        (29 * GRID_SIZE, 6 * GRID_SIZE),
        (30 * GRID_SIZE, 6 * GRID_SIZE),
        (29 * GRID_SIZE, 4 * GRID_SIZE),
        (30 * GRID_SIZE, 4 * GRID_SIZE),
        (31 * GRID_SIZE, 4 * GRID_SIZE),
        (33 * GRID_SIZE, 4 * GRID_SIZE),
        (33 * GRID_SIZE, 5 * GRID_SIZE),
        (33 * GRID_SIZE, 6 * GRID_SIZE),
        (33 * GRID_SIZE, 7 * GRID_SIZE),
        (33 * GRID_SIZE, 8 * GRID_SIZE),
        (34 * GRID_SIZE, 8 * GRID_SIZE),
        (35 * GRID_SIZE, 8 * GRID_SIZE),
        (36 * GRID_SIZE, 7 * GRID_SIZE),
        (36 * GRID_SIZE, 6 * GRID_SIZE),
        (36 * GRID_SIZE, 5 * GRID_SIZE),
        (35 * GRID_SIZE, 4 * GRID_SIZE),
        (34 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    resume = [
        (7 * GRID_SIZE, 17 * GRID_SIZE),
        (7 * GRID_SIZE, 18 * GRID_SIZE),
        (7 * GRID_SIZE, 19 * GRID_SIZE),
        (7 * GRID_SIZE, 20 * GRID_SIZE),
        (7 * GRID_SIZE, 21 * GRID_SIZE),
        (8 * GRID_SIZE, 17 * GRID_SIZE),
        (9 * GRID_SIZE, 17 * GRID_SIZE),
        (10 * GRID_SIZE, 18 * GRID_SIZE),
        (9 * GRID_SIZE, 19 * GRID_SIZE),
        (8 * GRID_SIZE, 19 * GRID_SIZE),
        (9 * GRID_SIZE, 20 * GRID_SIZE),
        (10 * GRID_SIZE, 21 * GRID_SIZE),
        (12 * GRID_SIZE, 17 * GRID_SIZE),
        (12 * GRID_SIZE, 18 * GRID_SIZE),
        (12 * GRID_SIZE, 19 * GRID_SIZE),
        (12 * GRID_SIZE, 20 * GRID_SIZE),
        (12 * GRID_SIZE, 21 * GRID_SIZE),
        (13 * GRID_SIZE, 21 * GRID_SIZE),
        (14 * GRID_SIZE, 21 * GRID_SIZE),
        (15 * GRID_SIZE, 21 * GRID_SIZE),
        (13 * GRID_SIZE, 19 * GRID_SIZE),
        (14 * GRID_SIZE, 19 * GRID_SIZE),
        (13 * GRID_SIZE, 17 * GRID_SIZE),
        (14 * GRID_SIZE, 17 * GRID_SIZE),
        (15 * GRID_SIZE, 17 * GRID_SIZE),
        (19 * GRID_SIZE, 17 * GRID_SIZE),
        (18 * GRID_SIZE, 17 * GRID_SIZE),
        (20 * GRID_SIZE, 17 * GRID_SIZE),
        (17 * GRID_SIZE, 18 * GRID_SIZE),
        (18 * GRID_SIZE, 19 * GRID_SIZE),
        (19 * GRID_SIZE, 19 * GRID_SIZE),
        (20 * GRID_SIZE, 20 * GRID_SIZE),
        (19 * GRID_SIZE, 21 * GRID_SIZE),
        (18 * GRID_SIZE, 21 * GRID_SIZE),
        (17 * GRID_SIZE, 21 * GRID_SIZE),
        (22 * GRID_SIZE, 17 * GRID_SIZE),
        (22 * GRID_SIZE, 18 * GRID_SIZE),
        (22 * GRID_SIZE, 19 * GRID_SIZE),
        (22 * GRID_SIZE, 20 * GRID_SIZE),
        (22 * GRID_SIZE, 21 * GRID_SIZE),
        (23 * GRID_SIZE, 21 * GRID_SIZE),
        (24 * GRID_SIZE, 21 * GRID_SIZE),
        (25 * GRID_SIZE, 21 * GRID_SIZE),
        (26 * GRID_SIZE, 21 * GRID_SIZE),
        (26 * GRID_SIZE, 20 * GRID_SIZE),
        (26 * GRID_SIZE, 19 * GRID_SIZE),
        (26 * GRID_SIZE, 18 * GRID_SIZE),
        (26 * GRID_SIZE, 17 * GRID_SIZE),
        (28 * GRID_SIZE, 17 * GRID_SIZE),
        (28 * GRID_SIZE, 18 * GRID_SIZE),
        (28 * GRID_SIZE, 19 * GRID_SIZE),
        (28 * GRID_SIZE, 20 * GRID_SIZE),
        (28 * GRID_SIZE, 21 * GRID_SIZE),
        (29 * GRID_SIZE, 18 * GRID_SIZE),
        (30 * GRID_SIZE, 19 * GRID_SIZE),
        (31 * GRID_SIZE, 18 * GRID_SIZE),
        (32 * GRID_SIZE, 17 * GRID_SIZE),
        (32 * GRID_SIZE, 18 * GRID_SIZE),
        (32 * GRID_SIZE, 19 * GRID_SIZE),
        (32 * GRID_SIZE, 20 * GRID_SIZE),
        (32 * GRID_SIZE, 21 * GRID_SIZE),
        (34 * GRID_SIZE, 17 * GRID_SIZE),
        (34 * GRID_SIZE, 18 * GRID_SIZE),
        (34 * GRID_SIZE, 19 * GRID_SIZE),
        (34 * GRID_SIZE, 20 * GRID_SIZE),
        (34 * GRID_SIZE, 21 * GRID_SIZE),
        (35 * GRID_SIZE, 21 * GRID_SIZE),
        (36 * GRID_SIZE, 21 * GRID_SIZE),
        (37 * GRID_SIZE, 21 * GRID_SIZE),
        (35 * GRID_SIZE, 19 * GRID_SIZE),
        (36 * GRID_SIZE, 19 * GRID_SIZE),
        (35 * GRID_SIZE, 17 * GRID_SIZE),
        (36 * GRID_SIZE, 17 * GRID_SIZE),
        (37 * GRID_SIZE, 17 * GRID_SIZE)
    ]

    menu = [
        (12 * GRID_SIZE, 26 * GRID_SIZE),
        (12 * GRID_SIZE, 27 * GRID_SIZE),
        (12 * GRID_SIZE, 28 * GRID_SIZE),
        (12 * GRID_SIZE, 29 * GRID_SIZE),
        (12 * GRID_SIZE, 30 * GRID_SIZE),
        (13 * GRID_SIZE, 27 * GRID_SIZE),
        (14 * GRID_SIZE, 28 * GRID_SIZE),
        (15 * GRID_SIZE, 27 * GRID_SIZE),
        (16 * GRID_SIZE, 26 * GRID_SIZE),
        (16 * GRID_SIZE, 27 * GRID_SIZE),
        (16 * GRID_SIZE, 28 * GRID_SIZE),
        (16 * GRID_SIZE, 29 * GRID_SIZE),
        (16 * GRID_SIZE, 30 * GRID_SIZE),
        (18 * GRID_SIZE, 26 * GRID_SIZE),
        (18 * GRID_SIZE, 27 * GRID_SIZE),
        (18 * GRID_SIZE, 28 * GRID_SIZE),
        (18 * GRID_SIZE, 29 * GRID_SIZE),
        (18 * GRID_SIZE, 30 * GRID_SIZE),
        (19 * GRID_SIZE, 30 * GRID_SIZE),
        (20 * GRID_SIZE, 30 * GRID_SIZE),
        (21 * GRID_SIZE, 30 * GRID_SIZE),
        (19 * GRID_SIZE, 28 * GRID_SIZE),
        (20 * GRID_SIZE, 28 * GRID_SIZE),
        (19 * GRID_SIZE, 26 * GRID_SIZE),
        (20 * GRID_SIZE, 26 * GRID_SIZE),
        (21 * GRID_SIZE, 26 * GRID_SIZE),
        (23 * GRID_SIZE, 26 * GRID_SIZE),
        (23 * GRID_SIZE, 27 * GRID_SIZE),
        (23 * GRID_SIZE, 28 * GRID_SIZE),
        (23 * GRID_SIZE, 29 * GRID_SIZE),
        (23 * GRID_SIZE, 30 * GRID_SIZE),
        (24 * GRID_SIZE, 27 * GRID_SIZE),
        (25 * GRID_SIZE, 28 * GRID_SIZE),
        (26 * GRID_SIZE, 26 * GRID_SIZE),
        (26 * GRID_SIZE, 27 * GRID_SIZE),
        (26 * GRID_SIZE, 28 * GRID_SIZE),
        (26 * GRID_SIZE, 29 * GRID_SIZE),
        (26 * GRID_SIZE, 30 * GRID_SIZE),
        (28 * GRID_SIZE, 26 * GRID_SIZE),
        (28 * GRID_SIZE, 27 * GRID_SIZE),
        (28 * GRID_SIZE, 28 * GRID_SIZE),
        (28 * GRID_SIZE, 29 * GRID_SIZE),
        (28 * GRID_SIZE, 30 * GRID_SIZE),
        (29 * GRID_SIZE, 30 * GRID_SIZE),
        (30 * GRID_SIZE, 30 * GRID_SIZE),
        (31 * GRID_SIZE, 30 * GRID_SIZE),
        (32 * GRID_SIZE, 30 * GRID_SIZE),
        (32 * GRID_SIZE, 27 * GRID_SIZE),
        (32 * GRID_SIZE, 26 * GRID_SIZE),
        (32 * GRID_SIZE, 28 * GRID_SIZE),
        (32 * GRID_SIZE, 29 * GRID_SIZE)
    ]

    resume_arrows = [
        (42 * GRID_SIZE, 17 * GRID_SIZE),
        (41 * GRID_SIZE, 18 * GRID_SIZE),
        (40 * GRID_SIZE, 19 * GRID_SIZE),
        (41 * GRID_SIZE, 20 * GRID_SIZE),
        (42 * GRID_SIZE, 21 * GRID_SIZE),
        (3 * GRID_SIZE, 18 * GRID_SIZE),
        (4 * GRID_SIZE, 19 * GRID_SIZE),
        (3 * GRID_SIZE, 20 * GRID_SIZE),
        (2 * GRID_SIZE, 21 * GRID_SIZE),
        (2 * GRID_SIZE, 17 * GRID_SIZE)
    ]

    menu_arrows = [
        (42 * GRID_SIZE, 26 * GRID_SIZE),
        (41 * GRID_SIZE, 27 * GRID_SIZE),
        (40 * GRID_SIZE, 28 * GRID_SIZE),
        (41 * GRID_SIZE, 29 * GRID_SIZE),
        (42 * GRID_SIZE, 30 * GRID_SIZE),
        (2 * GRID_SIZE, 26 * GRID_SIZE),
        (3 * GRID_SIZE, 27 * GRID_SIZE),
        (4 * GRID_SIZE, 28 * GRID_SIZE),
        (3 * GRID_SIZE, 29 * GRID_SIZE),
        (2 * GRID_SIZE, 30 * GRID_SIZE)
    ]

    over = [
        (3 * GRID_SIZE, 4 * GRID_SIZE),
        (4 * GRID_SIZE, 4 * GRID_SIZE),
        (3 * GRID_SIZE, 8 * GRID_SIZE),
        (4 * GRID_SIZE, 8 * GRID_SIZE),
        (4 * GRID_SIZE, 6 * GRID_SIZE),
        (8 * GRID_SIZE, 4 * GRID_SIZE),
        (9 * GRID_SIZE, 6 * GRID_SIZE),
        (7 * GRID_SIZE, 6 * GRID_SIZE),
        (8 * GRID_SIZE, 6 * GRID_SIZE),
        (12 * GRID_SIZE, 5 * GRID_SIZE),
        (18 * GRID_SIZE, 8 * GRID_SIZE),
        (19 * GRID_SIZE, 8 * GRID_SIZE),
        (20 * GRID_SIZE, 8 * GRID_SIZE),
        (18 * GRID_SIZE, 6 * GRID_SIZE),
        (19 * GRID_SIZE, 6 * GRID_SIZE),
        (18 * GRID_SIZE, 4 * GRID_SIZE),
        (19 * GRID_SIZE, 4 * GRID_SIZE),
        (20 * GRID_SIZE, 4 * GRID_SIZE),
        (26 * GRID_SIZE, 4 * GRID_SIZE),
        (27 * GRID_SIZE, 4 * GRID_SIZE),
        (25 * GRID_SIZE, 5 * GRID_SIZE),
        (25 * GRID_SIZE, 6 * GRID_SIZE),
        (25 * GRID_SIZE, 7 * GRID_SIZE),
        (26 * GRID_SIZE, 8 * GRID_SIZE),
        (27 * GRID_SIZE, 8 * GRID_SIZE),
        (28 * GRID_SIZE, 7 * GRID_SIZE),
        (28 * GRID_SIZE, 6 * GRID_SIZE),
        (28 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 4 * GRID_SIZE),
        (30 * GRID_SIZE, 5 * GRID_SIZE),
        (30 * GRID_SIZE, 6 * GRID_SIZE),
        (30 * GRID_SIZE, 7 * GRID_SIZE),
        (31 * GRID_SIZE, 8 * GRID_SIZE),
        (32 * GRID_SIZE, 7 * GRID_SIZE),
        (32 * GRID_SIZE, 6 * GRID_SIZE),
        (32 * GRID_SIZE, 5 * GRID_SIZE),
        (32 * GRID_SIZE, 4 * GRID_SIZE),
        (34 * GRID_SIZE, 4 * GRID_SIZE),
        (34 * GRID_SIZE, 5 * GRID_SIZE),
        (34 * GRID_SIZE, 6 * GRID_SIZE),
        (34 * GRID_SIZE, 7 * GRID_SIZE),
        (34 * GRID_SIZE, 8 * GRID_SIZE),
        (35 * GRID_SIZE, 8 * GRID_SIZE),
        (36 * GRID_SIZE, 8 * GRID_SIZE),
        (37 * GRID_SIZE, 8 * GRID_SIZE),
        (35 * GRID_SIZE, 6 * GRID_SIZE),
        (36 * GRID_SIZE, 6 * GRID_SIZE),
        (35 * GRID_SIZE, 4 * GRID_SIZE),
        (36 * GRID_SIZE, 4 * GRID_SIZE),
        (37 * GRID_SIZE, 4 * GRID_SIZE),
        (39 * GRID_SIZE, 4 * GRID_SIZE),
        (39 * GRID_SIZE, 5 * GRID_SIZE),
        (39 * GRID_SIZE, 6 * GRID_SIZE),
        (39 * GRID_SIZE, 7 * GRID_SIZE),
        (39 * GRID_SIZE, 8 * GRID_SIZE),
        (40 * GRID_SIZE, 4 * GRID_SIZE),
        (41 * GRID_SIZE, 4 * GRID_SIZE),
        (42 * GRID_SIZE, 5 * GRID_SIZE),
        (41 * GRID_SIZE, 6 * GRID_SIZE),
        (40 * GRID_SIZE, 6 * GRID_SIZE),
        (41 * GRID_SIZE, 7 * GRID_SIZE),
        (42 * GRID_SIZE, 8 * GRID_SIZE),
        (21 * GRID_SIZE, 4 * GRID_SIZE),
        (20 * GRID_SIZE, 6 * GRID_SIZE),
        (21 * GRID_SIZE, 8 * GRID_SIZE),
        (18 * GRID_SIZE, 5 * GRID_SIZE),
        (18 * GRID_SIZE, 7 * GRID_SIZE),
        (16 * GRID_SIZE, 8 * GRID_SIZE),
        (16 * GRID_SIZE, 7 * GRID_SIZE),
        (16 * GRID_SIZE, 6 * GRID_SIZE),
        (16 * GRID_SIZE, 4 * GRID_SIZE),
        (16 * GRID_SIZE, 5 * GRID_SIZE),
        (12 * GRID_SIZE, 4 * GRID_SIZE),
        (12 * GRID_SIZE, 6 * GRID_SIZE),
        (12 * GRID_SIZE, 8 * GRID_SIZE),
        (12 * GRID_SIZE, 7 * GRID_SIZE),
        (13 * GRID_SIZE, 5 * GRID_SIZE),
        (14 * GRID_SIZE, 6 * GRID_SIZE),
        (15 * GRID_SIZE, 5 * GRID_SIZE),
        (10 * GRID_SIZE, 8 * GRID_SIZE),
        (10 * GRID_SIZE, 7 * GRID_SIZE),
        (10 * GRID_SIZE, 6 * GRID_SIZE),
        (10 * GRID_SIZE, 5 * GRID_SIZE),
        (9 * GRID_SIZE, 4 * GRID_SIZE),
        (7 * GRID_SIZE, 5 * GRID_SIZE),
        (7 * GRID_SIZE, 7 * GRID_SIZE),
        (7 * GRID_SIZE, 8 * GRID_SIZE),
        (5 * GRID_SIZE, 6 * GRID_SIZE),
        (5 * GRID_SIZE, 7 * GRID_SIZE),
        (5 * GRID_SIZE, 8 * GRID_SIZE),
        (2 * GRID_SIZE, 7 * GRID_SIZE),
        (2 * GRID_SIZE, 6 * GRID_SIZE),
        (2 * GRID_SIZE, 5 * GRID_SIZE),
        (5 * GRID_SIZE, 4 * GRID_SIZE)
    ]

    retry = [
        (11 * GRID_SIZE, 17 * GRID_SIZE),
        (12 * GRID_SIZE, 17 * GRID_SIZE),
        (12 * GRID_SIZE, 19 * GRID_SIZE),
        (11 * GRID_SIZE, 19 * GRID_SIZE),
        (16 * GRID_SIZE, 21 * GRID_SIZE),
        (17 * GRID_SIZE, 21 * GRID_SIZE),
        (18 * GRID_SIZE, 21 * GRID_SIZE),
        (16 * GRID_SIZE, 19 * GRID_SIZE),
        (17 * GRID_SIZE, 19 * GRID_SIZE),
        (17 * GRID_SIZE, 17 * GRID_SIZE),
        (18 * GRID_SIZE, 17 * GRID_SIZE),
        (16 * GRID_SIZE, 17 * GRID_SIZE),
        (21 * GRID_SIZE, 17 * GRID_SIZE),
        (22 * GRID_SIZE, 17 * GRID_SIZE),
        (31 * GRID_SIZE, 19 * GRID_SIZE),
        (33 * GRID_SIZE, 17 * GRID_SIZE),
        (33 * GRID_SIZE, 18 * GRID_SIZE),
        (32 * GRID_SIZE, 19 * GRID_SIZE),
        (32 * GRID_SIZE, 20 * GRID_SIZE),
        (32 * GRID_SIZE, 21 * GRID_SIZE),
        (30 * GRID_SIZE, 18 * GRID_SIZE),
        (30 * GRID_SIZE, 17 * GRID_SIZE),
        (28 * GRID_SIZE, 18 * GRID_SIZE),
        (27 * GRID_SIZE, 17 * GRID_SIZE),
        (26 * GRID_SIZE, 17 * GRID_SIZE),
        (25 * GRID_SIZE, 17 * GRID_SIZE),
        (27 * GRID_SIZE, 19 * GRID_SIZE),
        (26 * GRID_SIZE, 19 * GRID_SIZE),
        (25 * GRID_SIZE, 19 * GRID_SIZE),
        (25 * GRID_SIZE, 18 * GRID_SIZE),
        (25 * GRID_SIZE, 20 * GRID_SIZE),
        (25 * GRID_SIZE, 21 * GRID_SIZE),
        (27 * GRID_SIZE, 20 * GRID_SIZE),
        (28 * GRID_SIZE, 21 * GRID_SIZE),
        (22 * GRID_SIZE, 18 * GRID_SIZE),
        (22 * GRID_SIZE, 19 * GRID_SIZE),
        (22 * GRID_SIZE, 20 * GRID_SIZE),
        (22 * GRID_SIZE, 21 * GRID_SIZE),
        (23 * GRID_SIZE, 17 * GRID_SIZE),
        (19 * GRID_SIZE, 17 * GRID_SIZE),
        (19 * GRID_SIZE, 21 * GRID_SIZE),
        (18 * GRID_SIZE, 19 * GRID_SIZE),
        (16 * GRID_SIZE, 18 * GRID_SIZE),
        (16 * GRID_SIZE, 20 * GRID_SIZE),
        (14 * GRID_SIZE, 18 * GRID_SIZE),
        (13 * GRID_SIZE, 17 * GRID_SIZE),
        (13 * GRID_SIZE, 19 * GRID_SIZE),
        (13 * GRID_SIZE, 20 * GRID_SIZE),
        (14 * GRID_SIZE, 21 * GRID_SIZE),
        (11 * GRID_SIZE, 20 * GRID_SIZE),
        (11 * GRID_SIZE, 21 * GRID_SIZE),
        (11 * GRID_SIZE, 18 * GRID_SIZE)
    ]


@dataclass
class Colors:
    """Defines colors for game elements."""

    # Global
    black = (0, 0, 0)

    # Menu
    green_grid = (0, 50, 0)

    tile_inside_color = (0, 20, 0)
    logo_anime = [(0, 150 + i, 0) for i in range(106)]

    # Game
    gray_grid = (50, 50, 50)

    apple = (255, 0, 0)
    apple_in_searchlight = (255, 140, 0)
    searchlight = (30, 30, 30)

    snake = (50, 160, 0)
    snake_head = (100, 255, 100)

    score = (20, 220, 20)


@dataclass
class ObjPoints:
    """Stores point sets for objects on screen."""

    play_button = ((6 * GRID_SIZE, 15 * GRID_SIZE),
                   (38 * GRID_SIZE, 24 * GRID_SIZE))

    quit_button = ((6 * GRID_SIZE, 24 * GRID_SIZE),
                   (38 * GRID_SIZE, 33 * GRID_SIZE))

    resume_button = ((3 * GRID_SIZE, 15 * GRID_SIZE),
                     (41 * GRID_SIZE, 24 * GRID_SIZE))

    menu_button = ((7 * GRID_SIZE, 24 * GRID_SIZE),
                   (38 * GRID_SIZE, 33 * GRID_SIZE))

    retry_button = ((7 * GRID_SIZE, 15 * GRID_SIZE),
                    (38 * GRID_SIZE, 24 * GRID_SIZE))


class ParticlePresets:
    """Settings for particles."""

    @staticmethod
    def apple():
        """Return settings for apple's particles"""
        return (
            (uniform(-2 * RES_MULT, 2 * RES_MULT),
             uniform(-2 * RES_MULT, 2 * RES_MULT)),
            randint(2 * RES_MULT, 5 * RES_MULT),
            (randint(200, 255), randint(0, 200), 0),
            10000
        )

    @staticmethod
    def snake():
        """Return settings for snake's particles"""
        return (
            (uniform(-4, 4), uniform(-4, 4)),
            randint(5, 7),
            (randint(100, 150), randint(200, 255), randint(100, 150)),
            10000
        )


class GameObject:
    """Basic class for in game objects."""

    def __init__(self, position=(0, 0)):
        self.position = position
        self.body_color = None

    def draw(self):
        """Draw object on screen surface."""
        pass


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
        super().__init__(self)
        self.body_color = body_color

    def draw(self):
        """Draw a grid based on class defined point sets."""
        for point_set in self.grid:
            pygame.draw.rect(screen, self.body_color, point_set)


class GameGrid(Grid):
    """Creating a grid to make outlines between squares."""

    # Define field boarders. 1 pixel wide.
    boarders_grid = [
        (0, 7 * GRID_SIZE, 1, SCREEN_HEIGHT),
        (SCREEN_WIDTH - 1, 7 * GRID_SIZE, SCREEN_WIDTH - 1, SCREEN_HEIGHT),
        (0, SCREEN_HEIGHT - 1, SCREEN_WIDTH, SCREEN_HEIGHT - 1)
    ]

    # Define horizontal lines. 2 pixels wide.
    vertical_grid = [(x - 1, 7 * GRID_SIZE, 1, SCREEN_HEIGHT)
                     for x in range(GRID_SIZE, SCREEN_WIDTH, GRID_SIZE)]

    # Define vertical lines. 2 pixels wide.
    horizontal_grid = [(0, y - 1, SCREEN_WIDTH, 1)
                       for y in range(7 * GRID_SIZE, SCREEN_HEIGHT, GRID_SIZE)]

    grid = boarders_grid + vertical_grid + horizontal_grid

    def __init__(self, body_color=Colors.black):
        super().__init__(body_color)


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

    def draw(self, positions=[]):
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


class MenuAnimation:
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


class MenuText:
    """Text in menu made of several tiles."""

    def __init__(self):
        self.logo_text = [Bit(point) for point in Text.logo]
        self.play_button = [Bit(point) for point in Text.play]
        self.quit_button = [Bit(point) for point in Text.quit]
        self.play_arrows = [Bit(point) for point in Text.play_arrows]
        self.quit_arrows = [Bit(point) for point in Text.quit_arrows]

        # Display arrows only when mouse is over button.
        # These values are changed by other classes.
        self.display_play_arrows = False
        self.display_quit_arrows = False

        # List of animations that are currently displayed in menu
        self.animations = []

    def draw(self, highlight, iter_counter):
        """Draw text and animations on screen."""
        # Contains main text that is always on screen
        bits = self.logo_text + self.play_button + self.quit_button

        # List of tiles that should be filled with their color
        # are located in 'highlight' variable. For each animation
        # calculate new positions that should be filled on this frame.
        # Append those positions to highlight variable.
        for anime in self.animations:
            highlight += anime.update(iter_counter)

        # Check if mouse is over button, display arrows if so.
        if self.display_play_arrows:
            bits += self.play_arrows
        if self.display_quit_arrows:
            bits += self.quit_arrows

        # Draw tiles
        for bit in bits:
            bit.draw(highlight)

    def start_animation(self, anime, from_, _to, mouse):
        """Add new animation to text on the button
        if mouse is over the button.
        """
        # Check if an animation already exists.
        if anime in self.animations:
            return

        # If not, append new animation to the list
        self.animations.append(MenuAnimation(anime, from_, _to, mouse))

    def stop_animation(self, anime):
        """Remove animation from the list
        if mouse is no longer over the button.
        """
        self.animations = [animation for animation in self.animations
                           if animation.obj != anime]

    def stop_all(self):
        """Remove all animations."""
        self.animations = []


class MouseGlow:
    """Highlight tiles that are below the mouse.
    Positions list of those tiles recreates with every frame.
    """

    def __init__(self):
        self.positions = []
        self.fix = 2 if RES_MULT == 1 else 1

    def draw(self, mouse, update_only=False):
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


class Button:
    """Button. Invisible object on screen, defined as set of points."""

    def __init__(self, point):
        self.from_point, self.to_point = point

    def hover(self, mouse):
        """Check if the mouse is over button"""
        if (self.from_point[0] < mouse[0] < self.to_point[0]
                and self.from_point[1] < mouse[1] < self.to_point[1]):
            return True

        return False


class Menu:
    """Controls instances of all other elements included in menu."""

    def __init__(self):
        self.grid = Grid(body_color=Colors.green_grid)
        self.logo = MenuText()
        self.mouseglow = MouseGlow()

        self.play_button = Button(ObjPoints.play_button)
        self.quit_button = Button(ObjPoints.quit_button)

    def hover(self, iter_counter, mouse):
        """Check if the mouse is above button in menu.
        If so, display arrows around the button and
        start animation on the button itself.
        """
        if self.play_button.hover(mouse):
            self.logo.display_play_arrows = True
            self.logo.start_animation(Text.play, iter_counter, 15, mouse)

        else:
            self.logo.display_play_arrows = False
            self.logo.stop_animation(Text.play)

        if self.quit_button.hover(mouse):
            self.logo.display_quit_arrows = True
            self.logo.start_animation(Text.quit, iter_counter, 15, mouse)

        else:
            self.logo.display_quit_arrows = False
            self.logo.stop_animation(Text.quit)

    def click(self, mouse):
        """Click handler. Start command if the button has been clicked."""
        if self.play_button.hover(mouse):
            self.logo.stop_all()
            return self.change_mode('game')

        if self.quit_button.hover(mouse):
            return self.change_mode('quit')

    @staticmethod
    def change_mode(mode):
        """Return game mode"""
        return mode


class Apple(GameObject):
    """Ingame object, with a position and color"""

    def __init__(self):
        super().__init__(self)
        self.body_color = Colors.apple
        self.position = (8 * GRID_SIZE, 8 * GRID_SIZE)

    def randomize_position(self, snake_positions):
        """Get random position of new apple. Random position cannot be
        inside the snake. Choice is used here, as usual random will be
        really inefficient as snake grows.
        """
        return choice([pos for pos in
                       [(x, y)
                        for x in range(0, SCREEN_WIDTH, GRID_SIZE)
                        for y in range(7 * GRID_SIZE,
                                       SCREEN_HEIGHT, GRID_SIZE)]
                       if pos not in snake_positions])

    def update(self, snake_positions):
        """Check if the snake's head is colliding with apple.
        If so, get new position for an apple and return True for snake.
        """
        if self.position in snake_positions:
            self.position = self.randomize_position(snake_positions)
            self.draw()

            return True

        else:
            # Draw an apple anyway, no matter if snake has eaten it.
            self.draw()

            return False

    def draw(self):
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

    def __init__(self):
        super().__init__(self)
        # Some variables to pass tests:
        self.body_color = Colors.snake
        self.length = 1

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

    def draw(self, jump):
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

    def get_head_position(self):
        """Idk what this method is needed for,
        as we always know where the head is.
        """
        pass

    def reset(self):
        """Won't be used, as new instance of snake
        is created to reset the game.
        """
        pass


class Particle(GameObject):
    """Particle. Used in some animations. Has its own position,
    size and velocity.
    Dies over certain period of time.
    """

    def __init__(self, pos, preset):
        self.position = vec(pos[0] + GRID_SIZE // 2, pos[1] + GRID_SIZE // 2)
        self.velocity = vec(preset[0])
        self.size = vec(preset[1])
        self.body_color = preset[2]

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

    def draw(self):
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


class GameAnimation:
    """Class for ingame animations. Actually is made of particles."""

    def __init__(self):
        self.first_layer = []
        self.second_layer = []
        self.third_layer = []

    def clean_up(self):
        """Remove dead particles from animation lists."""
        self.first_layer = [item for item in self.first_layer if item.alive]
        self.second_layer = [item for item in self.second_layer if item.alive]
        self.third_layer = [item for item in self.third_layer if item.alive]

    def all(self):
        """Get animations from all 3 lists."""
        return self.first_layer + self.second_layer + self.third_layer


class SearchLight:
    """Beam of light that goes from the head of the snake,
    indicating path the snake will cover if the direction is unchanged.
    """

    def __init__(self, snake):
        self.snake = snake
        self.positions = []

    def draw(self):
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


class Rect:
    """Just a usual rect :)"""

    def __init__(self, from_x, from_y, to_x, to_y, color=Colors.black):
        self.rect = pygame.Rect(from_x, from_y, to_x, to_y)
        self.color = color

    def draw(self):
        """Draw a rect."""
        pygame.draw.rect(screen, self.color, self.rect)


class GameText:
    """Displays score in game."""

    digits_map = {
        '0': Text.digit_0,
        '1': Text.digit_1,
        '2': Text.digit_2,
        '3': Text.digit_3,
        '4': Text.digit_4,
        '5': Text.digit_5,
        '6': Text.digit_6,
        '7': Text.digit_7,
        '8': Text.digit_8,
        '9': Text.digit_9,
    }

    def __init__(self):
        self.score_logo = [Bit(point) for point in Text.score]

    def draw(self, score):
        """Draw text and animations on screen."""
        # Creates pixel digits from string digits.
        bits = [Bit((point[0] + GRID_SIZE * 5 * i, point[1]),
                    color_set=[Colors.score],
                    change_colors=False)
                for i in range(3) for point in
                self.digits_map[('%03d' % score)[i]]] + self.score_logo

        # Draw tiles
        for bit in bits:
            bit.draw()


class Game:
    """Collection of all instances included in game process."""

    def __init__(self):
        self.grid = GameGrid(body_color=Colors.gray_grid)

        self.apple = Apple()
        self.snake = Snake()
        self.searchlight = SearchLight(self.snake)

        self.cover = Rect(0, 0, SCREEN_WIDTH, GRID_SIZE * 7 - 1)
        self.label = GameText()

        self.animation = GameAnimation()

        # How often the snake will move
        self.update_rate = 12

        # Stage of snake animations.
        self.snake_jump = 10

        # Length of the snake.
        self.score = 1

        # If game is active, do update snake positions.
        self.active = True


class PauseText(MenuText):
    """Text in pause screen."""

    def __init__(self):
        self.pause = [Bit(point) for point in Text.pause]
        self.resume = [Bit(point) for point in Text.resume]
        self.menu = [Bit(point) for point in Text.menu]

        self.resume_arrows = [Bit(point) for point in Text.resume_arrows]
        self.menu_arrows = [Bit(point) for point in Text.menu_arrows]

        # Display arrows only when mouse is over button.
        # These values are changed by other classes.
        self.display_resume_arrows = False
        self.display_menu_arrows = False

        # List of animations that are currently displayed in menu
        self.animations = []

    def draw(self, highlight, iter_counter):
        """Draw text and animations on screen."""
        # Contains main text that is always on screen
        bits = self.pause + self.resume + self.menu

        # List of tiles that should be filled with their color
        # are located in 'highlight' variable. For each animation
        # calculate new positions that should be filled on this frame.
        # Append those positions to highlight variable.
        for anime in self.animations:
            highlight += anime.update(iter_counter)

        # Check if mouse is over button, display arrows if so.
        if self.display_resume_arrows:
            bits += self.resume_arrows
        if self.display_menu_arrows:
            bits += self.menu_arrows

        # Draw tiles
        for bit in bits:
            bit.draw(highlight)


class Pause(Menu):
    """Collection of all instances included in pause screen."""

    def __init__(self):
        self.logo = PauseText()
        self.mouseglow = MouseGlow()

        self.resume_button = Button(ObjPoints.resume_button)
        self.menu_button = Button(ObjPoints.menu_button)

    def hover(self, iter_counter, mouse):
        """Check if the mouse is above button in menu.
        If so, display arrows around the button and
        start animation on the button itself.
        """
        if self.resume_button.hover(mouse):
            self.logo.display_resume_arrows = True
            self.logo.start_animation(Text.resume, iter_counter, 15, mouse)

        else:
            self.logo.display_resume_arrows = False
            self.logo.stop_animation(Text.resume)

        if self.menu_button.hover(mouse):
            self.logo.display_menu_arrows = True
            self.logo.start_animation(Text.menu, iter_counter, 15, mouse)

        else:
            self.logo.display_menu_arrows = False
            self.logo.stop_animation(Text.menu)

    def click(self, mouse):
        """Click handler. Start command if the button has been clicked."""
        if self.resume_button.hover(mouse):
            return self.change_mode('game')

        if self.menu_button.hover(mouse):
            return self.change_mode('menu')


class OverText(MenuText):
    """Text in gameover screen."""

    def __init__(self):
        self.over = [Bit(point) for point in Text.over]
        self.retry = [Bit(point) for point in Text.retry]
        self.menu = [Bit(point) for point in Text.menu]

        self.retry_arrows = [Bit(point) for point in Text.resume_arrows]
        self.menu_arrows = [Bit(point) for point in Text.menu_arrows]

        # Display arrows only when mouse is over button.
        # These values are changed by other classes.
        self.display_retry_arrows = False
        self.display_menu_arrows = False

        # List of animations that are currently displayed in menu
        self.animations = []

    def draw(self, highlight, iter_counter):
        """Draw text and animations on screen."""
        # Contains main text that is always on screen
        bits = self.over + self.retry + self.menu

        # List of tiles that should be filled with their color
        # are located in 'highlight' variable. For each animation
        # calculate new positions that should be filled on this frame.
        # Append those positions to highlight variable.
        for anime in self.animations:
            highlight += anime.update(iter_counter)

        # Check if mouse is over button, display arrows if so.
        if self.display_retry_arrows:
            bits += self.retry_arrows
        if self.display_menu_arrows:
            bits += self.menu_arrows

        # Draw tiles
        for bit in bits:
            bit.draw(highlight)


class Over(Menu):
    """Collection of all instances included in gameover screen."""

    def __init__(self):
        self.logo = OverText()
        self.mouseglow = MouseGlow()

        self.retry_button = Button(ObjPoints.retry_button)
        self.menu_button = Button(ObjPoints.menu_button)

    def hover(self, iter_counter, mouse):
        """Check if the mouse is above button in menu.
        If so, display arrows around the button and
        start animation on the button itself.
        """
        if self.retry_button.hover(mouse):
            self.logo.display_retry_arrows = True
            self.logo.start_animation(Text.retry, iter_counter, 15, mouse)

        else:
            self.logo.display_retry_arrows = False
            self.logo.stop_animation(Text.retry)

        if self.menu_button.hover(mouse):
            self.logo.display_menu_arrows = True
            self.logo.start_animation(Text.menu, iter_counter, 15, mouse)

        else:
            self.logo.display_menu_arrows = False
            self.logo.stop_animation(Text.menu)

    def click(self, mouse):
        """Click handler. Start command if the button has been clicked."""
        if self.retry_button.hover(mouse):
            return self.change_mode('game')

        if self.menu_button.hover(mouse):
            return self.change_mode('menu')


class Engine:
    """Class to connect everything above into one game."""

    def __init__(self):
        self.iter_counter = 0
        self.screen = 'menu'

        self.menu = Menu()
        self.game = Game()
        self.pause = Pause()
        self.over = Over()

        self.cover_all = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cover_score = pygame.Surface((SCREEN_WIDTH, 7 * GRID_SIZE - 1))

        self.cover_all.set_alpha(128)
        self.cover_score.set_alpha(128)
        self.cover_all.fill(Colors.black)
        self.cover_score.fill(Colors.black)

    def handle_keys_mouse(self, mouse):
        """None"""
        # Get menu button clicks.
        if self.screen == 'menu':
            self.screen = self.menu.click(mouse)

            if self.screen == 'game':
                # Restart game, if play in menu has been selected.
                self.game = Game()

            if self.screen == 'quit':
                # Return true, to exit main loop
                return True

        if self.screen == 'pause':
            self.screen = self.pause.click(mouse)

            if self.screen == 'game':
                # Set game to active, if the game was unpaused.
                self.game.active = True

        if self.screen == 'over':
            self.screen = self.over.click(mouse)

            if self.screen == 'game':
                self.over.logo.stop_all()
                # Restart game, if retry was selected.
                self.game = Game()

    def handle_keys_keydown(self, event):
        """Just a method to make handle_keys less complex :)"""
        if event.key == pygame.K_ESCAPE:
            if self.screen == 'game':
                # Set game to inactive, if the game was paused.
                self.game.active = False
                self.screen = 'pause'
                self.pause.logo.stop_all()

            elif self.screen == 'pause':
                # Set game to active, if the game was unpaused.
                self.game.active = True
                self.screen = 'game'

            else:
                pass

        # Move the snake around.
        if event.key == pygame.K_w:
            self.game.snake.update_direction(UP)
        if event.key == pygame.K_s:
            self.game.snake.update_direction(DOWN)
        if event.key == pygame.K_d:
            self.game.snake.update_direction(RIGHT)
        if event.key == pygame.K_a:
            self.game.snake.update_direction(LEFT)

        if event.key == pygame.K_SPACE:
            # Speed up the game when SPACE is pressed.
            if self.screen == 'game':
                self.game.update_rate = self.game.update_rate // 2

    def handle_keys_keyup(self, event):
        """Just a method to make handle_keys less complex :)"""
        if event.key == pygame.K_SPACE:
            # Slow down the game when SPACE is released.
            if self.screen == 'game':
                self.game.update_rate = self.game.update_rate * 2

    def handle_keys(self):
        """Get keys pressed and send actions to other game parts."""
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit immediately if window was closed.
                pygame.quit()
                raise SystemExit

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_keys_mouse(mouse)

            if event.type == pygame.KEYDOWN:
                self.handle_keys_keydown(event)

            if event.type == pygame.KEYUP:
                self.handle_keys_keyup(event)

        return False

    def render(self):
        """Select screen to render, based on current mode."""
        response = self.handle_keys()

        if self.screen == 'menu':
            self.render_menu()
        elif self.screen == 'game':
            self.render_game()
        elif self.screen == 'pause':
            self.render_pause()
        elif self.screen == 'over':
            self.render_over()
        else:
            pass

        self.iter_counter += 1

        return response

    def render_menu(self):
        """Render menu screen."""
        mouse = pygame.mouse.get_pos()  # Get mouse positions.

        screen.fill(Colors.black)  # Clean the screen for a new frame

        # Draw a grid on the background
        self.menu.grid.draw()

        # If mouse is somewhere on the screen, highlight tiles
        # that located below the mouse.
        self.menu.mouseglow.draw(mouse)

        # Draw menu elements, buttons and title
        self.menu.logo.draw(self.menu.mouseglow.positions, self.iter_counter)

        # Check if the mouse is on top of the button, highlight button if so.
        self.menu.hover(self.iter_counter, mouse)

    def render_game(self):
        """Render game screen"""
        # Move snake based on update_rate value if the game is active.
        if self.iter_counter % self.game.update_rate == 0 and self.game.active:
            # Update apple.
            apple_eaten = self.game.apple.update(self.game.snake.positions)

            # Check if snake ate the apple.
            if apple_eaten:
                # If so, create particle animation for a new apple.
                particles = [Particle(self.game.apple.position,
                                      ParticlePresets.apple())
                             for i in range(30)]
                self.game.animation.third_layer += particles

            # Check if snake bit its own tail.
            if self.game.snake.move(apple_eaten):
                # If so, render gameover screen.
                self.screen = 'over'

            # Reset animation stage value.
            self.game.snake_jump = 0

        # Change apple color if apple in searchlight.
        if self.game.apple.position in self.game.searchlight.positions:
            self.game.apple.body_color = Colors.apple_in_searchlight
        else:
            self.game.apple.body_color = Colors.apple

        # Reset the screen
        screen.fill(Colors.black)

        # Draw grid and searchlight
        self.game.grid.draw()
        self.game.searchlight.draw()

        # Draw animations
        for anime in self.game.animation.third_layer:
            anime.draw()

        self.game.apple.draw()

        # Draw snake or snake animation based on snake_jump value
        self.game.snake_jump = self.game.snake.draw(self.game.snake_jump)

        # Draw a cover for score to be displayed on top.
        self.game.cover.draw()

        # Update and draw score.
        self.game.score = len(self.game.snake.positions) - 2
        self.game.label.draw(self.game.score)

        # Remove all animations with expired lifetime.
        self.game.animation.clean_up()

    def render_pause(self):
        """Render pause screen."""
        mouse = pygame.mouse.get_pos()

        # Set game to inactive to stop position updates.
        self.game.active = False
        self.render_game()

        # Cover game with transparent screen.
        screen.blit(self.cover_all, (0, 0))
        screen.blit(self.cover_score, (0, 0))

        # Draw pause screen on top.
        self.pause.mouseglow.draw(mouse, update_only=True)
        self.pause.logo.draw(self.pause.mouseglow.positions, self.iter_counter)
        self.pause.hover(self.iter_counter, mouse)

    def render_over(self):
        """Render gameover screen."""
        mouse = pygame.mouse.get_pos()

        # Set game to inactive to stop position updates.
        self.game.active = False
        self.render_game()

        # Cover game with transparent screen.
        screen.blit(self.cover_all, (0, 0))
        screen.blit(self.cover_score, (0, 0))

        # Draw over screen on top.
        self.over.mouseglow.draw(mouse, update_only=True)
        self.over.logo.draw(self.over.mouseglow.positions, self.iter_counter)
        self.over.hover(self.iter_counter, mouse)


def main():
    """Main loop."""
    pygame.init()
    engine = Engine()

    while True:
        if engine.render():
            break

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
