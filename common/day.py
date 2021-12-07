import abc
import logging
from os import path


class Day(abc.ABC):
    def __init__(self, input_file_name: str):
        self.input_file = path.join("inputs", input_file_name)
        self.logger = logging.getLogger()

    def read_input_lines(self) -> list[str]:
        self.logger.debug(f"Read {self.input_file}")
        with open(self.input_file, 'r') as file:
            return [x.strip() for x in file.readlines()]

    def read_input_integers(self) -> list[int]:
        return list(map(lambda x: int(x), self.read_input_lines()))

    def read_input_integers_one_line(self, separator: str = ',') -> list[int]:
        return [int(x) for x in self.read_input_lines()[0].split(separator)]

    @abc.abstractmethod
    def part1(self) -> int:
        pass

    @abc.abstractmethod
    def part2(self) -> int:
        pass
