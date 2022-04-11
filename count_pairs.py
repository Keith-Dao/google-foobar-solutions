from collections import defaultdict


def solution(banana_list: list[int]) -> int:

    n = len(banana_list)
    assert 1 <= n <= 100

    banana_map: dict[int, set[int]] = defaultdict(set)
    for i in range(n):
        banana_map[banana_list[i]].add(i)

    terminating_pairs: dict[int, set] = defaultdict(set)
    bananas: list[int] = list(sorted(banana_map.keys()))
    n_b: int = len(bananas)

    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    def does_terminate(x: int, y: int) -> bool:
        if x == y:
            return True

        d: int = gcd(x, y)
        x, y = x // d, y // d
        if (x + y) % 4 != 0:
            return False
        x, y = min(x, y), max(x, y)
        return does_terminate(y - x, 2 * x)

    for i in range(n_b):
        x: int = bananas[i]
        for j in range(i + 1, n_b):
            y: int = bananas[j]
            if does_terminate(x, y):
                terminating_pairs[x].add(y)
                terminating_pairs[y].add(x)

    paired_with: list[int] = [-1] * n

    def pair(i: int, seen: list[bool]) -> bool:
        for j in range(n):
            if (
                banana_list[i] == banana_list[j]
                or banana_list[j] in terminating_pairs[banana_list[i]]
                or seen[j] == True
            ):
                continue

            seen[j] = True
            if paired_with[j] == -1 or pair(paired_with[j], seen):
                # Able to pair with current or successfully repaired previous
                paired_with[j] = i
                return True

        return False

    result: int = 0
    for i in range(n):
        seen: list[bool] = [False] * n
        if pair(i, seen):
            result += 1

    return n - result + result % 2


if __name__ == "__main__":
    print(solution([1, 1]))
    print(solution([1, 7, 3, 21, 13, 19]))
    print(solution([2, 4]))
    print(solution([5, 3]))
