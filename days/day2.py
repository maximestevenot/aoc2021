from common.day import Day


class Day2(Day):
    UP = "up"
    DOWN = "down"
    FORWARD = "forward"

    def __init__(self, input_file_name: str):
        super().__init__(input_file_name)
        self.movement_list = self.get_movement_list()

    def get_movement_list(self):
        return list(map(lambda x: Day2.split_and_convert(x), self.read_input_lines()))

    @staticmethod
    def split_and_convert(line: str) -> (str, int):
        move = line.split(" ")
        return move[0], int(move[1])

    def part1(self) -> int:
        depth, horizontal_position = self.compute_positions_part1()
        return depth * horizontal_position

    def part2(self) -> int:
        depth, horizontal_position = self.compute_positions_part2()
        return depth * horizontal_position

    def compute_positions_part1(self):
        depth = 0
        horizontal_position = 0

        for direction, distance in self.movement_list:
            if direction == self.UP:
                depth -= distance
            elif direction == self.DOWN:
                depth += distance
            elif direction == self.FORWARD:
                horizontal_position += distance

        return depth, horizontal_position

    def compute_positions_part2(self):
        depth = 0
        horizontal_position = 0
        aim = 0

        for direction, distance in self.movement_list:
            if direction == self.UP:
                aim -= distance
            elif direction == self.DOWN:
                aim += distance
            elif direction == self.FORWARD:
                horizontal_position += distance
                depth += (aim * distance)

        return depth, horizontal_position
