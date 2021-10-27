
# http://www.france-ioi.org/algo/task.php?idChapter=534&idTask=366

def iter(nb,depth):
    global t
    if depth != 0:
        for i in range(nb):
            iter(i,depth -1)
    else:
        t += nb

nbCard = int(input())
nbRoll = int(input())
t = 0
iter(nbCard,nbRoll - 1)
print(t)
