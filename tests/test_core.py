import pytest

from fibonacci_tdd_kata import fibonacci


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
    ],
)
def test_fibonacci(n: int, expected: int) -> None:
    assert fibonacci(n) == expected


def test_large_values() -> None:
    assert fibonacci(100000) > 1000000
    assert fibonacci(1000000) > fibonacci(999999)