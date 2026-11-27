"""Instructions screen showing the controls and the rules."""

import pygame

from .base import Screen
from ..state import State
from ...parsing import Config


class InstructionsScreen(Screen):
    """Screen listing the game controls, the rules and the points.

    The points and level values are read from the configuration, so the
    screen always matches the loaded config file.
    """

    def __init__(self, config: Config) -> None:
        """Build the lines to display from the configuration.

        Args:
            config: Game configuration loaded from the JSON file.
        """
        self.font = pygame.font.Font(None, 32)
        self.lines: list[str] = [
            "INSTRUCTIONS",
            "",
            "Arrows / WASD : move",
            "Escape : pause",
            "Cheat mode : ???",
            "",
            "Eat every pacgum to clear the level",
            "Avoid the ghosts: they cost you a life",
            "Super-pacgums make ghosts edible",
            "",
            f"Pacgum: {config.points_per_pacgum} points",
            f"Super-pacgum: {config.points_per_super_pacgum} points",
            f"Ghost: {config.points_per_ghost} points",
            f"{len(config.levels)} levels, {config.level_max_time}s each",
            "",
            "Press Escape to go back",
        ]

    def handle_event(self, event: pygame.event.Event) -> State | None:
        """Go back to the main menu when Escape is pressed.

        Args:
            event: The pygame event to handle.

        Returns:
            State.MENU when Escape is pressed, otherwise None.
        """
        if event.type != pygame.KEYDOWN:
            return None
        if event.key == pygame.K_ESCAPE:
            return State.MENU
        return None

    def render(self, surface: pygame.Surface) -> None:
        """Draw every line centered, with the title in yellow.

        Args:
            surface: The surface to draw on.
        """
        surface.fill((0, 0, 0))
        for index, line in enumerate(self.lines):
            if index == 0:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            image = self.font.render(line, True, color)
            y = 40 + index * 32
            x = (surface.get_width() - image.get_width()) // 2
            surface.blit(image, (x, y))
