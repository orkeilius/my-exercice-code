import sys
  
#using dict( instead of list/deque is faster

def main():
    nbPoint,nbLinks = list(map(int,sys.stdin.readline().split()))
    graph = {i:[] for i in range(nbPoint)}
    for i in range(nbLinks):
        link = list(map(int,sys.stdin.readline().split()))
        graph[link[1] -1].append(link[0] -1)
    
    output = []
    while len(graph) != 0:
        found = False
        for point in graph.keys():
            if len(graph[point]) == 0 :
                output.append(str(point + 1))
                for subPoint in graph.keys():
                    if point in graph[subPoint]:
                        graph[subPoint].remove(point)
                
                found = True
                graph.pop(point)
                break
        
        if not found:
            return "-1"
        
    return " ".join(output)


    


if __name__ == "__main__":
    print(main())