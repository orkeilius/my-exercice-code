import main

def test_1():
    assert main.main("rochard",["martin","bernard",
"thomas",
"petit",
"robert",
"richard",
"durand",
"dubois"]) == "richard"

def test_2():
    assert main.main("rochard",["martin","bernard",
"tho",
"pett",
"robt",
"ricrd",
"durd",
"duis"]) == "bernard"