"""States of the application, one for each screen."""

from enum import Enum, auto


class State(Enum):
    """Screens the application can be on."""
    MENU = auto()
    PLAYING = auto()
    HIGHSCORES = auto()
    INSTRUCTIONS = auto()
    EXIT = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    VICTORY = auto()
