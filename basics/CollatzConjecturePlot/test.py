import pytest
from . import collatz


@pytest.mark.parametrize('number, expected_lst', (
    (1, [1]),
    (3, [3, 10, 5, 16, 8, 4, 2, 1]),
    (11, [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
    (15, [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
), ids=[str(i + 1) for i in range(4)])
def test_collatz(number, expected_lst):
    result_lst = collatz(number)
    assert result_lst == expected_lst
