# http://www.france-ioi.org/algo/task.php?idChapter=530&idTask=517

def check(text):
    opening = "([{<"
    closing = ")]}>"
    state = ""
    for t in text:
        if t in opening:
            state = closing[opening.find(t)] + state
        elif t in closing:
            if state == "":
                print("no")
                return
            elif t == state[0]:
                state = state[1:]
            else:
                print("no")
                return
    
    if state == "":
        print("yes")
    else:
        print("no")
                
if __name__ == "__main__":
    check(input())
