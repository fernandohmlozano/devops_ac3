def func(x):
    return x + 2

def test_positivo():
    assert func(4) == 5

def test_negativo():
    assert func(-2) == -1

def test_zero():
    assert func(0) == 1