from decimal import *
import math


def main():
    radius = int(input()) 
    nbNode = int(input())
    nodes = [[0,0]]
    for i in range(nbNode):
        nodes.append(list(map(int,input().split())))
    
    nodes = getPerimeter(nodes,radius) #remove useless node
    
    best = len(nodes)
    for angle in range(360): #naive implementation by try 360 degrees
        x = Decimal(radius * math.sin(math.pi * 2 * angle / 360))
        y = Decimal(radius * math.cos(math.pi * 2 * angle / 360))
        newNode = nodes.copy()
        newNode.append([x,y])
        best = min(best, len(getPerimeter(newNode,radius)))
    return best
    

def getPerimeter(nodes,radius):
    perimeter = [max(nodes,key=lambda x:x[1])] #get the highest point because he is always part of the perimeter
    perimeter.insert(0,[radius*-1,perimeter[0][1]]) 
    while 1:
        best = ([],-1)
        
        B = Decimal(math.dist(perimeter[-2],perimeter[-1]))
        
        for node in nodes :
            if node == perimeter[-1]:
                continue
            A = Decimal(math.dist(perimeter[-2],node))
            C = Decimal(math.dist(node,perimeter[-1]))
            s1 = ((C**2) + (B**2) - (A**2))
            s2 = (2 * B * C)
            angle = Decimal(math.acos(max(min(s1 / s2,1),0)))  
            if best[1] < angle:
                best = [node,angle]
        
        # remove current point if he on a straight line
        if round(best[1],5) == round(math.pi /2,5):
            perimeter.pop(-1)
        
        if best[0]  == perimeter[1]:
            return perimeter[1:]
        
        perimeter.append(best[0])
        nodes.remove(best[0])
            
    
if __name__ == "__main__":
    main()