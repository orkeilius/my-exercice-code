import main

def test_1():
    assert main.main(3,[2,2,2]) == "0 0 0"

def test_2():
    assert main.main(5,[5, 2, 4, 6, 1]) == "0 1 1 0 4"

def test_3():
    assert main.main(5,[10, 5, 7, 1, 1]) == "0 1 1 3 3"