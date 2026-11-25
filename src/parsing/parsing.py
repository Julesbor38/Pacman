import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


MIN_LEVELS = 10
DEFAULT_LEVEL = {"width": 21, "height": 15}

BOUNDS: dict[str, tuple[int, int]] = {
    "lives": (1, 10),
    "points_per_pacgum": (0, 10_000),
    "points_per_super_pacgum": (0, 10_000),
    "points_per_ghost": (0, 10_000),
    "seed": (0, 2**31 - 1),
    "level_max_time": (10, 600),
    "width": (15, 101),
    "height": (15, 101),
}

def default_levels() -> list[dist[str, int]]:
	return [dict(DEFAULT_LEVEL) for _ in range(MIN_LEVELS)]


@dataclass
class Config:
	highscore_filename: str = "highscores.json"
	lives: int = 3
	pacgum: int = 42
	points_per_pacgum: int = 10
	points_per_super_pacgum: int = 50
	point_per_ghost: int = 200
	seed: int = 42
	level_max_time: int = 90
	levels: list[dict[str, int]] = field(default_factory=default_levels)

def _warn(message: str) -> None:
	print(f"config warning: {message}", file=sys.stderr)

def _check_value(name: str, value: Any, default: Any) -> Any:
	if type(value) is not type(default):
		_warn(f"{name} : expected {type(default).__name__}, using {default}")
		return default
	if isinstance(value, str) and not value.strip():
		_warn(f"{name}: empty string using {default}")
		return default
	if name in BOUNDS:
		low, high = BOUNDS[name]
		if not low <= value <= high:
			clamped = min(max(value, low), high)
			_warn(f"{name} out of range, clamped to {clamped}")
			return clamped
	return value


