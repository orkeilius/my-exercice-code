import mock
import main


def test_demo_perimeter_1():
    assert main.getPerimeter([[1,0],
                              [2,1],
                              [2,-1],
                              [0,0]],99) == [[2,1],[2,-1],[0,0]]

def test_demo_perimeter_2():
    assert main.getPerimeter([[0,2],
                              [1,2],
                              [2,0],
                              [2,1],
                              [0,0]],99) == [[0,2],[1,2],[2,1],[2,0],[0,0]]

def test_demo_perimeter_3():
    assert main.getPerimeter([[-1,0],
                              [1,0],
                              [0,0]],99) == [[-1,0],[1,0]]


def test_error_perimeter_1():
    assert len(main.getPerimeter([[2, 1], [2, -1], [0, 0], [1.2202099292274013, -2.7406363729278023]],3)) == 4

def test_error_perimeter_2():
    assert len(main.getPerimeter([[0, 2], [1, 2], [2, 1], [2, 0], [0, 0], [3.4641016151377544, 2.0000000000000004]],4)) == 4
     

def test_demo_1():
    inputs = iter(["3",
                   "3",
                   "1 0",
                   "2 1",
                   "2 -1"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == 3

def test_demo_2():
    inputs = iter(["4",
                   "4",
                   "0 2",
                   "1 2",
                   "2 0",
                   "2 1"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == 4

def test_demo_3():
    inputs = iter(["1",
                   "2",
                   "-1 0",
                   "1 0"]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == 4