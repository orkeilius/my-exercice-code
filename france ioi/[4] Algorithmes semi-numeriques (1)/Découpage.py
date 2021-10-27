
# http://www.france-ioi.org/algo/task.php?idChapter=534&iOrder=4

dimensions = list(map(int, input().split()))

# implantation of euclid's algorithm
def euclid(a, b):
    if b == 0 :
        return a
    return euclid(b, a % b)

print(euclid(*dimensions))