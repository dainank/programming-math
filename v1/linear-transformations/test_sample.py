from hypothesis import given, strategies as st
from hypothesis.strategies import text


@given(st.integers(), st.integers(), st.integers(), st.integers())
def test_ints_are_commutative(x1, y1, x2, y2):
    assert x1 * 2 + x2 * 2 == 2 * (x1 + x2)
    assert y1 * 2 + y2 * 2 == 2 * (y1 + y2)
    assert x1 ** 2 + x2 ** 2 == (x1 + x2) ** 2
    assert y1 ** 2 + y2 ** 2 == (y1 + y2) ** 2
