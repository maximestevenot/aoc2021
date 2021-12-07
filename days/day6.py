from common.day import Day


class Day6(Day):
    def part1(self) -> int:
        return self.count_fish_v2(80)

    def part2(self) -> int:
        return self.count_fish_v2(256)

    def count_fish_v2(self, nb_days: int):
        initial_population = self.read_input_integers_one_line()

        population_distribution = {}
        for i in range(9):
            population_distribution[i] = initial_population.count(i)

        self.logger.debug(f"Initial state : {initial_population}")
        self.logger.debug(population_distribution)

        for day in range(nb_days):
            new_population_distribution = {}
            for i in range(8):
                new_population_distribution[i] = population_distribution[i + 1]
            new_population_distribution[8] = population_distribution[0]
            new_population_distribution[6] += population_distribution[0]
            population_distribution = new_population_distribution

        pop_size = 0
        for i in range(9):
            pop_size += population_distribution[i]

        return pop_size
