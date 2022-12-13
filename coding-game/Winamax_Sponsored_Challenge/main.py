import sys
import math


width, height = [int(i) for i in input().split()]
golfMap = []
balls = [] # [[posX posY,nbShot]]

#get golfmap info and balls
for y in range(height):
    golfMap.append(input())
    for x in range(width):
        if golfMap[y][x] in "123456789":
            balls.append([x,y,int(golfMap[y][x])])

[print(i,file=sys.stderr) for i in balls]
#calculate every paths 
paths = []

def nextMove(ball,moveHistory,lastDirection):
    global paths
    #i should use match/case but is not supported on condingame yet
    try:
        if golfMap[ball[0]][ball[1]] == "H":
            paths[-1].append(moveHistory)
    except IndexError:
        return

    if ball[2] == 0:
        return
    elif golfMap[ball[0]][ball[1]] == "." or lastDirection == 0:
        if lastDirection != 1: #left
            nextMove([ball[0] + ball[2],ball[1],ball[2]],moveHistory + [[1,0,ball[2]]],3)
        if lastDirection != 2: #up
            nextMove([ball[0],ball[1] - ball[2],ball[2]],moveHistory + [[0,-1,ball[2]]],4)
        if lastDirection != 3: #right
            nextMove([ball[0] - ball[2],ball[1],ball[2]],moveHistory + [[-1,0,ball[2]]],1)
        if lastDirection != 4: #down
            nextMove([ball[0],ball[1] + ball[2],ball[2]],moveHistory + [[0,1,ball[2]]],2)
    return
   
for ball in balls:
    paths.append([])
    nextMove(ball,[[ball[0],ball[1]]],0)
 
   
#apply path | ball with few path will be apply first
moveMap = []
[moveMap.append(["."] * width) for i in range(height)]

def validPatch(path):
    #check if the path still valid
    pos = path[0]
    for move in path[1:]:
        for i in range(move[1]):
            pos[0] += move[0][0]
            pos[1] += move[0][1]
            if golfMap[pos[0]][pos[1]] in "v<>^":
                return False
    return True

def applyPath(path):
    #check if the path still valid
    pos = path[0]
    for move in path[1:]:
        print(path,file=sys.stderr)
        for i in range(move[2]):
            if move[0] == 1:
                moveMap[pos[0]][pos[1]] = ">"
            elif move[0] == -1:
                moveMap[pos[0]][pos[1]] = "<"
            elif move[1] == 1:
                moveMap[pos[0]][pos[1]] = "^"
            elif move[1] == -1:
                moveMap[pos[0]][pos[1]] = "v"
            pos[0] += move[0]
            pos[1] += move[1]

while len(paths) !=0:
    paths.sort(key=lambda x : len(x))
    
    applyPath(paths[0][0])
    paths.pop(0)
        
    [print(i,file=sys.stderr) for i in moveMap] 
    #recheck path 
    for ball in paths:
        for path in ball:
            if not validPatch(path):
                ball.remove(path)
    

        

[print(i,file=sys.stderr) for i in moveMap]