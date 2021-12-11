from common.day import Day
from days.day1 import Day1
from days.day10 import Day10
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from days.day5 import Day5
from days.day6 import Day6
from days.day7 import Day7
from days.day9 import Day9


class UnimplementedDayException(Exception):
    pass


def default_file_name(index: int, example: bool) -> str:
    return f"day_{index}_example.txt" if example else f"day_{index}.txt"


class DayFactory:
    @staticmethod
    def get(index: int, example: bool) -> Day:
        if index == 1:
            return Day1(default_file_name(index, example))
        if index == 2:
            return Day2(default_file_name(index, example))
        if index == 3:
            return Day3(default_file_name(index, example))
        if index == 4:
            return Day4(default_file_name(index, example))
        if index == 5:
            return Day5(default_file_name(index, example))
        if index == 6:
            return Day6(default_file_name(index, example))
        if index == 7:
            return Day7(default_file_name(index, example))
        if index == 9:
            return Day9(default_file_name(index, example))
        if index == 10:
            return Day10(default_file_name(index, example))
        else:
            raise UnimplementedDayException(f'Day {index} not implemented')
