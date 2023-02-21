import mock
import main


def test_demo_1():
    inputs = iter(["12 16",
"1 2",
"1 3",
"2 4",
"2 5",
"3 5",
"3 7",
"4 6",
"5 6",
"6 10",
"6 11",
"7 6",
"8 7",
"9 8",
"10 9",
"10 11",
"11 12"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == "OUI"

