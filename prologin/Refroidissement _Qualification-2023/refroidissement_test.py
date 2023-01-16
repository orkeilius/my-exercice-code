import mock
import main

def test_demo_1():
    inputs = iter(["4",
                   "6",
                   "5",
                   "1",
                   "2",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 4

def test_demo_1_reverse():
    inputs = iter(["4",
                   "6",
                   "5",
                   "2",
                   "1",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == -1

def test_demo_2():
    inputs = iter(["4",
                   "6",
                   "1",
                   "1",
                   "2",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 1

def test_demo_2_reverse():
    inputs = iter(["4",
                   "6",
                   "1",
                   "2",
                   "1",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == -1


def test_demo_3():
    inputs = iter(["4",
                   "6",
                   "1",
                   "2",
                   "1",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == -1
def test_demo_3_reverse():
    inputs = iter(["4",
                   "6",
                   "1",
                   "1",
                   "2",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 1

def test_demo_4():
    inputs = iter(["4",
                   "6",
                   "7",
                   "1",
                   "2",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 5

def test_demo_4_reverse():
    inputs = iter(["4",
                   "6",
                   "7",
                   "2",
                   "1",
                   "1 3 1",
                   "1 2 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == -1

def test_1():
    inputs = iter(["4",
                   "6",
                   "1",
                   "1",
                   "2",
                   "1 3 1",
                   "1 4 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 2

def test_2():
    inputs = iter(["4",
                   "6",
                   "7",
                   "1",
                   "2",
                   "1 3 1",
                   "1 4 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 2 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 5
        
def test_voidLoop():
    inputs = iter(["4",
                   "6",
                   "7",
                   "1",
                   "2",
                   "1 3 1",
                   "1 4 1",
                   "3 3 2",
                   "3 4 1",
                   "4 1 1",
                   "4 3 1"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == -1