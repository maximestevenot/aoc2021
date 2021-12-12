import logging
from dataclasses import dataclass
from typing import Optional


@dataclass
class Coordinates:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Point:
    coord: Coordinates
    value: int

    def __hash__(self):
        return hash((self.value, self.coord))

    def __lt__(self, other):
        return self.value < other.value


class Matrix:
    def __init__(self):
        self.content = {}
        self.logger = logging.getLogger()

    def add_row(self, index: int, row: list[int]) -> None:
        self.content[index] = row

    def get(self, x: int, y: int) -> Optional[Point]:
        row = self.content.get(x)
        return Point(Coordinates(x, y), row[y]) if row and y in range(0, len(row)) else None

    def get_neighbours(self, x: int, y: int):
        neighbours = set()

        neighbours.add(self.get(x - 1, y))
        neighbours.add(self.get(x + 1, y))
        neighbours.add(self.get(x, y - 1))
        neighbours.add(self.get(x, y + 1))

        return filter(lambda n: n is not None, neighbours)

    def from_raw_input(self, table: list[str]):
        for i, row in enumerate(table):
            self.add_row(i, [int(c) for c in row])
        return self
