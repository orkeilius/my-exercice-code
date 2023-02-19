def main(nbPlanets, planets):
    output = []
    shadows = []
    for planet in range(nbPlanets):
        for index, shadow in enumerate(shadows):
            if shadow[0] > planets[planet]:
                output.append(str(shadow[1]+1))
                shadows= [[planets[planet],planet]] +  shadows[index:]
                break
        if len(output) == planet:
            output.append("0")
            shadows= [[planets[planet],planet]]
        


    return " ".join(output)
    
if __name__ == "__main__":
    nbPlanet = int(input())
    planet = list(map(int,input().split()))
    print(main(nbPlanet, planet))