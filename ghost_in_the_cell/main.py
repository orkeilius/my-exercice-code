import sys
import math
import time

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
factory_link = []

#get all link
for i in range(link_count):
    link = [int(j) for j in input().split()]
    factory_link.append(link.copy())
    factory_link.append([link[1],link[0],link[2]])

while True:
    start = time.time()

    # collect data
    factory_data = [[] for factory in range(factory_count)]
    troop_data = []
    entity_count = int(input())  
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        
        #factory entity
        if entity_type == "FACTORY":
            factory_data[entity_id] = [int(inputs[2]),int(inputs[3]),int(inputs[4])]
        
        #troop entity
        elif entity_type == "TROOP":
            if int(inputs[2]) == 1:
                troop_data.append(int(inputs[4]))
            else:
                factory_data[2][1] += int(inputs[5])

                

    print("WAIT",end="")
    move = None
    


    # get possible action

    move = [-1,0,0,-10]
    for f in range(len(factory_data)):
        #print(factory_data[f][0], file=sys.stderr, flush=True)
        if factory_data[f][0] == 1:
            for link in factory_link:
                #print("_",factory_data[link[1]][0], file=sys.stderr, flush=True)
                if link[0] == f and (factory_data[link[1]][0] != 1):
                    if factory_data[link[1]][1] +1 <= factory_data[f][1] and not link[1]  in troop_data:
                        # set priority
                        print(link[0],troop_data, file=sys.stderr, flush=True)
                        priority = (factory_data[link[1]][2]*3) * (abs(factory_data[link[1]][0]) * 2) / ((factory_data[link[1]][1] + 1)) * (link[2] / 5)
                        if move[3] < priority:
                            move = [f,link[1],factory_data[link[1]][1] +1,priority]
    if move[0] != -1:
        print(";MOVE {} {} {}".format(move[0],move[1],move[2]),end="")
    print("")

    factory_data[move[0]][1] -= move[2]
    factory_data[move[1]][1] = 99999999
    #print(time.time())
