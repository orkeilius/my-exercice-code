import sys

# http://www.france-ioi.org/algo/task.php?idChapter=530&idTask=358

# return all possible name
def enum(depth,string):
    for letter in letters:
        if depth == output_size:
             sys.stdout.write(string + letter + "\n")
        else:
            enum(depth + 1, string + letter)



# get input
letter_size = int(input())
letters = list(input())
letters.sort()
output_size = int(input())

# return number of possible name
sys.stdout.write(str(letter_size ** output_size)+"\n")

# return all possible name
enum(1,"")
