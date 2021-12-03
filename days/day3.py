from common.day import Day


class Day3(Day):

    def part1(self) -> int:
        table = self.read_input_lines()
        result = []
        for i in range(len(table[0])):
            one = 0
            zero = 0
            for line in table:
                if line[i] == "0":
                    zero += 1
                else:
                    one += 1
            result.append((one, zero))
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

    def part2(self) -> int:
        return -9999999999
