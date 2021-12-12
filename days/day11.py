from common.algebra import Matrix
from common.day import Day


class Day11(Day):

    def __init__(self, input_file_name: str):
        super().__init__(input_file_name)
        self.matrix = Matrix().from_raw_input(self.read_input_lines())

    def part1(self) -> int:
        return -1

    def part2(self) -> int:
        return -1
