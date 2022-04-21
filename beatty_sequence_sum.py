from decimal import Decimal, localcontext


def solution(n_s: str):
    n: Decimal = Decimal(n_s)

    with localcontext() as ctx:
        ctx.prec = 101
        r: Decimal = Decimal(2).sqrt()
        s: Decimal = Decimal(2) + Decimal(2).sqrt()

        def solve(n: Decimal | int) -> Decimal | int:
            if n == 0:
                return 0

            N: int = int(n * r)
            m: int = int(Decimal(N) / s)

            return N * (N + 1) // 2 - m * (m + 1) - solve(m)

        return str(int(solve(n)))


if __name__ == "__main__":
    assert solution("5") == "19"
    assert solution("77") == "4208"
