from common.day import Day

Entry = tuple[list[str], list[str]]


class Day8(Day):
    def part1(self) -> int:
        entries = self.read_entries()

        count = 0
        for pattern, output in entries:
            count += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], output)))

        return count

    def part2(self) -> int:
        return -1

    def read_entries(self) -> list[Entry]:
        entries = []
        for line in self.read_input_lines():
            sequences = line.split()
            entry = (sequences[:10], sequences[11:])
            self.logger.debug(entry)
            entries.append(entry)
        return entries
