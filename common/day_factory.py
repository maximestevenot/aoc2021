from common.day import Day
from days.day1 import Day1
from days.day10 import Day10
from days.day11 import Day11
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from days.day5 import Day5
from days.day6 import Day6
from days.day7 import Day7
from days.day8 import Day8
from days.day9 import Day9


class UnimplementedDayException(Exception):
    pass


class DayFactory:
    @staticmethod
    def get(index: int, example: bool) -> Day:
        file_name = f"day_{index}_example.txt" if example else f"day_{index}.txt"

        if index == 1:
            return Day1(file_name)
        if index == 2:
            return Day2(file_name)
        if index == 3:
            return Day3(file_name)
        if index == 4:
            return Day4(file_name)
        if index == 5:
            return Day5(file_name)
        if index == 6:
            return Day6(file_name)
        if index == 7:
            return Day7(file_name)
        if index == 8:
            return Day8(file_name)
        if index == 9:
            return Day9(file_name)
        if index == 10:
            return Day10(file_name)
        if index == 11:
            return Day11(file_name)
        else:
            raise UnimplementedDayException(f'Day {index} not implemented')
