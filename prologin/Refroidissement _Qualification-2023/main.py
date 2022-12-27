def main():
    nbNode = int(input())
    nbLink = int(input())
    targetTemp = int(input())
    startNode = int(input()) - 1
    endNode = int(input()) - 1
    
    nodes = [[] for i in range(nbNode)]
    nodesPreviousTemp = [0] * nbNode
    for i in range(nbLink):
        link = list(map(int,input().split()))
        nodes[link[0]-1].append([link[1]-1,link[2]])
    
    queue = [[startNode,0,0]] # A pointer contain his position, temp, and pipe
    while 1:
        if queue == []:
            print(-1)
            return -1
        pointer = queue.pop(0)
        if pointer[0] == endNode and pointer[1] >= targetTemp:
            print(pointer[2])
            return pointer[2]
        else:
            for link in nodes[pointer[0]]:
                nextTemp = link[1] + pointer[1]
                if nextTemp > nodesPreviousTemp[link[0]] and nodesPreviousTemp[link[0]] < targetTemp:
                    nodesPreviousTemp[pointer[0]] = pointer[1]
                    queue.append([link[0],nextTemp,pointer[2]+1])

if __name__ == "__main__": 
    main()