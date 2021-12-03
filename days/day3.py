from common.bits import BitsSequence, BitsCount
from common.day import Day


class Day3(Day):

    def part1(self) -> int:
        table = self.read_input_lines()
        table_bits_count = self.count_table_bits(table)

        gamma_rate = self.compute_gamma_rate(table_bits_count)
        epsilon_rate = gamma_rate.opposite()

        return int(gamma_rate) * int(epsilon_rate)

    def part2(self) -> int:
        table = self.read_input_lines()

        oxygen_data = self.filter_table(Day3.filter_oxygen_data, 0, len(table[0]), table)
        co2_data = self.filter_table(Day3.filter_co2_data, 0, len(table[0]), table)

        oxygen_scrubber_rating = BitsSequence(oxygen_data[0])
        co2_scrubber_rating = BitsSequence(co2_data[0])

        return int(co2_scrubber_rating) * int(oxygen_scrubber_rating)

    @staticmethod
    def compute_gamma_rate(table_bits_count) -> BitsSequence:
        gamma_rate = BitsSequence()
        for col in table_bits_count:
            gamma_rate.append(col.max_bit())
        return gamma_rate

    @staticmethod
    def count_table_bits(table: list[str]) -> list[BitsCount]:
        result = []
        for i in range(len(table[0])):
            result.append(Day3.count_column_bits(table, i))
        return result

    @staticmethod
    def count_column_bits(table: list[str], col_index: int) -> BitsCount:
        counter = BitsCount()
        for line in table:
            counter.increment(line[col_index])
        return counter

    @staticmethod
    def filter_oxygen_data(column_index: int, bits_count, table: list[str]) -> list[str]:
        return list(filter(lambda x: x[column_index] == bits_count.max_bit(), table))[0:bits_count.max()]

    @staticmethod
    def filter_co2_data(column_index: int, bits_count, table: list[str]) -> list[str]:
        return list(filter(lambda x: x[column_index] == bits_count.min_bit(), table))[0:bits_count.min()]

    def filter_table(self, list_filter, column_index: int, last_column_index: int, table: list[str]) -> list[str]:
        if column_index < last_column_index and len(table) > 1:
            filtered_table = list_filter(column_index, self.count_column_bits(table, column_index), table)
            return self.filter_table(list_filter, column_index + 1, last_column_index, filtered_table)
        return table
