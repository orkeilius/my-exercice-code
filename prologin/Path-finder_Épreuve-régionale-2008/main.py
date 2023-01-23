
def main():
    size = int(input())
    
    graph = []
    for i in range(size):
        graph.append(list(map(int,input().split())))
    
    for x in range(size):
        for y in range(size):
            if(x >= size or y >= size):
                continue

            previousNb = []
            if x -1 >= 0:
                previousNb.append( graph[x - 1][y] )
            if y -1 >= 0:
                previousNb.append( graph[x][y - 1] )

            if previousNb != []:
                graph[x][y] += max(previousNb)
        
        
    
    return graph[size -1][size -1]



if __name__ == "__main__":
    print(main())
