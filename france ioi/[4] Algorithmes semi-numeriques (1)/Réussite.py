import sys

# http://www.france-ioi.org/algo/task.php?idChapter=534&iOrder=6
# i use sys here because the output must be very fast
def primes(n):
    """ 
    this prime finders have been found online (not mine)
    credit : https://stackoverflow.com/a/3035188/16254121
    Returns  a list of primes < n 
    """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



nb = int(sys.stdin.readline())

# edge case for 0 and 1
for i in range(min(2, nb)):
    sys.stdout.write(str(i)+"\n")

sys.stdout.write("\n".join(map(str,primes(nb + 1))))