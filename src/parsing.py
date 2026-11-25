import json
import sys
from dataclasses import dataclass, field, fields
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


def default_levels() -> list[dict[str, int]]:
    return [dict(DEFAULT_LEVEL) for _ in range(MIN_LEVELS)]


@dataclass
class Config:
    highscore_filename: str = "highscores.json"
    lives: int = 3
    pacgum: int = 42
    points_per_pacgum: int = 10
    points_per_super_pacgum: int = 50
    points_per_ghost: int = 200
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


def _read_levels(raw: Any) -> list[dict[str, int]]:

    if not isinstance(raw, list):
        _warn("level: list expected, using default levels")
        return default_levels()
    levels: list[dict[str, int]] = []
    for index, entry in enumerate(raw, start=1):
        if not isinstance(entry, dict):
            _warn(f"level {index} ignored: object expected")
            continue
        levels.append({
            key: _check_value(key, entry.get(key, DEFAULT_LEVEL[key]),
                              DEFAULT_LEVEL[key])
            for key in ("width", "height")
        })
    if len(levels) < MIN_LEVELS:
        _warn(f"{len(levels)} levels found, at least {MIN_LEVELS} required")
    return levels or default_levels()


def strip_comments(text: str) -> str:
    return "\n".join(line for line in text.splitlines()
                     if not line.lstrip().startswith("#"))


def load_config(path: str) -> Config:
    config = Config()
    file = Path(path)
    if not file.is_file():
        _warn(f"config file not found: {path}, using default")
        return config
    try:
        data = json.loads(strip_comments(file.read_text(encoding="utf-8")))
    except json.JSONDecodeError as error:
        _warn(f"Invalid JSON at line {error.lineno}:"
              f"{error.msg}, using default")
        return config
    except (OSError, UnicodeDecodeError) as error:
        _warn(f"cannot read {path}: {error}, using defaulst")
        return config
    if not isinstance(data, dict):
        _warn("config root must be a JSON object, using defaults")
        return config
    know_keys = {item.name for item in fields(Config)} | {"level"}
    for key in data:
        if key not in know_keys:
            _warn(f"unknow key '{key}' ignored")
    for item in fields(Config):
        if item.name == "levels" or item.name not in data:
            continue
        default = getattr(config, item.name)
        setattr(config, item.name, _check_value(
            item.name, data[item.name], default))
    if "level" in data:
        config.levels = _read_levels(data["level"])
    return config
