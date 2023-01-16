import mock
import main


def test_demo_1():
    inputs = iter(["9", "2", "10", "3 1 4 5 5 9 2 5 7"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 9


def test_demo_2():
    inputs = iter(["10", 
                   "3", 
                   "100", 
                   "3 1 4 4 5 9 2 6 7 4"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 187

def test_demo_3():
    inputs = iter(["8", 
                   "1", 
                   "25", 
                   "3 2 4 4 5 4 2 6"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 24


def test_full():
    inputs = iter(["12", 
                   "8", 
                   "5", 
                   "8 8 8 8 4 4 4 4 1 1 1 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 15

def test_1():
    inputs = iter(["12", 
                   "8", 
                   "300", 
                   "1 1 1 5 50 60 70 80 200 200 200 204"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 568

def test_2():
    inputs = iter(["12", 
                   "8", 
                   "300", 
                   "1 1 1 50 60 70 80 200 200 200 204"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 284



def test_2():
    inputs = iter(["12", 
                   "8", 
                   "300", 
                   "1 1 1 50 60 70 80 200 200 200 204"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 284

def test_3():
    inputs = iter(["8", 
                   "8", 
                   "300", 
                   "3 3 4 4 4 5 5 6 "]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 600 - 5

def test_4():
    inputs = iter(["8", 
                   "8", 
                   "300", 
                   "3 3 4 4 4 5 5 6 1 1 1 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 900 - 5


def _4():
    inputs = iter(["12", 
                   "8", 
                   "300", 
                   "8 65 84 641 54 13 46 46 9 43 16 45"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 0