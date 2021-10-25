# http://www.france-ioi.org/algo/task.php?idChapter=530&idTask=517

def check(text):
    opening = "([{<"
    closing = ")]}>"
    state = ""
    for t in text:

        # add to var in state
        if t in opening:
            state = closing[opening.find(t)] + state
        
        # check if the closing bracket match the opening
        elif t in closing:
            if state == "":
                print("no")
                return
            elif t == state[0]:
                state = state[1:]
            else:
                print("no")
                return
    
    #check if the all bracket are closed
    if state == "":
        print("yes")
    else:
        print("no")
                
if __name__ == "__main__":
    check(input())
