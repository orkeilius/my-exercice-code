from sys import stdin
from decimal import *


def main():
    nbShow = int(stdin.readline())
    shows = []
    for i in range(nbShow):
        shows.append(tuple(map(int, stdin.readline().split())))

    shows.sort(key=lambda x: x[0],)
    average = Decimal(0)
    best = (0, -1)

    for index, show in enumerate(shows):
        average = ((average * index) + show[1]) / (index + 1)
        if average >= best[1]:
            best = (show[0], average)

    return best[0]


if __name__ == '__main__':

    print(main())
