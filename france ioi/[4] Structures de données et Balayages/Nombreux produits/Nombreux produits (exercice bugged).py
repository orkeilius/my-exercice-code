from collections import deque
from sys import stdin

# http://www.france-ioi.org/algo/task.php?idChapter=532&iOrder=2


def main():
    input = stdin.readline
    # input
    nbDispenser = int(stdin.readline())
    nbOperation = int(stdin.readline())

    # make Dispenser var
    # first value is ignored because dispenser id start at 1
    dispensers = [deque() for i in range(nbOperation + 1)]

    # read change
    for operation in range(nbOperation):
        name, number, params = map(int, input().split(" "))
        # remove operation
        if number < 0:
            while number < 0:
                numberStored, date = dispensers[name].popleft()
                number += numberStored
            if number > 0:
                dispensers[name].appendleft((number, date))

        # add operation
        else:
            dispensers[name].append((number, params))

    # print output
    for dispenser in range(1, nbDispenser + 1):
        if len(dispensers[dispenser]) == 0:
            print("0")
        else:
            print(min([i[1] for i in dispensers[dispenser]]))


main()
