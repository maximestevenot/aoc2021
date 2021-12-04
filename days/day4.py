from dataclasses import dataclass

from common.day import Day


class NoWinnerException(Exception):
    pass


@dataclass
class Cell:
    value: int
    is_marked: bool = False

    def mark(self, val: int) -> bool:
        self.is_marked = (self.value == val)
        return self.is_marked


class Board:
    def __init__(self, matrix: list[list[Cell]]):
        self.matrix = matrix
        self.coord = {}
        self.init_coordinates()
        self.is_winner = False
        self.result = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0],
        }

    def init_coordinates(self):
        y = 0
        for row in self.matrix:
            x = 0
            for cell in row:
                self.coord[cell.value] = (y, x)
                x += 1
            y += 1

    def sum_unmarked(self) -> int:
        total = 0
        for row in self.matrix:
            for cell in row:
                if not cell.is_marked:
                    total += cell.value
        return total

    def check_number(self, num: int) -> (int, int, int):
        if self.is_winner:
            return ()
        coord = self.coord.get(num)
        if coord:
            y, x = coord
            cell = self.matrix[y][x]
            cell.mark(num)
            if cell.is_marked:
                self.update_result(x, y)
            if self.is_bingo():
                sum_unmarked = self.sum_unmarked()
                return num * sum_unmarked, num, sum_unmarked

        return ()

    def update_result(self, x: int, y: int):
        self.result["row"][y] += 1
        self.result["col"][x] += 1

    def is_bingo(self) -> bool:
        self.is_winner = 5 in self.result["row"] or 5 in self.result["col"]
        return self.is_winner


class Day4(Day):

    def part1(self) -> int:
        table = self.read_input_lines()
        sequence_str = table.pop(0)
        sequence = [int(s) for s in sequence_str.split(',') if s.isdigit()]
        boards = self.build_boards(table)

        for num in sequence:
            for b in boards:
                result = b.check_number(num)
                if result:
                    return result[0]

        raise NoWinnerException()

    def part2(self) -> int:
        table = self.read_input_lines()
        sequence_str = table.pop(0)
        sequence = [int(s) for s in sequence_str.split(',') if s.isdigit()]
        boards = self.build_boards(table)

        winner_board = ()
        for num in sequence:
            for b in boards:
                result = b.check_number(num)
                if result:
                    winner_board = result

        if winner_board:
            return winner_board[0]
        else:
            raise NoWinnerException()

    @staticmethod
    def build_boards(table) -> list[Board]:
        raw_boards = Day4.extract_raw_boards(table)
        boards = []
        for r in raw_boards:
            numbers = list(map(lambda x: [int(s) for s in x.split() if s.isdigit()], r))
            boards.append(Board(list(map(lambda x: [Cell(value=v) for v in x], numbers))))
        return boards

    @staticmethod
    def extract_raw_boards(table: list[str]) -> list[list[str]]:
        raw_board = []
        for i in range(len(table) // 6):
            raw_board.append(table[6 * i + 1:6 + 6 * i])
        return raw_board
