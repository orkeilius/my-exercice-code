from sys import stdin
import time

# http://www.france-ioi.org/algo/task.php?idChapter=532&idTask=1800


def main():
    nbDay, nbGroup = map(int, stdin.readline().split())
    days = tuple(map(int, stdin.readline().split()))
    dayContent = [0 for i in range(nbGroup)]
    start = 0
    best = 100000
    nbDifferent = 0

    for end in range(0, nbDay):
        dayContent[days[end] - 1] += 1

        if dayContent[days[end] - 1] == 1:
            nbDifferent += 1
            if nbDifferent == nbGroup:
                while dayContent[days[start - 1] - 1] != 0:
                    dayContent[days[start] - 1] -= 1
                    start += 1
                best = min(best, end - (start - 1))
                nbDifferent -= 1

    print(best + 1)


main()
