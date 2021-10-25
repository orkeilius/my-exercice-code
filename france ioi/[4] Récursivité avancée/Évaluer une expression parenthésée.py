import sys

def cal():
    i = ""
    int1,int2,operator = "","",""

    #get data
    while i != "\n" or i != ")":

        i = sys.stdin.read(1)

        #read entry
        if i == "(":
            if operator == "":
                int1 =  cal()
            else:
                int2 = cal()
            continue
        elif i in "+-*/%":
            operator = i
        elif i in "1234567890":
            if operator == "":
                int1 += i
            else:
                int2 += i
        else:
           break
      
    #calcul the output
    if operator == "" or int2 == "":
        return int1
    elif operator == "+":
        return int(int1) + int(int2)
    elif operator == "-":
        return int(int1) - int(int2)
    elif operator == "*":
        return int(int1) * int(int2)
    elif operator == "/":
        return int(int1) / int(int2)
    elif operator == "%":
        return int(int1) % int(int2)
        

print(cal())