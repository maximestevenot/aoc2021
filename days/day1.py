from itertools import tee

from common.day import Day


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class Day1(Day):
    def get_answer(self) -> str:
        counter = 0
        for (a, b) in pairwise(self.read_input_integers()):
            if a < b:
                counter += 1
        return str(counter)
