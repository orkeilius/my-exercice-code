from collections import deque

def dfs(graph,pos):
    size = 1
    queue = deque([pos])
    graph[pos][0] = False

    while len(queue) != 0:
        pos = queue.pop()

        for link in graph[pos][1:]:
            if graph[link][0]:
                size+=1
                graph[link][0] = False
                queue.append(link)
    return size

def main():
    nbPoint,nbLinks = list(map(int,input().split()))
    graph = [[True] for i in range(nbPoint)]
    for i in range(nbLinks):
        link = list(map(int,input().split()))
        graph[link[0] -1].append(link[1] -1)
        graph[link[1] -1].append(link[0] -1)
    total = 0
    best = 0
    for point in range(len(graph)): 
        if graph[point][0]:
            total += 1
            best = max(best, dfs(graph,point))
    print(total,best,sep=" ")


if __name__ == "__main__":
    main()