from collections import deque

MOVES = (-1,0,1)
def main(width, largeur,pos,plane):
    posList = deque([pos])
    for y in range(1,width):
        nextPos = deque([])
        for i in range(len(posList)):
            pos = posList.popleft()
            for move in MOVES:
                if pos + move <= -1 or pos + move >= largeur:
                    continue
                if plane[y][pos + move] == ".":
                    nextPos.append(pos + move)
        
        if len(nextPos) == 0:
            return "I have a bad feeling about this" 
        
        posList = nextPos
    
    return "May the force be with you"

   
    
if __name__ == "__main__":
    height = int(input())
    width = int(input())
    pos = int(input()) 
    plane = [input() for i in range(height)]
    print(main(height, width,pos,plane))