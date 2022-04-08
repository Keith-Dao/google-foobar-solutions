import math
from typing import Callable


def solution(
    dimensions: list[int],
    your_position: list[int],
    trainer_position: list[int],
    distance: int,
) -> int:

    x, y = your_position
    tx, ty = trainer_position
    width, height = dimensions

    # Get the number of mirrored rooms in the first quadrant
    max_x: int = x + distance
    max_y: int = y + distance
    x_rooms: int = math.ceil(max_x / width)
    y_rooms: int = math.ceil(max_y / height)

    your_positions: set[tuple[int, int]] = set()
    trainer_positions: set[tuple[int, int]] = set()

    def add_position(
        positions: set[tuple[int, int]], x: int, y: int, mx: int, my: int
    ) -> None:
        sign: Callable[[int], int] = (
            lambda a: -(a % 2) * 2 + 1
        )  # Reflect along odd axes
        positions.add(
            (
                sign(mx) * x + (mx + mx % 2) * width,
                sign(my) * y + (my + my % 2) * height,
            )
        )

    # Add all the mirrored rooms
    for mx in range(x_rooms):
        for my in range(y_rooms):
            add_position(your_positions, x, y, mx, my)
            add_position(trainer_positions, tx, ty, mx, my)

    def reflect(positions: set[tuple[int, int]]) -> None:
        # Mirror the positions into four quadrants
        new_positions = set()
        for x1, y1 in positions:
            new_positions.add((x1, y1))
            new_positions.add((x1, -y1))
            new_positions.add((-x1, y1))
            new_positions.add((-x1, -y1))
        positions.update(new_positions)

    # Mirror positions into each quadrant
    reflect(your_positions)
    reflect(trainer_positions)

    def get_distance(x1: int, y1: int) -> int:
        return (dx := x - x1) * dx + (dy := y - y1) * dy

    def filter_out_of_range(positions: set[tuple[int, int]]) -> None:
        positions.difference_update(
            {p for p in positions if get_distance(*p) > distance * distance}
        )

    # Remove all positions that cannot be reached
    filter_out_of_range(your_positions)
    filter_out_of_range(trainer_positions)

    def is_smaller(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
        return get_distance(*p1) < get_distance(*p2)

    # Find all angles that will hit you
    seen: dict[float, tuple[int, int]] = {}
    for x1, y1 in your_positions:
        if x1 == x and y1 == y:
            continue

        angle: float = math.atan2(y1 - y, x1 - x)
        if angle not in seen or is_smaller((x1, y1), seen[angle]):
            seen[angle] = (x1, y1)

    # Remove possible final destinations if the ray is blocked
    to_remove: set[tuple[int, int]] = set()
    for x1, y1 in trainer_positions:
        angle: float = math.atan2(y1 - y, x1 - x)
        if angle in seen:
            if is_smaller((x1, y1), seen[angle]):
                # Current coordinate is closer
                to_remove.add(seen[angle])
            else:
                # Old coordinate was closer i.e. blocked
                to_remove.add((x1, y1))
                continue
        seen[angle] = (x1, y1)
    trainer_positions.difference_update(to_remove)

    return len(trainer_positions)


if __name__ == "__main__":

    assert solution([3, 2], [1, 1], [2, 1], 4) == 7
    assert solution([300, 275], [150, 150], [185, 100], 500) == 9
