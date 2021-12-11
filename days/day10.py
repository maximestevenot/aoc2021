from common.day import Day


class Day10(Day):
    pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}

    def part1(self) -> int:
        coef = {')': 3, ']': 57, '}': 1197, '>': 25137}
        table = self.read_input_lines()
        result = 0
        for row in table:
            closing_stack = []
            for symbol in row:
                if symbol in self.pairs:
                    closing_stack.append(self.pairs[symbol])
                elif symbol != closing_stack.pop():
                    result += coef[symbol]
                    break
        return result

    def part2(self) -> int:
        coef = {")": 1, "]": 2, "}": 3, ">": 4}
        table = self.read_input_lines()
        corrupted_symbols = []
        remaining_symbols = []
        for row in table:
            closing_stack = []
            is_corrupted_row = False
            for symbol in row:
                if symbol in self.pairs:
                    closing_stack.append(self.pairs[symbol])
                elif symbol != closing_stack.pop():
                    corrupted_symbols.append(symbol)
                    is_corrupted_row = True
                    break
            if not is_corrupted_row and len(closing_stack) > 0:
                remaining_symbols.append(closing_stack)

        scores = []
        for stack in remaining_symbols:
            row_score = 0
            self.logger.debug(stack)
            for i, symbol in enumerate(stack):
                row_score += 5 ** i * coef[symbol]
            self.logger.debug(row_score)
            scores.append(row_score)
            
        scores = sorted(scores)
        return scores[len(scores) // 2]
