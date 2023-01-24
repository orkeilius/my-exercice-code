

def quickSort(liste):
    if len(liste) <= 1:
        return liste
    liste.insert(0,liste.pop(-1)) 
    pivot = 0
    for index, elem in enumerate(liste):
        if elem < liste[pivot]:
            liste.insert(0,liste.pop(index))
            pivot+= 1
    
    
    
    return quickSort(liste[:pivot]) + [liste[pivot]] + quickSort(liste[pivot+1:]) 
    
                

def main():
    # a classic sort() could also
    liste = list(map(int,input().split()))
    return quickSort(liste)[10]

if __name__ == "__main__":
    print(main())