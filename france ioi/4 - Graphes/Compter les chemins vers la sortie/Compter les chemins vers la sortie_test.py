import main

def test_demo_1():
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
    assert main.main((10,10),[list(i) for i in plane]) == 4