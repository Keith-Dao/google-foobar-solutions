def solution(arr: list[int]) -> int:

    n: int = len(arr)
    assert n > 0

    if n == 1:
        return arr[0]

    max_neg: float = float("-inf")
    count_zero = count_neg = 0
    product: int = 1

    for num in arr:
        if num == 0:
            count_zero += 1
            continue

        if num < 0:
            count_neg += 1
            max_neg = max(max_neg, num)

        product *= num

    if count_neg == 1 and count_zero == n - 1:
        return 0

    if count_neg % 2 == 1:
        product = int(product / max_neg)

    return product


if __name__ == "__main__":
    print(solution([0, 2, 2, 0, 2]))
    print(solution([5, 2, -2, -1, 0]))
    print(solution([-1, 0]))
    print(solution([-1]))
