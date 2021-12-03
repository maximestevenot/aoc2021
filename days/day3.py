from common.day import Day

ZERO = "0"

ONE = "1"


class Day3(Day):

    def part1(self) -> int:
        table = self.read_input_lines()
        result = self.count_bits(table)
        mystr = ""
        for r in result:
            if max(r) == r[0]:
                mystr += "1"
            else:
                mystr += "0"
        gamma_rate = int(mystr, 2)

        uu = []
        for x in mystr:
            uu.append(str(abs(int(x) - 1)))
        epsilon_rate = int("".join(uu), 2)

        return gamma_rate * epsilon_rate

    @staticmethod
    def count_bits(table):
        result = []
        for i in range(len(table[0])):
            result.append(Day3.count_one_zero_col(table, i))
        return result

    @staticmethod
    def count_one_zero_col(table: list[str], col_index: int):
        one = 0
        zero = 0
        for line in table:
            if line[col_index] == "0":
                zero += 1
            else:
                one += 1
        return one, zero

    @staticmethod
    def get_max_bit(r: (int, int)):
        return ONE if max(r) == r[0] else ZERO

    @staticmethod
    def get_min_bit(r: (int, int)):
        return ZERO if max(r) == r[0] else ONE


    def part2(self) -> int:
        table = self.read_input_lines()
        # result = self.count_bits(table)
        new_table = self.filter_data_oxygen(0, table, len(table[0]))

        oxygen = int("".join(new_table), 2)

        table2 = self.filter_data_co2(0, table, len(table[0]))
        co2 = int("".join(table2), 2)

        return co2 * oxygen

    def filter_data_oxygen(self, i, table, stop):
        if i < stop and len(table) > 1:
            r = self.count_one_zero_col(table, i)
            new_table = list(filter(lambda x: x[i] == self.get_max_bit(r), table))
            return self.filter_data_oxygen(i+1, new_table[0:max(r)], stop)
        return table

    def filter_data_co2(self, i, table, stop):
        print(i)
        if i < stop and len(table) > 1:
            r = self.count_one_zero_col(table, i)
            print(r)
            new_table = list(filter(lambda x: x[i] == self.get_min_bit(r), table))
            print(new_table)
            return self.filter_data_co2(i+1, new_table[0:min(r)], stop)
        return table
