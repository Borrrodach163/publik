import pytest
from app.triangle import is_triangle

@pytest.mark.parametrize("a", [1, 25, 0, 99, 3])
@pytest.mark.parametrize("b", [0, 15, 4])
@pytest.mark.parametrize("c", [-1, 30, 0, 5])
@pytest.mark.xfail(raises = AssertionError)
def test_is_triangle(a,b,c):
    is_triangle(a,b,c)
    assert is_triangle(a,b,c) is True