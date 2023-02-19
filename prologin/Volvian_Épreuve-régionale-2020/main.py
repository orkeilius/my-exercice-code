MONEY_VALUE = [200,100,50,20,10,5,2,1]
def main(target):
    total = 0
    for i in MONEY_VALUE:
        total += target // i
        target %= i
    return total
    
if __name__ == "__main__":
    price = int(input())
    money = int(input())
    print(main(money - price))