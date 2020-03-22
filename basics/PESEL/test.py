import pytest
from . import pesel_validation, get_age, get_gender, get_birth_date


@pytest.mark.parametrize('pesel_number, expected_validation', (
    ('19301852416', True),
    ('85061855671', True),
    ('85061855672', False),
    ('84061855671', False)
), ids=[str(i + 1) for i in range(4)])
def test_pesel_validation(pesel_number, expected_validation):
    assert pesel_validation(pesel_number) == expected_validation


@pytest.mark.parametrize('pesel_number, expected_gender', (
    ('19301852416', 'Man'),
    ('85061855671', 'Man'),
    ('85061851981', 'Woman'),
    ('85061826901', 'Woman')
), ids=[str(i + 1) for i in range(4)])
def test_get_gender(pesel_number, expected_gender):
    assert get_gender(pesel_number) == expected_gender


@pytest.mark.parametrize('pesel_number, expected_birth_date', (
    ('19301852416', '2019-10-18'),
    ('85061855671', '1985-06-18'),
    ('85120115687', '1985-12-01'),
    ('85121609729', '1985-12-16')
), ids=[str(i + 1) for i in range(4)])
def test_get_birth_date(pesel_number, expected_birth_date):
    assert get_birth_date(pesel_number) == expected_birth_date


@pytest.mark.parametrize('pesel_number, expected_age', (
    # test for date 22.03.2020
    ('19301852416', 0),
    ('85061855671', 34),
    ('01322584986', 18),
    ('18301849123', 1)
), ids=[str(i + 1) for i in range(4)])
def test_get_age(pesel_number, expected_age):
    assert get_age(pesel_number) == expected_age

