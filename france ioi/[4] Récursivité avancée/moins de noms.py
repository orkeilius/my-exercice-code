import math
import sys

# http://www.france-ioi.org/algo/task.php?idChapter=530&iOrder=3

# return all possible name
def enum(depth, string, dict):
    """
    recursive fonction for each caracther
    like "changement de nom" but with is own dictionary to remove word with 2 letter
    """
    for letter in dict:
        if depth == output_size:
            sys.stdout.write(string + letter + "\n")
        else:
            l = dict.copy()
            l.remove(letter)
            enum(depth + 1, string + letter, l)


# get input
letter_size = int(input())
letters = list(input())
output_size = int(input())

# return number of possible nam
t = 1
for i in range(output_size):
    t = t * (letter_size - i)
sys.stdout.write(str(t)+"\n")

# return all possible name
enum(1, "", letters)