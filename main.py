import ctypes
import pygame

from modules import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from modules import Engine


try:
    # Try to set high-res. Works on Windows 10-11.
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

except AttributeError as error:
    print(error)

try:
    # Load an icon for game window from file.
    icon = pygame.image.load('resources/icon.png')
    pygame.display.set_icon(icon)

except FileNotFoundError as error:
    print(error)

pygame.display.set_caption('the_sneaky_snake')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


def main():
    """Main loop."""
    pygame.init()
    engine = Engine(screen)

    while True:
        if engine.render():
            break

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
