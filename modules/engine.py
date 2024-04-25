import pygame

from modules.constants import UP, DOWN, LEFT, RIGHT
from modules.constants import Colors, ParticlePresets

from modules.animations import Particle
from modules.windows import Menu, Game, Pause, Over


class Engine:
    """Class to connect everything above into one game."""

    def __init__(self, screen):
        self.screen = screen

        self.iter_counter = 0
        self.screen_type = 'menu'

        self.menu = Menu()
        self.game = Game()
        self.pause = Pause()
        self.over = Over()

    def handle_keys_mouse(self, mouse):
        """Just a method to make handle_keys less complex :)"""
        # Get menu button clicks.
        if self.screen_type == 'menu':
            self.screen_type = self.menu.click(mouse)

            if self.screen_type == 'game':
                # Restart game, if play in menu has been selected.
                self.game = Game()

            if self.screen_type == 'quit':
                # Return true, to exit main loop
                return True

        if self.screen_type == 'pause':
            self.screen_type = self.pause.click(mouse)

            if self.screen_type == 'game':
                # Set game to active, if the game was unpaused.
                self.game.active = True

        if self.screen_type == 'over':
            self.screen_type = self.over.click(mouse)

            if self.screen_type == 'game':
                self.over.tiles.stop_all()
                # Restart game, if retry was selected.
                self.game = Game()

        return False

    def handle_keys_keydown(self, event):
        """Just a method to make handle_keys less complex :)"""
        if event.key == pygame.K_ESCAPE:
            if self.screen_type == 'game':
                # Set game to inactive, if the game was paused.
                self.game.active = False
                self.screen_type = 'pause'
                self.pause.tiles.stop_all()

            elif self.screen_type == 'pause':
                # Set game to active, if the game was unpaused.
                self.game.active = True
                self.screen_type = 'game'

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
            if self.screen_type == 'game':
                self.game.update_rate = self.game.update_rate // 2

    def handle_keys_keyup(self, event):
        """Just a method to make handle_keys less complex :)"""
        if event.key == pygame.K_SPACE:
            # Slow down the game when SPACE is released.
            if self.screen_type == 'game':
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
                if self.handle_keys_mouse(mouse):
                    return True

            if event.type == pygame.KEYDOWN:
                self.handle_keys_keydown(event)

            if event.type == pygame.KEYUP:
                self.handle_keys_keyup(event)

        return False

    def render(self):
        """Select screen to render, based on current mode."""
        response = self.handle_keys()

        if self.screen_type == 'menu':
            self.render_menu()
        elif self.screen_type == 'game':
            self.render_game()
        elif self.screen_type == 'pause':
            self.render_pause()
        elif self.screen_type == 'over':
            self.render_over()

        self.iter_counter += 1

        return response

    def render_menu(self):
        """Render menu screen."""
        mouse = pygame.mouse.get_pos()  # Get mouse positions.

        self.screen.fill(Colors.black)  # Clean the screen for a new frame

        # Draw a grid on the background
        self.menu.grid.draw(self.screen)

        # If mouse is somewhere on the screen, highlight tiles
        # that located below the mouse.
        self.menu.mouseglow.draw(self.screen, mouse)

        # Draw menu elements, buttons and title
        self.menu.tiles.draw(self.screen, self.menu.mouseglow.positions,
                             self.iter_counter)

        # Check if the mouse is on top of the button, highlight button if so.
        self.menu.hover(mouse, self.iter_counter)

    def render_game(self):
        """Render game screen"""
        # Move snake based on update_rate value if the game is active.
        if self.iter_counter % self.game.update_rate == 0 and self.game.active:
            # Update apple.
            apple_eaten = self.game.apple.update(self.screen,
                                                 self.game.snake.positions)

            # Check if snake ate the apple.
            if apple_eaten:
                # If so, create particle animation for a new apple.
                particles = [Particle(self.game.apple.position,
                                      ParticlePresets.apple())
                             for i in range(30)]
                self.game.animations += particles

            # Check if snake bit its own tail.
            if self.game.snake.move(apple_eaten):
                # If so, render gameover screen.
                self.screen_type = 'over'

            # Reset animation stage value.
            self.game.snake_jump = 0

        # Change apple color if apple in searchlight.
        if self.game.apple.position in self.game.searchlight.positions:
            self.game.apple.body_color = Colors.apple_in_searchlight
        else:
            self.game.apple.body_color = Colors.apple

        # Reset the screen
        self.screen.fill(Colors.black)

        # Draw grid and searchlight
        self.game.grid.draw(self.screen)
        self.game.searchlight.draw(self.screen)

        # Draw animations
        for anime in self.game.animations:
            anime.draw(self.screen)

        self.game.apple.draw(self.screen)

        # Draw snake or snake animation based on snake_jump value
        self.game.snake_jump = self.game.snake.draw(self.screen,
                                                    self.game.snake_jump)

        # Draw a cover for score to be displayed on top.
        self.game.cover.draw(self.screen)

        # Update and draw score.
        self.game.score = len(self.game.snake.positions) - 2
        self.game.label.draw(self.screen, self.game.score)

        # Remove all animations with expired lifetime.
        self.game.animations = [particle for particle in self.game.animations
                                if particle.alive]

    def render_pause(self):
        """Render pause screen."""
        mouse = pygame.mouse.get_pos()

        # Set game to inactive to stop position updates.
        self.game.active = False
        self.render_game()

        # Cover game with transparent screen.
        self.pause.cover_all.draw(self.screen)
        self.pause.cover_score.draw(self.screen)

        # Draw pause screen on top.
        self.pause.mouseglow.draw(self.screen, mouse, update_only=True)
        self.pause.tiles.draw(self.screen, self.pause.mouseglow.positions,
                              self.iter_counter)
        self.pause.hover(mouse, self.iter_counter)

    def render_over(self):
        """Render gameover screen."""
        mouse = pygame.mouse.get_pos()

        # Set game to inactive to stop position updates.
        self.game.active = False
        self.render_game()

        # Cover game with transparent screen.
        self.over.cover_all.draw(self.screen)
        self.over.cover_score.draw(self.screen)

        # Draw over screen on top.
        self.over.mouseglow.draw(self.screen, mouse, update_only=True)
        self.over.tiles.draw(self.screen, self.over.mouseglow.positions,
                             self.iter_counter)
        self.over.hover(mouse, self.iter_counter)
