import abc
from os import path


class Day(abc.ABC):
    def __init__(self, input_file_name: str):
        self.input_file = path.join("inputs", input_file_name)

    def read_input_lines(self) -> list[str]:
        with open(self.input_file, 'r') as file:
            return [x.strip() for x in file.readlines()]

    @abc.abstractmethod
    def get_answer(self) -> str:
        pass
