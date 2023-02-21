from collections import deque

MOVES = [(-1,0),(1,0),(0,1),(0,-1)]

def main(size,plane):
    plane[1][0] = "*"
    plane[-1][-2] = "*"
    queue = deque([(1,1)])
    while len(queue) != 0:
        pos = queue.pop()
        plane[pos[0]][pos[1]] = "*"

        for move in MOVES:
            nextPos = [pos[0] + move[0], pos[1] + move[1]]
            if plane[nextPos[0]][nextPos[1]] == ".":
                queue.append(nextPos)

    return sum([i.count(".") for i in plane])


if __name__ == "__main__":
    size = list(map(int,input().split()))
    plane = [list(input()) for i in range(size[0])]
    print(main(size,plane))