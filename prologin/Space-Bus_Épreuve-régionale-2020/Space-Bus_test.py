import main

def test_1():
    assert str(main.main(3,23,[5,2,3],[10,7,13])) == "8"

def test_2():
    assert str(main.main(5,35,[7,7,4,11,5],[15,9,10,20,15])) == "18"

