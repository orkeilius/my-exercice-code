
def main(target,move,holes):
    if move == target:
        return 1

    for hole in holes:
        if move == hole:
            return -1
    
    return 0

if __name__ == "__main__":
    target = int(input())
    move = int(input())
    nbHole = int(input())
    holes = list(map(int,input().split()))
    print(main(target,move,holes))