from modules.constants import SCREEN_HEIGHT, SCREEN_WIDTH, GRID_SIZE
from modules.constants import Colors, ObjPoints, PointText

from modules.game import Grid, GameGrid, Apple, Snake
from modules.button import Button
from modules.animations import MouseGlow, SearchLight, Cover, ShadowCover
from modules.texts import MenuText, GameText, PauseText, OverText


class Window:
    WIN_ANIME_TIME = 15

    def __init__(self):
        self.mouseglow = MouseGlow()

    def hover(self, mouse, iter_counter):
        if self.button_1.hover(mouse):
            self.tiles.display_arrows_1 = True
            self.tiles.start_animation(self.button_1.text,
                                       iter_counter,
                                       self.WIN_ANIME_TIME,
                                       mouse)
        else:
            self.tiles.display_arrows_1 = False
            self.tiles.stop_animation(self.button_1.text)

        if self.button_2.hover(mouse):
            self.tiles.display_arrows_2 = True
            self.tiles.start_animation(self.button_2.text,
                                       iter_counter,
                                       self.WIN_ANIME_TIME,
                                       mouse)
        else:
            self.tiles.display_arrows_2 = False
            self.tiles.stop_animation(self.button_2.text)

    def click(self, mouse):
        if self.button_1.hover(mouse):
            return self.button_1.mode

        if self.button_2.hover(mouse):
            return self.button_2.mode


class Menu(Window):
    """Controls instances of all other elements included in menu."""

    def __init__(self):
        super().__init__()

        self.grid = Grid(body_color=Colors.green_grid)
        self.tiles = MenuText()

        self.button_1 = Button(ObjPoints.play_button, PointText.play, 'game')
        self.button_2 = Button(ObjPoints.quit_button, PointText.quit, 'quit')


class Pause(Window):
    """Collection of all instances included in pause screen."""

    def __init__(self):
        super().__init__()

        self.tiles = PauseText()

        self.button_1 = Button(ObjPoints.resume_button,
                               PointText.resume, 'game')
        self.button_2 = Button(ObjPoints.menu_button, PointText.menu, 'menu')

        self.cover_all = ShadowCover(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.cover_score = ShadowCover(0, 0, SCREEN_WIDTH, 7 * GRID_SIZE - 1)


class Over(Menu):
    """Collection of all instances included in gameover screen."""

    def __init__(self):
        super().__init__()

        self.tiles = OverText()

        self.button_1 = Button(ObjPoints.retry_button, PointText.retry, 'game')
        self.button_2 = Button(ObjPoints.menu_button, PointText.menu, 'menu')

        self.cover_all = ShadowCover(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.cover_score = ShadowCover(0, 0, SCREEN_WIDTH, 7 * GRID_SIZE - 1)


class Game:
    """Collection of all instances included in game process."""

    def __init__(self):
        self.grid = GameGrid(body_color=Colors.gray_grid)

        self.apple = Apple()
        self.snake = Snake()
        self.searchlight = SearchLight(self.snake)

        self.cover = Cover()
        self.label = GameText()

        self.animations = []

        # How often the snake will move
        self.update_rate = 12

        # Stage of snake animations.
        self.snake_jump = 10

        # Length of the snake.
        self.score = 1

        # If game is active, do update snake positions.
        self.active = True
