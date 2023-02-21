from collections import deque

MOVES = [(-1,0),(1,0),(0,1),(0,-1)]


def main(size,plane):
    total = 0
    for x in range(size[0]):
        for y in range(size[1]):  
            if plane[x][y] == ".":
                total += 1
                dfs(plane,size,(x,y))
    return total


def dfs(plane,size,pos):
    queue = deque([pos])
    while len(queue) != 0:
        pos = queue.pop()
        plane[pos[0]][pos[1]] = "*"

        for move in MOVES:
            nextPos = [pos[0] + move[0], pos[1] + move[1]]
            if 0 <= nextPos[0] < size[0] and 0 <= nextPos[1] < size[1]:
                if plane[nextPos[0]][nextPos[1]] == ".":
                    queue.append(nextPos)



if __name__ == "__main__":
    size = list(map(int,input().split()))
    plane = [list(input()) for i in range(size[0])]
    print(main(size,plane))