def solution(l):
    if (n := len(l)) < 3:
        return 0

    divides: list[list[int]] = [[] for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                divides[i].append(j)

    triples: int = 0
    for i in range(n - 2):
        for j in divides[i]:
            triples += len(divides[j])

    return triples


if __name__ == "__main__":
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))
