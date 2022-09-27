import sys
import copy


width, height = [int(i) for i in input().split()]


#get golf's map info and balls
golfMap = []
balls = [] # [[posY posX,nbShot]]
for y in range(height):
    golfMap.append(input())
    for x in range(width):
        if golfMap[y][x] in "123456789":
            balls.append([y,x,int(golfMap[y][x])])
            
            
#calculate every paths 
paths = []
def findMove(ball,moveHistory,lastDirection):
    global paths
    #i should use match/case but is not supported on condingame yet
    if not (0 <= ball[0] < height and 0 <= ball[1] < width):
        return
    if golfMap[ball[0]][ball[1]] == "H":
        paths[-1].append(moveHistory)

    if ball[2] == 0:
        return
    elif golfMap[ball[0]][ball[1]] == "." or lastDirection == 0:
        if lastDirection != 1: #left
            findMove([ball[0],ball[1] - ball[2],ball[2] - 1],moveHistory + [[0,-1,ball[2]]],3)
        if lastDirection != 2: #up
            findMove([ball[0]- ball[2],ball[1],ball[2] - 1],moveHistory + [[-1,0,ball[2]]],4)
        if lastDirection != 3: #right
            findMove([ball[0],ball[1] + ball[2],ball[2] - 1],moveHistory + [[0,1,ball[2]]],1)
        if lastDirection != 4: #down
            findMove([ball[0] + ball[2],ball[1],ball[2] - 1],moveHistory + [[1,0,ball[2]]],2)
    return
   
for ball in balls:
    paths.append([])
    findMove(ball,[[ball[0],ball[1]]],0)


#apply path | if not path working path the previous path is canceled
#ball with few path will be apply first a
def applyPath(path,moveMap):
    #apply path with the index of the ball. -1 définitif pat
    pos = path[0].copy()
    for move in path[1:]:
        for i in range(move[2]):
            if not moveMap[pos[0]][pos[1]] in ".H":
                return -1
            if move[0] == 1:
                moveMap[pos[0]][pos[1]] = "v"
            elif move[0] == -1:
                moveMap[pos[0]][pos[1]] = "^"
            elif move[1] == 1:
                moveMap[pos[0]][pos[1]] = ">"
            else:
                moveMap[pos[0]][pos[1]] = "<"
            pos[1] += move[1]
            pos[0] += move[0]
        if moveMap[pos[0]][pos[1]] != ".":
                return -1
    moveMap[pos[0]][pos[1]] = "U"
    return moveMap

def bruteforcePath(pathIndex, moveMap):
    global solved
    if moveMap == -1:
        return False
    if pathIndex == len(paths) :
        solved = moveMap
        return True
    for path in paths[pathIndex]:
        if bruteforcePath(pathIndex + 1,applyPath(path,copy.deepcopy(moveMap))):
            return True

solved = [] 
#sort paths by number of path to have less try
paths.sort(key=lambda x : len(x))
liste = [(["."] * width) for i in range(height)]

bruteforcePath(0, liste)
[print("".join(i).replace("U",".")) for i in solved]