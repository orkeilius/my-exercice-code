
# http://www.france-ioi.org/algo/task.php?idChapter=534&iOrder=4

dimensions = list(map(int, input().split()))

for i in range(min(dimensions), 0, -1):
    if dimensions[0] // i == dimensions[0] / i and dimensions[1] // i == dimensions[1] / i:
        print(i)
        break
