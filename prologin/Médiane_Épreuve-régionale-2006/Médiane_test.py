import mock
import main
import random

def test_sort_1():
    inputs = [3,4,0,9,4]
    assert main.quickSort(inputs) == sorted(inputs)

def test_sort_2():
    inputs = [8,5,7,6,0,4]
    assert main.quickSort(inputs) == sorted(inputs)

def test_sort_3():
    inputs = [5,5,5,5,5,5,5,5]
    assert main.quickSort(inputs) == sorted(inputs)

def test_full():
    for i in range(500):
        inputs = [random.randint(-999,999) for loop in range(999)]
        assert main.quickSort(inputs) == sorted(inputs)
        
def test_1():
    inputs = iter(["1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == 11