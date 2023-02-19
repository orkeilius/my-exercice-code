import main

def test_1():
    assert main.main(18,4,[5,12,14,15]) == 0

def test_2():
    assert main.main(16,12,[5,12,14,15]) == -1

def test_3():
    assert main.main(18,18,[5,12,14,15]) == 1