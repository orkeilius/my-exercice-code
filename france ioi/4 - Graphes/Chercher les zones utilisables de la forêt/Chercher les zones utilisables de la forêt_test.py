import mock
import main


def test_demo_1():
    inputs = iter(["12 14",
"1 2 12",
"1 3 10",
"2 4 11",
"2 5 13",
"3 5 12",
"3 7 13",
"4 6 9",
"5 6 7",
"6 7 15",
"8 9 12",
"8 10 10",
"9 10 10",
"10 11 9",
"11 12 10"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == (2,7)

