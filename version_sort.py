def solution(versions: list[str]) -> list[str]:
    versions.sort(key=lambda v: tuple(map(int, v.split("."))))
    return versions


if __name__ == "__main__":
    versions: list[str] = [
        "2.21.1",
        "2.2",
        "3.21.4",
        "1.0",
        "1.0.0",
        "1.0.1",
        "1",
        "9.6",
        "10.3",
    ]

    print(solution(versions))
