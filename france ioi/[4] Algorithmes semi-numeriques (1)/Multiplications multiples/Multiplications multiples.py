import sys

# http://www.france-ioi.org/algo/task.php?idChapter=534&iOrder=7

t = 1
for i in range(int(sys.stdin.readline())):
    t = str(int(t * int(sys.stdin.readline())))
    t = int(t[len(t) - 6:])
sys.stdout.write("{:04d}".format(t))