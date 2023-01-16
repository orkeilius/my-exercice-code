import mock
import main

def test_demo_1():
    inputs = iter(["4",
                   "3 1 4 1"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "3 4 3 3"

def test_demo_2():
    inputs = iter(["5",
                   "2 3 4 5 4"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "5 4 3 2 2"

def test_2_boucle():
    inputs = iter(["6",
                   "2 3 1 5 6 4"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "3 3 3 3 3 3"

def test_666666():
    inputs = iter(["12",
                   "2 3 1 5 6 4 1 2 3 4 5 6"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "3 3 3 3 3 3 4 4 4 4 4 4"

def test_lien():
    inputs = iter(["9",
                   "2 3 4 5 3 5 6 7 8"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "5 4 3 3 3 4 5 6 7" 

def test_lien_reverse():
    inputs = iter(["9",
                   "2 3 4 5 6 7 9 7 8"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "9 8 7 6 5 4 3 3 3"   

def test_tree():
    inputs = iter(["10",
                   "2 3 1 1 4 5 5 2 8 9"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == "3 3 3 4 5 6 6 4 5 6"   