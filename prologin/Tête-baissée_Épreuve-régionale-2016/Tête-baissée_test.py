import mock
import main

def test_demo_1():
    inputs = iter(["10", 
                   "..........", 
                   "..........", 
                   "..........", 
                   "...T......",
                   "X......X..",
                   "....M.....",
                   "X.........",
                   "..........",
                   "..........",
                   "........X."]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 3

def test_demo_2():
    inputs = iter(["4", 
                   "....", 
                   "....", 
                   "T.MX", 
                   "...."]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 0

def test_1():
    inputs = iter(["4", 
                   "....", 
                   "..X.", 
                   "T.X.", 
                   "..XM"]).__next__
    with mock.patch("builtins.input", inputs):
        assert main.main() == 2