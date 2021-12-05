import re
from dataclasses import dataclass

from common.day import Day


@dataclass
class Coordinates:
    x: int
    y: int

    def norm(self) -> int:
        return abs(self.x - self.y)


@dataclass
class Line:
    start_coord: Coordinates
    end_coord: Coordinates

    def is_horizontal(self) -> bool:
        return self.start_coord.y == self.end_coord.y

    def is_vertical(self) -> bool:
        return self.start_coord.x == self.end_coord.x

    def is_diagonal(self) -> bool:
        # return (self.start_coord.x == self.start_coord.y and self.end_coord.x == self.end_coord.y) or \
        #        (self.start_coord.x == self.end_coord.y and self.start_coord.y == self.end_coord.x)
        return self.start_coord.norm() == self.end_coord.norm()

    def max_x(self) -> int:
        return max(self.end_coord.x, self.start_coord.x)

    def max_y(self) -> int:
        return max(self.end_coord.y, self.start_coord.y)

    def min_x(self) -> int:
        return min(self.end_coord.x, self.start_coord.x)

    def min_y(self) -> int:
        return min(self.end_coord.y, self.start_coord.y)


class Day5(Day):

    def part1(self) -> int:
        lines = self.get_lines()
        play_board = self.init_play_board(lines)
        self.fill_play_board(lines, play_board)
        return self.count_overlap(play_board)

    def part2(self) -> int:
        lines = self.get_lines()
        play_board = self.init_play_board(lines)
        self.fill_play_board(lines, play_board, True)
        return self.count_overlap(play_board)

    @staticmethod
    def count_overlap(play_board):
        overlap_count = 0
        for p in play_board:
            overlap_count += len(list(filter(lambda x: x > 1, p)))
        return overlap_count

    def init_play_board(self, lines) -> list[list[int]]:
        x_max = max(l.max_x() for l in lines)
        y_max = max(l.max_y() for l in lines)
        self.logger.debug(f"x_max={x_max}, y_max={y_max}")
        # return [[0] * (x_max + 1)] * (y_max + 1)
        return [[0 for i in range(x_max + 1)] for j in range(y_max + 1)]

    def get_lines(self) -> list[Line]:
        table = self.read_input_lines()
        lines = []
        for row in table:
            num = [int(s) for s in re.findall(r"\d+", row)]
            line = Line(start_coord=Coordinates(x=num[0], y=num[1]),
                        end_coord=Coordinates(x=num[2], y=num[3]))
            self.logger.debug(line)
            lines.append(line)
        return lines

    def fill_play_board(self, lines: list[Line],
                        play_board: list[list[int]],
                        manage_diagonals: bool = False) -> None:
        for line in lines:
            if line.is_vertical():
                self.logger.debug(f'vertical: {line}')
                for y in range(line.min_y(), line.max_y() + 1):
                    play_board[y][line.start_coord.x] += 1
            elif line.is_horizontal():
                self.logger.debug(f'horizontal: {line}')
                for x in range(line.min_x(), line.max_x() + 1):
                    play_board[line.start_coord.y][x] += 1
            elif manage_diagonals:
                self.logger.debug(f'diagonal: {line}')
                diagonal_points = self.get_diagonal_points(line.start_coord, line.end_coord)
                for point in diagonal_points:
                    play_board[point.x][point.y] += 1
            else:
                self.logger.debug(f'excluded: {line}')

    def get_diagonal_points(self, start_coord: Coordinates, end_coord: Coordinates):
        start_x = start_coord.x
        start_y = start_coord.y
        end_x = end_coord.x
        end_y = end_coord.y
        if start_x > end_x:
            start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

        coords = []

        slope = (end_y - start_y) // (end_x - start_x)
        for x, y in zip(range(start_x, end_x), range(start_y, end_y, slope)):
            coords.append(Coordinates(y, x))
        coords.append(Coordinates(end_y, end_x))

        self.logger.debug(coords)
        return coords
