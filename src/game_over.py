import pygame
import sys

class GameOver:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 64)
        self.options_font = pygame.font.SysFont("Arial", 48)
        self.options = ["RESTART GAME", "QUIT"]

    def draw(self, winner, winner_hits):
        self.screen.fill((0, 0, 0))  # Fill the screen with black

        # Game Over text
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        x = (self.width - game_over_text.get_width()) // 2
        y = self.height // 6
        self.screen.blit(game_over_text, (x, y))

        # Winner text
        winner_text = self.font.render(f"The winner is {winner}!", True, (255, 255, 0))
        x = (self.width - winner_text.get_width()) // 2
        y += 100  # Add spacing below "GAME OVER"
        self.screen.blit(winner_text, (x, y))

        # Winner hits text
        hits_text = self.font.render(f"You hit the ball a total of {winner_hits} times!", True, (255, 255, 255))
        x = (self.width - hits_text.get_width()) // 2
        y += 80  # Add spacing below "The winner is"
        self.screen.blit(hits_text, (x, y))

        # Draw options
        for index, option in enumerate(self.options):
            text = self.options_font.render(option, True, (255, 255, 255))
            x = (self.width - text.get_width()) // 2
            y += 100  # Add spacing for menu options
            self.screen.blit(text, (x, y))

        pygame.display.flip()

    def get_choice(self, winner, winner_hits):
        while True:
            self.draw(winner, winner_hits)  # Draw with winner and winner_hits

            # Base y position starts after all the texts above
            base_y = self.height // 6 + 100 + 80 + 100  # Match the y-spacing in draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for index, option in enumerate(self.options):
                        text = self.options_font.render(option, True, (255, 255, 255))
                        x = (self.width - text.get_width()) // 2
                        y = base_y + index * 100  # Proper y alignment for menu options
                        if x <= mouse_x <= x + text.get_width() and y <= mouse_y <= y + text.get_height():
                            return option