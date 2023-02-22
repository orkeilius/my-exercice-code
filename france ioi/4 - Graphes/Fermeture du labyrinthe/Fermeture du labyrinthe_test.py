import mock
import main


def test_demo_1():
    inputs = iter(["12 16",
"1 2",
"1 3",
"2 4",
"2 6",
"3 6",
"3 7",
"4 5",
"5 7",
"5 9",
"5 10",
"6 5",
"7 8",
"8 11",
"9 12",
"10 9",
"11 10"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == "1 2 3 4 6 5 7 8 11 10 9 12"

def test_demo_2():
    inputs = iter(["4 4",
"1 2",
"2 3",
"3 4",
"4 1"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == "-1"