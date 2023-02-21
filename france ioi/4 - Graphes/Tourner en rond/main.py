from collections import deque
import sys

def dfs(graph,pos):
    queue = deque([[pos,[]]])
    graph[pos][0] = False

    while len(queue) != 0:
        pos = queue.pop()

        for link in graph[pos[0]][1:]:
            if link in pos[1]:
                return True
            if not graph[link][0]:
                continue
            graph[link][0] = False
            queue.append((link,pos[1] + [pos[0]]))
        
    return False


    
    

def main():
    nbPoint,nbLinks = list(map(int,sys.stdin.readline().split()))
    graph = [[True] for i in range(nbPoint)]
    for i in range(nbLinks):
        link = list(map(int,sys.stdin.readline().split()))
        graph[link[0] -1].append(link[1] -1)

    for point in range(len(graph)): 
        if graph[point][0]:
            if dfs(graph,point):
                return "OUI"
    return "NON"


if __name__ == "__main__":
    print(main())