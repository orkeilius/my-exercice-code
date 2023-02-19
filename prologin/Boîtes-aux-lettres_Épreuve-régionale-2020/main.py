def main(name,names):
    nameSize = len(name)
    best = ("",-1)
    for i in names:
        score = 0
        if nameSize != len(i):
            continue
            
        for letter in range(nameSize):
            if name[letter] == i[letter]:
                score += 1
        
        if best[1] < score:
            best = (i,score)

    return best[0]
    
if __name__ == "__main__":
    name = input()
    nb = int(input())
    names = [input() for i in range(nb)]
    print(main(name, names))