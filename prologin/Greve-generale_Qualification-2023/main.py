def main():
    out = []
    nb = int(input())
    cinemas = list(map(int,input().split()))
    out =  [0] * len(cinemas)
    for cinema in range(nb):
        history = []
        position = cinema
        while 1:
            if out[position] != 0:
                out[cinema] = out[position] + len(history)
                break
            elif position in history:
                # if loop find every element in a loop have the same result
                out[cinema] = len(history)
                loopSize = len(history[history.index(position):])
                for elem in history[history.index(position):]:
                    out[elem] = loopSize
                history = history[:history.index(position)] # remove element in the loop
                break
            history.append(position)
            position = cinemas[position]  - 1
        
        # set element result before the loop / precalculated value
        for i in range(len(history)):
            out[history[i]] = out[cinema] - i        
    
    print(" ".join(map(str,out)))
    return " ".join(map(str,out))

if __name__ == "__main__":
    main()
