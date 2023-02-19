import main

def test_1():
    assert main.main(30) == 2
def test_null():
    assert main.main(0) == 0

def test_2():
    assert main.main(103) == 3