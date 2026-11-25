import json
import logging
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Config:
	highscore_filename: str = "highscores.json"
	lives: int = 3
	pacgum: int = 42
	points_per_pacgum: int = 10
	points_per_super_pacgum: int = 50
	point_per_ghost: int = 200
	sedd: int = 42
	level_max_time: int = 90
	levels: list[dict[str, int]] = field(default_factory=lambda: [{"widht": 21, "height": 15}] * 10)

