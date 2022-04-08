def solution(start: int, length: int) -> int:
    def xor_to(n: int) -> int:
        return {0: n, 1: 1, 2: n + 1, 3: 0}[n % 4]

    # xor range up to the last id checked
    result: int = xor_to(start + length * (length - 1))

    # remove range of numbers before start
    result ^= xor_to(start - 1)

    # remove range of numbers at the end of the line
    for line in range(1, length - 1):
        last_id: int = start + length * (line + 1) - 1
        result ^= xor_to(last_id)
        result ^= xor_to(last_id - line)

    return result


if __name__ == "__main__":

    def print_solution(start: int, length: int) -> None:
        print("(", start, ",", length, ") ->", solution(start, length))

    print_solution(0, 3)
    print_solution(17, 4)
