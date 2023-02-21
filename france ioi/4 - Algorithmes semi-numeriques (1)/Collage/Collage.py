
# http://www.france-ioi.org/algo/task.php?idChapter=534&idTask=361

def euclid(a, b):
    """
    euclid's algorithm
    """
    if b == 0:
        return a
    return euclid(b, a % b)


a, b = tuple(map(int, input().split()))
print(round(a * b / euclid(a, b)))
