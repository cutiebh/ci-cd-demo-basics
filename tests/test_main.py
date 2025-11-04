from src.main import add, subtract, multiply, divide

def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10


def test_subtract_function():
    assert subtract(6, 3) == 3
    assert subtract(0, 0) == 0
    assert subtract(5, 5) == 0

#Added by Cutie
def test_multiply_function():
    assert multiply(2, 3) == 6
    assert multiply(0, 0) == 0
    assert multiply(5, 5) == 1
    assert multiply(9, 1) == 9

def test_divide_function():
    assert divide(10, 2) == 5
    assert divide(0, 0) == 0
    assert divide(5, 5) == 1
    assert divide(9, 1) == 9