from common.day import Day


class Day1(Day):
    def get_answer(self) -> str:
        return ' '.join(self.read_input_lines())
