from common.day import Day


def compute_fuel_consumption_part_1(position: int, target_position: int) -> int:
    return abs(position - target_position)


def compute_fuel_consumption_part_2(position: int, target_position: int) -> int:
    return sum(range(1, abs(position - target_position) + 1))


class Day7(Day):

    def part1(self) -> int:
        return self.compute_min_fuel(compute_fuel_consumption_part_1)

    def part2(self) -> int:
        return self.compute_min_fuel(compute_fuel_consumption_part_2)

    def compute_min_fuel(self, compute_fuel_consumption) -> int:
        positions = self.read_input_integers_one_line()
        self.logger.debug(positions)

        target_positions = list(range(min(positions), max(positions)))
        fuel_list = []
        for tp in target_positions:
            fuel = 0
            for p in positions:
                fuel += compute_fuel_consumption(p, tp)
            fuel_list.append((tp, fuel))

        min_fuel = min(fuel_list, key=lambda x: x[1])
        self.logger.debug(min_fuel)
        return min_fuel[1]
