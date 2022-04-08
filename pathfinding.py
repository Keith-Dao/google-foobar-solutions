from collections import deque


def solution(map: list[list[int]]) -> int:

    m, n = len(map), len(map[0])
    if m == 1 and n == 1:
        return 1

    queue: deque = deque([(0, 0, map[0][0] == 1)])
    visited = set(queue)
    steps = 0

    while queue:
        steps += 1
        for _ in range(len(queue)):
            r, c, broken = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < m or not 0 <= nc < n:
                    # Out of bounds
                    continue

                if map[nr][nc] == 1 and broken:
                    # Cannot break wall
                    continue

                if nr == m - 1 and nc == n - 1:
                    return steps + 1

                next_state: tuple[int, int, bool] = (
                    nr,
                    nc,
                    broken or map[nr][nc] == 1,
                )
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
    return -1


if __name__ == "__main__":
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
