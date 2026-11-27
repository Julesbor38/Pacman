"""Main Pygame window controller."""

import pygame
from .screens.base import Screen
from .screens.main_menu import MainMenu
from .state import State
from .screens.instructions import InstructionsScreen
from ..parsing import Config


class App:
    """Manage the game window, the main loop and the current screen.

    The app keeps one screen per state and forwards events and drawing
    to the screen of the current state.
    """

    def __init__(self, config: Config,
                 width: int = 800,
                 height: int = 600) -> None:
        """Initialize Pygame, create the screens and open the window.

        Args:
            config: Game configuration loaded from the JSON file.
            width: Width of the window, in pixels.
            height: Height of the window, in pixels.
        """
        pygame.init()
        self.screens: dict[State, Screen] = {
            State.MENU: MainMenu(),
            State.INSTRUCTIONS: InstructionsScreen(config),
        }
        self.state = State.MENU
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
        """Read events and forward them to the current screen.

        Closing the window stops the app. When the
        current screen returns a new state, switch to it if its screen
        exists, or stop the app if the state is EXIT.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                next_state = self.screens[self.state].handle_event(event)
                if next_state == State.EXIT:
                    self.running = False
                elif next_state in self.screens:
                    self.state = next_state

    def render(self) -> None:
        """Draw the current screen and display the new frame."""
        self.screens[self.state].render(self.screen)
        pygame.display.flip()
