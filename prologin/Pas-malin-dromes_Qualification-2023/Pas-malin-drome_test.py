import mock
import main

def test_global_1():
    inputs = iter(["3",
                   "ze44bi",
                   "zebiibe52z",
                   "zebi1bezE"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 1

def test_global_2():
    inputs = iter(["3",
                   "ze47AZbi",
                   "zebiibe2z",
                   "zebi1bez"]).__next__
    
    with mock.patch('builtins.input', inputs):
        assert main.main() == 2

def test_global_3():
    inputs = iter(["1",
                   "e11",]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == 1

def test_global_4():
    inputs = iter(["1",
                   "er1",]).__next__
    with mock.patch('builtins.input', inputs):
        assert main.main() == 0

def test_palindrome_1():
    assert main.palindrome(["a","b","A"]) == False
        
def test_palindrome_1b():
    assert main.palindrome(["a","b","a"]) == True

def test_palindrome_2():
   assert main.palindrome(["a","b","B","a"]) == False 
    
def test_palindrome_b():
    assert main.palindrome(["a","b","b","a"]) == True

def test_palindrome_3():
    assert main.palindrome(["a","b","c","b","A"]) == False
        
def test_palindrome_3b():
    assert main.palindrome(["a","b","c","b","a"]) == True