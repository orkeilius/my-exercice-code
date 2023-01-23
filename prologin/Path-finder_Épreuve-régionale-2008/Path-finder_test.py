import mock
import main

def test_demo_1():
    inputs = iter(["10",
                   "8 8 3 9 8 6 1 3 5 6",
                   "7 5 9 4 8 3 6 9 8 1",
                   "3 5 6 4 2 6 0 7 4 2",
                   "3 8 5 5 0 1 3 6 7 0",
                   "8 0 9 6 2 4 5 3 1 6",
                   "3 6 6 8 0 4 6 5 8 5",
                   "6 9 3 2 8 2 8 3 5 0",
                   "8 1 1 3 6 5 0 1 3 2",
                   "9 0 7 2 7 9 9 3 2 3",
                   "3 7 7 1 3 2 9 2 1 2"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 119





def test_global_1():
    inputs = iter(["3",
                   "1 1 1",
                   "1 1 1",
                   "1 1 1"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 5
