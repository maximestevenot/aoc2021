from common.algebra import Point, Matrix
from common.day import Day


class Heightmap(Matrix):

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
        self.matrix = Heightmap().from_raw_input(self.read_input_lines())

    def part1(self) -> int:
        low_points = self.matrix.get_low_points()
        result = 0
        for p in low_points:
            result += p.value + 1
        return result

    def part2(self) -> int:
        return -1
