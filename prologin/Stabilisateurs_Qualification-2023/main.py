from random import randint
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

# not optimized
def addStabilisateur2(stabilité,accroche,recursion):
    if len(accroche) <= 3:
        return stabilité
    
    bestStabilité = stabilité
    for i1 in range(0,len(accroche) - 3):
        for i2 in range(i1 + 1,len(accroche) - 2):
            for i3 in range(i2 + 1,len(accroche) - 1):
                for i4 in range(i3 + 1,len(accroche)):
                    newStabilité = maxStabilité - ((accroche[i4] - accroche[i1]) ** 2)
                    if stabilité + newStabilité > stabilité and recursion <= nbStabilisateur:
                        newAccroche = accroche.copy()
                        newAccroche.pop(i4)
                        newAccroche.pop(i3)
                        newAccroche.pop(i2)
                        newAccroche.pop(i1)
                        bestStabilité = max(bestStabilité, addStabilisateur2(stabilité + newStabilité,newAccroche,recursion+1)) 
    
    return bestStabilité

if __name__ == "__main__":
    main()

