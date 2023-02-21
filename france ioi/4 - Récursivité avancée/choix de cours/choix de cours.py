import sys

# http://www.france-ioi.org/algo/task.php?idChapter=530&idTask=358

# return all possible name
def enum(depth, string, dict):
    """
    recursive fonction for each cours
    """
    for number in range(dict, nb_int - (nb_output - depth - 1)):
        if depth == nb_output:
            print(" ".join(map(str, string + [number])))
        else:
            enum(depth + 1, string + [number], number + 1)


# get input
nb_int, nb_output = map(int, sys.stdin.readline().split())

# return all possible name
enum(1, [], 1)
