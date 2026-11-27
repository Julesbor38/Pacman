"""Pac-gums and super pac-gums: where they are and what eating them gives."""

from dataclasses import dataclass, field

from ..maze import PILLAR_42

Cell = tuple[int, int]


@dataclass
class Pellets:
    """Cells that still hold a pac-gum or a super pac-gum."""

    dots: set[Cell] = field(default_factory=set)
    super_dots: set[Cell] = field(default_factory=set)

    def eat(self, cell: Cell) -> str | None:
        """Remove the pellet on this cell and return its kind, if any."""
        if cell in self.dots:
            self.dots.remove(cell)
            return "pacgum"
        if cell in self.super_dots:
            self.super_dots.remove(cell)
            return "super"
        return None

    def is_empty(self) -> bool:
        """Return True when every pellet has been eaten."""
        return not self.dots and not self.super_dots


def create_pellets(
    maze: list[list[int]], start: Cell | None = None
) -> Pellets:
    """Put a pac-gum on every free cell, then a super pac-gum in each corner."""
    height = len(maze)
    width = len(maze[0])
    pellets = Pellets()
    for y in range(height):
        for x in range(width):
            if maze[y][x] != PILLAR_42 and (x, y) != start:
                pellets.dots.add((x, y))
    corners = [
        (0, 0),
        (width - 1, 0),
        (0, height - 1),
        (width - 1, height - 1),
    ]
    for corner in corners:
        if corner in pellets.dots:
            pellets.dots.remove(corner)
            pellets.super_dots.add(corner)
    return pellets
