from modules.animations import Bit, TextAnimation
from modules.constants import PointText, GRID_SIZE, Colors


class TextTiles:
    """Tiles from which the texts are made"""

    def __init__(self):
        # Display arrows only when mouse is over button.
        # These values are changed by other classes.
        self.display_arrows_1 = False
        self.display_arrows_2 = False

        # List of animations that are currently displayed in menu
        self.animations = []

    def draw(self, screen, highlight, iter_counter):
        """Draw text and animations on screen."""
        # List of tiles that should be filled with their color
        # are located in 'highlight' variable. For each animation
        # calculate new positions that should be filled on this frame.
        # Append those positions to highlight variable.
        for anime in self.animations:
            highlight += anime.update(iter_counter)

        # Draw tiles
        for bit in self.logo:
            bit.draw(screen, highlight)

        if self.display_arrows_1:
            for bit in self.arrows_1:
                bit.draw(screen, highlight)

        if self.display_arrows_2:
            for bit in self.arrows_2:
                bit.draw(screen, highlight)

    def start_animation(self, anime, from_, _to, mouse):
        """Add new animation to text on the button
        if mouse is over the button.
        """
        # Check if an animation already exists.
        if anime in self.animations:
            return

        # If not, append new animation to the list
        self.animations.append(TextAnimation(anime, from_, _to, mouse))

    def stop_animation(self, anime):
        """Remove animation from the list
        if mouse is no longer over the button.
        """
        self.animations = [animation for animation in self.animations
                           if animation.obj != anime]

    def stop_all(self):
        """Remove all animations."""
        self.animations = []


class MenuText(TextTiles):
    """Text in menu made of several tiles."""

    def __init__(self):
        super().__init__()
        self.logo = [Bit(point) for point in
                     PointText.logo + PointText.play + PointText.quit]

        self.arrows_1 = [Bit(point) for point in PointText.play_arrows]
        self.arrows_2 = [Bit(point) for point in PointText.quit_arrows]


class PauseText(TextTiles):
    """Text in pause screen."""

    def __init__(self):
        super().__init__()
        self.logo = [Bit(point) for point in
                     PointText.pause + PointText.resume + PointText.menu]

        self.arrows_1 = [Bit(point) for point in PointText.resume_arrows]
        self.arrows_2 = [Bit(point) for point in PointText.menu_arrows]


class OverText(TextTiles):
    """Text in gameover screen."""

    def __init__(self):
        super().__init__()
        self.logo = [Bit(point) for point in
                     PointText.over + PointText.retry + PointText.menu]

        self.arrows_1 = [Bit(point) for point in PointText.resume_arrows]
        self.arrows_2 = [Bit(point) for point in PointText.menu_arrows]


class GameText:
    """Displays score in game."""

    digits_map = {
        '0': PointText.digit_0,
        '1': PointText.digit_1,
        '2': PointText.digit_2,
        '3': PointText.digit_3,
        '4': PointText.digit_4,
        '5': PointText.digit_5,
        '6': PointText.digit_6,
        '7': PointText.digit_7,
        '8': PointText.digit_8,
        '9': PointText.digit_9,
    }

    def __init__(self):
        self.score_logo = [Bit(point) for point in PointText.score]

    def draw(self, screen, score):
        """Draw text and animations on screen."""
        # Creates pixel digits from string digits.
        bits = [Bit((point[0] + GRID_SIZE * 5 * i, point[1]),
                    color_set=[Colors.score],
                    change_colors=False)
                for i in range(3) for point in
                self.digits_map[('%03d' % score)[i]]] + self.score_logo

        # Draw tiles
        for bit in bits:
            bit.draw(screen)
