# http://www.france-ioi.org/algo/task.php?idChapter=530&iOrder=7

text = input()
ident = ""

for t in text:
    if t == "}":
        ident = ident[:len(ident) - 3]
    print(ident + t)
    if t == "{":
        ident += "   "