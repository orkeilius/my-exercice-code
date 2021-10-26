from math import sqrt

# http://www.france-ioi.org/algo/task.php?idChapter=529&idTask=412
# math.dist is looks disable

def Sqr(a):
    # equals "** 2" to make the formula clearer 
    return a*a

def dist(x1, y1, x2, y2):
    # replace math.dist
    return sqrt(Sqr(y2-y1)+Sqr(x2-x1))


x1, y1 = map(int, input().split())
bestDistance = (9999999, 0, 0)

for i in range(int(input())):
    x2, y2 = tuple(map(int, input().split()))
    if dist(x1, y1, x2, y2) < bestDistance[0]:
        bestDistance = (dist(x1, y1, x2, y2), x2, y2)

print(*bestDistance[1:])
