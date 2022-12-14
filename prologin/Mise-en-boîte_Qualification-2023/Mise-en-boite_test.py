import mock
import main

def test_basic():
    inputs = iter(["3",
                   "5 8 1",
                   "1 5 10"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 3

def test_none():
    inputs = iter(["3",
                   "11 11 12",
                   "10 10 9"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 0

def test_full():
    inputs = iter(["4",
                   "1 5 8 77",
                   "8 77 1 5"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 4

def test_full():
    inputs = iter(["3",
                   "1 5 8",
                   "1 5 8"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 3

def test_101():
    inputs = iter(["3",
                   "5 7 8",
                   "5 5 8"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 2

def test_010():
    inputs = iter(["3",
                   "11 11 10",
                   "10 10 9"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 1