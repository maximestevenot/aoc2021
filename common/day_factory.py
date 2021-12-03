from common.day import Day
from days.day1 import Day1
from days.day2 import Day2
from days.day3 import Day3


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
        else:
            raise UnimplementedDayException(f'Day {index} not implemented')
