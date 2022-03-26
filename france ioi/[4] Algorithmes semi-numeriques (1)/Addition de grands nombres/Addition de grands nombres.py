import sys, math

# http://www.france-ioi.org/algo/task.php?idChapter=534&iOrder=8

base, len1, len2 = tuple(map(int, sys.stdin.readline().split()))
number1 = list(map(int, sys.stdin.readline().split()))
number2 = list(map(int, sys.stdin.readline().split()))

# format list to have the same size
number1 = number1[::-1] + [0] * (max(len1, len2) + 2 - len1)
number2 = number2[::-1] + [0] * (max(len1, len2) + 1 - len2)

# calculate the sum
output = []
for nb in range(max(len1, len2) + 1):
    output.append((number1[nb] + number2[nb]) % base)
    if (number1[nb] + number2[nb]) >= base:
        number1[nb + 1] += 1

# remove the zero a the end of output
while output[-1] == 0 and len(output) != 1:
    output.pop(-1)

print(*output[::-1])
