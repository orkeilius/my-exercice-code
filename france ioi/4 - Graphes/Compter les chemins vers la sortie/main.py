import copy
MOVES = [(-1,0),(1,0),(0,1),(0,-1)]

def main(size,plane):
    plane[1][0] = "*"
    plane[-1][-2] = "@"
    return dfs(size,plane,(1,1))

def dfs(size,plane,pos):
    total = 0
    plane[pos[0]][pos[1]] = "*"

    for move in MOVES:
        nextPos = [pos[0] + move[0], pos[1] + move[1]]
        if plane[nextPos[0]][nextPos[1]] == "@":
            total += 1 
        if plane[nextPos[0]][nextPos[1]] == ".":
            total += dfs(size,plane,nextPos)
    plane[pos[0]][pos[1]] = "."
    return total


    

if __name__ == "__main__":
    size = list(map(int,input().split()))
    plane = [list(input()) for i in range(size[0])]
    print(main(size,plane))