from common.day import Day
from days.day1 import Day1
from days.day2 import Day2


class UnimplementedDayException(Exception):
    pass


def default_file_name(index: int) -> str:
    return f"day_{index}.txt"


class DayFactory:
    @staticmethod
    def get(index: int) -> Day:
        if index == 1:
            return Day1(default_file_name(index))
        if index == 2:
            return Day2(default_file_name(index))
        else:
            raise UnimplementedDayException(f'Day {index} not implemented')
