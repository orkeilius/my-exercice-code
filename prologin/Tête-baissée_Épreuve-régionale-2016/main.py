
_vector = [[0,1],[0,-1],[1,0],[-1,0]]

def main():
    size = int(input())
    graph = []
    visited =[]
    for i in range(size):
        graph.append(input())
        
        if "T" in graph[-1]:
            queue = [((i,graph[-1].index("T")),0)]
        
    while 1:
        current = queue.pop(0)
        visited.append(current[0])
        for move in _vector:
            pos,depth = current
            while 1:
                nextPos = (pos[0] + move[0],pos[1] + move[1])
                if 0 > nextPos[0] or nextPos[0] >= size:
                    break
                elif 0 > nextPos[1] or nextPos[1] >= size:
                    break
                elif graph[nextPos[0]][nextPos[1]] == "X":
                    break
                elif graph[nextPos[0]][nextPos[1]] == "M":
                     return depth
                
                pos = nextPos
                #   visited.append(current[0])
            if not pos in visited: 
                queue.append((pos,depth + 1))

    
if __name__ == "__main__":
    print(main())