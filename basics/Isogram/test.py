import pytest
from . import is_isogram


@pytest.mark.parametrize('word, expected_result', (
    ('Damian', False),
    ('Brzeczyszczykiewicz', False),
    ('Skrzynia', True),
    ('', True),
), ids=[str(i + 1) for i in range(4)])
def test_is_isogram(word, expected_result):
    assert is_isogram(word) == expected_result
