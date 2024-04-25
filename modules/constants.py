from dataclasses import dataclass
from random import randint, uniform


# Increase gamewindow size by n times.
RES_MULT = 3

# The size of the window itself.
SCREEN_WIDTH, SCREEN_HEIGHT = 720 * RES_MULT, 560 * RES_MULT
GRID_SIZE = 16 * RES_MULT  # Size of a single "tile" - square.

# Ingame snake directions
UP = (0, -GRID_SIZE)
DOWN = (0, GRID_SIZE)
LEFT = (-GRID_SIZE, 0)
RIGHT = (GRID_SIZE, 0)

# Frames per sec.
FPS = 60


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

    cells = set((x, y) for x in range(0, SCREEN_WIDTH, GRID_SIZE)
                for y in range(7 * GRID_SIZE, SCREEN_HEIGHT, GRID_SIZE))


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


@dataclass
class PointText:
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
