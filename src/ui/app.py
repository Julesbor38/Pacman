"""Main Pygame window controller."""

import pygame


class App:
    """Manages the game window and main loop."""

    def __init__(self, width: int = 800, height: int = 600) -> None:
        """Initialize Pygame and open the window."""
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pac-Man")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        """Run the main loop until the user quits."""
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self) -> None:
        """Read window and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def render(self) -> None:
        """Clear the screen and display the new frame."""
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
