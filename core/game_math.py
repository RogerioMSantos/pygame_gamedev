
from __future__ import annotations

import math
from typing import Iterable, Tuple, Union


def dist(p1: Iterable[float], p2: Iterable[float]) -> float:
    """ Multidimensional euclidean distance """
    d = 0
    for c1, c2 in zip(p1, p2):
        d += (c1 - c2) ** 2
    return math.sqrt(d)


def cartesian2polar(x: float, y: float) -> Tuple[float, float]:
    angle = math.degrees(math.atan2(y, x))
    radius = math.sqrt(x ** 2 + y ** 2)
    return (angle, radius)


def polar2cartesian(angle_degrees: float, radius: float) -> Tuple[float, float]:
    angle_rad = math.radians(angle_degrees)
    x = math.cos(angle_rad) * radius
    y = math.sin(angle_rad) * radius
    return (x, y)


class Vector2d:
    def __init__(self, x=0.0, y=0.0):
        self.x: float = x
        self.y: float = y

    def __add__(self, other: Vector2d):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2d):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, Vector2d]) -> Union[float, Vector2d]:
        if isinstance(other, (int, float)):
            return Vector2d(self.x * other, self.y * other)
        if isinstance(other, Vector2d):
            return self.x * other.x + self.y * other.y

        raise TypeError(f"Unsupported operand type for *: 'Vector2d' and '{type(other).__name__}'.")

    def __str__(self):
        return f"(x={self.x:.2f}, y={self.y:.2f})"

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return math.atan2(self.y, self.x)

    def as_tuple(self):
        return (self.x, self.y)

    @staticmethod
    def from_polar(angle_degrees, radius):
        x, y = polar2cartesian(angle_degrees, radius)
        return Vector2d(x, y)
