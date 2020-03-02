import pytest
from __init__ import compute_bmi


@pytest.mark.parametrize('weight, height, expected', (
        (80, 1.80, 'normal'),
        (47.8, 1.625, 'underweight'),
        (50.3, 1.625, 'normal'),
        (81.8, 1.803, 'overweight')
), ids=[str(i + 1) for i in range(4)])
def test_compute_bmi(weight, height, expected):
    result = compute_bmi(weight, height)
    assert result == expected
