nbCard = int(input())
nbRoll = int(input())
total = 1

for loop in range(nbCard, nbCard - nbRoll, -1):
    total *= loop
    
print(total)