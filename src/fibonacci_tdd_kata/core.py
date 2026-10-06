"""Core Fibonacci implementation."""


def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    def fast_doubling(n: int) -> tuple[int, int]:
        if n == 1:
            return (1, 1)

        a, b = fast_doubling(n // 2)

        c = a * (2 * b - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fast_doubling(n)[0]