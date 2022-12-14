import mock
import main

def test_all():
    inputs = iter(["a",
                   "b",
                   "c",
                   "d",
                   "e",
                   "f",
                   "_a",
                   "_b",
                   "_c",
                   "_d",
                   "_e",
                   "_f",]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 6

def test_none():
    inputs = iter(["a",
                   "b",
                   "c",
                   "d",
                   "e",
                   "f",
                   "a",
                   "b",
                   "c",
                   "d",
                   "e",
                   "f",]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 0

def test_suffle():
    inputs = iter(["aa",
                   "b",
                   "c",
                   "d",
                   "e",
                   "f",
                   "a",
                   "bb",
                   "c",
                   "d",
                   "e",
                   "f",]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 2

def test_memeAdore():
    inputs = iter(["a",
                   "b",
                   "a",
                   "d",
                   "e",
                   "f",
                   "_a",
                   "_b",
                   "_c",
                   "_d",
                   "_e",
                   "_f",]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 5

def test_memeDeteste():
    inputs = iter(["a",
                   "b",
                   "c",
                   "d",
                   "e",
                   "f",
                   "a",
                   "a",
                   "_c",
                   "_d",
                   "_e",
                   "_f",]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 5