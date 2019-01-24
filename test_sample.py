import pytest

from sample import add


@pytest.mark.parametrize('test_input, expected', [
    ((1, 2), 3),
    ((-1, 2), 1),
    ((1, -2), -1),
    ((0, 0), 0),
    ((-10, -10), -20)
])
def test_add(test_input, expected):
    assert add(*test_input) == expected
