
def main(nbStop,weight :int,peopleAtStop,distanceStop):

    previousTable = [0 for i in range(weight+1)]
    for stopId in range(nbStop):
        table = []
        for w in range(weight+1):
            if w < distanceStop[stopId]:
                table.append(previousTable[w])
            else:
                table.append(max(previousTable[w], previousTable[w - distanceStop[stopId]] + peopleAtStop[stopId]))
        previousTable = list(table.copy())
                
        
    
    return table.pop()


    


if __name__ == "__main__":
    nbStop = int(input())
    peopleAtStop = list(map(int,input().split()))
    distanceStop = list(map(int,input().split()))
    weight = int(input()) 
    print(main(nbStop,weight,peopleAtStop,distanceStop))