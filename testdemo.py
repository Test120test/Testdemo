import pytest

def test(a, b):
    return a+b


@pytest.mark.parametrize('a,b,expected_output', [(1,2,3), (2,3,5)])
def test_demo(a,b,expected_output):
    result = test(a,b)
    assert result == expected_output
