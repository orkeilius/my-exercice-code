import main

def test_1():
    assert main.main(6,5,2,["**.**",
"*.**.",
"**.**",
"*.**.",
"**...",
".*.**"]) == "May the force be with you"

def test_2():
    assert main.main(6,5,1,["*...*",
"*.**.",
"*.**.",
"*....",
"****.",
".**.."]) == "I have a bad feeling about this"

def test_3():
    assert main.main(6,5,2,["**.**",
"*.**.",
".****",
"****.",
"**...",
".*.**"]) == "I have a bad feeling about this"
    
def test_4():
    assert main.main(6,5,1,["*...*",
"*.**.",
"*.**.",
"*....",
"*.**.",
"*****"]) == "I have a bad feeling about this"
