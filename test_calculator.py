from calculator import add, sub

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(0, 5) == -5
