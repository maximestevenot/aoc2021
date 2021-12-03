from dataclasses import dataclass

ZERO = "0"
ONE = "1"


class BitsSequence:

    def __init__(self, sequence: str = ""):
        self.sequence = sequence

    def append(self, bit: str) -> None:
        self.sequence += bit if bit in [ZERO, ONE] else ""

    def opposite(self):
        opposite_sequence = BitsSequence()
        for b in self.sequence:
            opposite_sequence.append(str(abs(int(b) - 1)))
        return opposite_sequence

    def __str__(self):
        return self.sequence

    def __int__(self):
        return int(self.sequence, 2)


@dataclass
class BitsCount:
    zero: int = 0
    one: int = 0

    def max(self) -> int:
        return max(self.zero, self.one)

    def min(self) -> int:
        return min(self.zero, self.one)

    def max_bit(self) -> str:
        return ONE if self.max() == self.one else ZERO

    def min_bit(self) -> str:
        return ZERO if self.max() == self.one else ONE

    def __str__(self):
        return f"zero: {self.zero}, one: {self.one}"

    def increment(self, bit: str) -> None:
        if bit == ZERO:
            self.zero += 1
        else:
            self.one += 1
