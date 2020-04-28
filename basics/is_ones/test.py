import pytest
from . import is_ones


@pytest.mark.parametrize('n_ones, list_of_ones, result', (
        (3, [0, 1, 1, 1, 0], True),
        (2, [0, 1, 0, 0, 0], False)
), ids=[str(i + 1) for i in range(2)])
def test_is_ones(n_ones, list_of_ones, result):
    assert result == is_ones(n_ones, list_of_ones)
