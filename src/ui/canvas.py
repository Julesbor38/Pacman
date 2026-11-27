"""Pixel drawing helpers, built only on Surface.set_at (MLX-style)."""

import pygame

Color = tuple[int, int, int]


def put_pixel(surface: pygame.Surface, x: int, y: int, color: Color) -> None:
    """Set one pixel, ignoring coordinates outside the surface."""
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        surface.set_at((x, y), color)


def draw_line(
    surface: pygame.Surface,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    color: Color,
) -> None:
    """Draw a one-pixel line between two points (Bresenham)."""
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    step_x = 1 if x0 < x1 else -1
    step_y = 1 if y0 < y1 else -1
    error = dx + dy
    while True:
        put_pixel(surface, x0, y0, color)
        if x0 == x1 and y0 == y1:
            return
        double = 2 * error
        if double >= dy:
            error += dy
            x0 += step_x
        if double <= dx:
            error += dx
            y0 += step_y
