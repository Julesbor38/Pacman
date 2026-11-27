"""Base class shared by every screen of the application."""
import pygame
from ..state import State


class Screen:
    """Base class for every screen.

    Each screen (menu, pause, highscores...) inherits from this class
    and overrides only the methods it needs.
    """

    def handle_event(self, event: pygame.event.Event) -> State | None:
        """Handle one input event.

        Args:
            event: The pygame event to handle.

        Returns:
            The next state, or None to stay on this screen.
        """
        return None

    def update(self, dt: float) -> None:
        """Update the screen logic.

        Args:
            dt: Time elapsed since the last frame, in seconds.
        """
        pass

    def render(self, surface: pygame.Surface) -> None:
        """Draw the screen.

        Args:
            surface: The surface to draw on.
        """
        pass
