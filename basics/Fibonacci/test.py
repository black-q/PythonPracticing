import pytest
from . import fibonacci


@pytest.mark.parametrize('number_of_digits, expected_list', (
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),
        (4, [0, 1, 1, 2])
), ids=[str(i + 1) for i in range(2)])
def test_fibonacci(number_of_digits, expected_list):
    result_list = fibonacci(number_of_digits)
    assert result_list == expected_list
