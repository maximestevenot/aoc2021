from common.day import Day
from util.iterators import window


class Day1(Day):

    def part1(self) -> str:
        return str(self.count_increased_depth(self.read_input_integers()))

    def part2(self) -> str:
        sum_per_three = list(map(lambda x: sum(x), window(self.read_input_integers(), n=3)))
        return str(Day1.count_increased_depth(sum_per_three))

    @staticmethod
    def count_increased_depth(depth_list: list[int]) -> int:
        return len(list(filter(lambda x: x[0] < x[1], window(depth_list))))
