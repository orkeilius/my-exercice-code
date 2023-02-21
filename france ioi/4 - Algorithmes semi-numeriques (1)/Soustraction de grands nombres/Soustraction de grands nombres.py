import sys, math

# http://www.france-ioi.org/algo/task.php?idChapter=534&iOrder=8


def clean(a):
    """remove the zero a the end of list"""
    while a[-1] == 0 and len(a) != 1:
        a.pop(-1)
    return a


def subtract(originalNb1, originalNb2):
    """
    return subtracted number
    Args:
        nb1 ([int]): first number
        nb2 ([int]): number to subtract

    Returns:
        list: subtract
    """
    nb1, nb2 = originalNb1.copy(), originalNb2.copy()
    out = []
    for nb in range(max(len1, len2) + 1):
        i = nb1[nb] - nb2[nb]
        if i < 0:
            nb2[nb + 1] += 1
            i += base
        out.append(i)

    # clean output
    # check if the output is not a negative number and recalculate if
    if nb2[len(nb2) - 1] == 1:
        out = subtract(originalNb2, originalNb1)
        clean(out)
        out.append("-")
    else:
        clean(out)

    return out


# get input
base, len1, len2 = tuple(map(int, sys.stdin.readline().split()))
number1 = list(map(int, sys.stdin.readline().split()))
number2 = list(map(int, sys.stdin.readline().split()))

# format list to have the same size
number1 = number1[::-1] + [0] * (max(len1, len2) + 1 - len1)
number2 = number2[::-1] + [0] * (max(len1, len2) + 2 - len2)

output = subtract(number1, number2)

print(*output[::-1])
