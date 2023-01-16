def main():
    nb = int(input())
    restes = sorted(map(int,input().split()))
    boites = sorted(map(int,input().split()))
    
    reste = 0
    for boite in boites:
        if restes[reste] <= boite:
            reste += 1
                 
    #print(reste)
    return reste

if __name__ == "__main__":
    main()