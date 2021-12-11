import logging
from dataclasses import dataclass
from typing import Optional

from common.day import Day
from common.geometry import Coordinates


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

        return filter(lambda x: x is not None, neighbours)

    def get_low_points(self) -> set[Point]:
        low_points = set()
        for x in self.content:
            for y in range(len(self.content[x])):
                point = self.get(x, y)
                neighbours = self.get_neighbours(x, y)
                if point < min(neighbours):
                    low_points.add(point)
        self.logger.debug(low_points)
        return low_points


class Day9(Day):

    def __init__(self, input_file_name: str):
        super().__init__(input_file_name)
        self.matrix = self.build_matrix()

    def part1(self) -> int:
        low_points = self.matrix.get_low_points()
        result = 0
        for p in low_points:
            result += p.value + 1
        return result

    def part2(self) -> int:
        return -1

    def build_matrix(self):
        matrix = Matrix()
        table = self.read_input_lines()
        index = 0
        for row_string in table:
            row_int = []
            for char in row_string:
                row_int.append(int(char))
            matrix.add_row(index, row_int)
            index += 1
        return matrix

