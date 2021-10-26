import sys

# http://www.france-ioi.org/algo/task.php?idChapter=529&idTask=411

class square():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

mainSquare = square(*[int(i) for i in sys.stdin.readline().split()])
space = abs(mainSquare.x1 - mainSquare.x2) * abs(mainSquare.y1 - mainSquare.y2)

for loop in range(int(input())):
    squareIter = square(*[int(i) for i in sys.stdin.readline().split()])
    x = max(0, min(squareIter.x2,mainSquare.x2) - max(squareIter.x1,mainSquare.x1))
    y = max(0, min(squareIter.y2,mainSquare.y2) - max(squareIter.y1,mainSquare.y1))
    space -= x * y


print(round(space))
