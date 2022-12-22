def main():
    global maxStabilité, listAccroche,nbStabilisateur
     
    nbAccroche = int(input())
    nbStabilisateur = int(input())
    maxStabilité = int(input())
    listAccroche = sorted(list(map(int,input().split())))
    
    return addStabilisateur(0,listAccroche,1)
    print(addStabilisateur(0,listAccroche,0))
    
def addStabilisateur(stabilité,accroche,recursion):
    if len(accroche) <= 3:
        return stabilité
    
    bestStabilité = stabilité
    for i in range(len(accroche) - 3):
        newStabilité = maxStabilité - ((accroche[i+3] - accroche[i]) ** 2)
        if stabilité + newStabilité > stabilité and recursion <= nbStabilisateur:
            newAccroche = accroche.copy()
            del newAccroche[i:i+4]
            bestStabilité = max(bestStabilité, addStabilisateur(stabilité + newStabilité,newAccroche,recursion+1)) 
    
    return bestStabilité



if __name__ == "__main__":
    main()
