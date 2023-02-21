import mock
import main


def test_demo_1():
    inputs = iter(["6",
                   "900 250",
                   "600 200",
                   "3600 50",
                   "800 400",
                   "7200 20",
                   "2400 360"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == 2400


def test_1():
    inputs = iter(["6",
                   "900 250",
                   "600 200",
                   "3600 50",
                   "800 400",
                   "7200 20",
                   "2400 36"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == 800


def test_2():
    inputs = iter(["6",
                   "900 250",
                   "600 200",
                   "3600 50",
                   "800 400",
                   "7200 2000",
                   "2400 0"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == 7200


def test_3():
    inputs = iter(["4",
                   "1 200",
                   "2 200",
                   "3 200",
                   "4 0"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == 3


def test_4():
    inputs = iter(["4",
                   "1 100",
                   "2 200",
                   "3 100",
                   "4 200"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == 4


def test_5():
    inputs = iter(["4",
                   "1 100",
                   "2 200",
                   "3 99",
                   "4 200"]).__next__
    with mock.patch("sys.stdin.readline", inputs):
        assert main.main() == 2
