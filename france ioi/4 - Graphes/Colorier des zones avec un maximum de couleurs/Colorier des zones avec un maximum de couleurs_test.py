import main

def test_demo_1():
    plane = ["#####",
"#..#.",
"..##.",
"##.##",
".#..#"]
    assert main.main((5,5),[list(i) for i in plane]) == 4


def test_1():
    plane = ["##########",
".........#",
"###..#.#.#",
"#.###...##",
"#.#...#..#",
"#...####.#",
"#.#.....##",
"#..#..#..#",
"#...#..#.#",
"########.#"]
    assert main.main((10,10),[list(i) for i in plane]) == 1

def test_2():
    plane = ["##########",
".......#.#",
"###..#.#.#",
"#.###...##",
"#.#...#..#",
"#...####.#",
"###.....##",
"#..#..#..#",
"#...#..#.#",
"########.#"]
    assert main.main((10,10),[list(i) for i in plane]) == 3