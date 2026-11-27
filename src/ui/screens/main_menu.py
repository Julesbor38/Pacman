"""Main menu screen of the game."""
import pygame
from .base import Screen
from ..state import State


class MainMenu(Screen):
    """Main menu listing the options the player can choose from.

    The player moves the selection with the arrow keys or W/S
    and confirms with Enter.
    """
    def __init__(self) -> None:
        """Create the menu options and select the first one."""
        self.options: list[tuple[str, State]] = [
            ("Start Game", State.PLAYING),
            ("Highscores", State.HIGHSCORES),
            ("Instructions", State.INSTRUCTIONS),
            ("Exit", State.EXIT),
        ]
        self.selected: int = 0
        self.font = pygame.font.Font(None, 48)

    def handle_event(self, event: pygame.event.Event) -> State | None:
        """Move the selection or confirm the selected option.

        Args:
            event: The pygame event to handle.

        Returns:
            The state of the selected option when Enter is pressed,
            otherwise None to stay on the menu.
        """
        if event.type != pygame.KEYDOWN:
            return None
        if event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected = (self.selected + 1) % len(self.options)
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.selected = (self.selected - 1) % len(self.options)
        elif event.key == pygame.K_RETURN:
            return self.options[self.selected][1]
        elif event.key == pygame.K_ESCAPE:
            return State.EXIT
        return None

    def render(self, surface: pygame.Surface) -> None:
        """Draw the menu options, highlighting the selected one.

        Args:
            surface: The surface to draw on.
        """
        surface.fill((0, 0, 0))
        for index, (text, _) in enumerate(self.options):
            if index == self.selected:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            image = self.font.render(text, True, color)
            y = 200 + index * 60
            x = (surface.get_width() - image.get_width()) // 2
            surface.blit(image, (x, y))
