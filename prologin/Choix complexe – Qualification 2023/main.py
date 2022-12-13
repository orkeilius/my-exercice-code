def main():
    films = []
    for loop in range(6):
        i = input()
        if not i in films: 
            films.append(i)
    for loop in range(6):
        try:
            films.remove(input())
        except ValueError:
            pass
    print(len(films))
    #return len(films)
if __name__ == "__main__":
    main()